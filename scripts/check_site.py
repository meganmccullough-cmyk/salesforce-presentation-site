#!/usr/bin/env python3
"""Validate portable presentation markup, local assets, and deployment mirrors."""
import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta',
        'param', 'source', 'track', 'wbr'}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.ids = set()
        self.references = []
        self.files = []
        self.flips = []
        self.dialogs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag not in VOID:
            self.stack.append(tag)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate ID: {attrs["id"]}'
            self.ids.add(attrs['id'])
        for key in ['aria-controls', 'aria-labelledby', 'aria-describedby']:
            self.references.extend(attrs.get(key, '').split())
        for key in ['src', 'data-recognition-src']:
            if key in attrs:
                self.files.append(attrs[key])
        href = attrs.get('href', '')
        if href.startswith('#') and len(href) > 1:
            self.references.append(href[1:])
        if 'data-flip-card' in attrs:
            self.flips.append(attrs)
        if tag == 'button' and 'flip-card__toggle' in attrs.get('class', '').split():
            assert attrs.get('aria-controls'), 'Flip toggle lacks details target'
            assert attrs.get('data-card-title'), 'Flip toggle lacks accessible title'
            assert attrs.get('aria-expanded') == 'false', 'Export should start unflipped'
        if tag == 'dialog':
            self.dialogs.append(attrs)

    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, f'Unbalanced closing tag: {tag}'


def check(root):
    root = Path(root).resolve()
    markup = (root / 'index.html').read_text()
    page = Page()
    page.feed(markup)
    assert not page.stack, f'Unclosed tags: {page.stack}'
    for ref in page.references:
        assert ref in page.ids, f'Missing referenced ID: {ref}'
    assert page.flips, 'No flip cards in presentation'
    for name in ['deckEditToggle', 'deckDownloadHtml', 'fullscreenToggle',
                 'recognition-lightbox', 'recognition-lightbox-close',
                 'recognition-lightbox-frame', 'recognition-lightbox-image']:
        assert name in page.ids, f'Missing script dependency: {name}'
    page.files.extend(re.findall(r'url\([\x27\"]?([^\x27\")]+)', markup))
    for value in page.files:
        url = urlsplit(value)
        if url.scheme or url.netloc or value.startswith('#'):
            continue
        asset = root / unquote(url.path)
        assert asset.is_file(), f'Missing local asset: {value}'
        assert asset.resolve().is_relative_to(root), f'Asset escapes site: {value}'
    public = root / 'public'
    assert (public / 'index.html').read_bytes() == (root / 'index.html').read_bytes(), 'HTML mirrors differ'
    for asset in (root / 'assets').rglob('*'):
        if asset.is_file():
            mirror = public / asset.relative_to(root)
            assert mirror.is_file() and mirror.read_bytes() == asset.read_bytes(), f'Asset mirrors differ: {asset.name}'
    print(f'Passed: markup, {len(page.ids)} unique IDs, {len(page.flips)} flip cards, assets and deployment mirrors')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    args = parser.parse_args()
    try:
        check(args.site)
    except (AssertionError, OSError) as error:
        parser.exit(1, f'Validation failed: {error}\n')
