#!/usr/bin/env python3
"""Copy the neutral presentation starter into a new site directory."""
import argparse
import html
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--title', default='A vision for shared success')
    parser.add_argument('--presenter', default='Presenter')
    parser.add_argument('--organization', default='Team presentation')
    args = parser.parse_args()
    target = args.output.expanduser().resolve()
    if target.exists() and (not target.is_dir() or any(target.iterdir())):
        parser.error(f'Output must be a new or empty directory: {target}')
    template = Path(__file__).resolve().parents[1] / 'assets' / 'template'
    shutil.copytree(template, target, dirs_exist_ok=True)
    page = (target / 'index.html').read_text()
    values = {'__PRESENTATION_TITLE__': args.title, '__PRESENTER__': args.presenter,
              '__ORGANIZATION__': args.organization}
    # One pass prevents a user-supplied value from becoming another substitution.
    import re
    page = re.sub('|'.join(map(re.escape, values)),
                  lambda match: html.escape(values[match.group()], quote=True), page)
    (target / 'index.html').write_text(page)
    public = target / 'public'
    public.mkdir()
    shutil.copy2(target / 'index.html', public / 'index.html')
    shutil.copytree(target / 'assets', public / 'assets')
    print(f'Created site: {target}')


if __name__ == '__main__':
    main()
