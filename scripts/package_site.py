#!/usr/bin/env python3
"""Synchronize a presentation site and package its deployment copy."""
import argparse
import shutil
import zipfile
from pathlib import Path
from check_site import check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    args = parser.parse_args()
    root = args.site.expanduser().resolve()
    public = root / 'public'
    public.mkdir(exist_ok=True)
    shutil.copy2(root / 'index.html', public / 'index.html')
    shutil.copytree(root / 'assets', public / 'assets', dirs_exist_ok=True)
    check(root)
    archive = root / 'presentation-site.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as output:
        for file in sorted(public.rglob('*')):
            if file.is_file():
                output.write(file, 'presentation-site/' + file.relative_to(public).as_posix())
        if (root / 'LICENSE').is_file():
            output.write(root / 'LICENSE', 'presentation-site/LICENSE')
    print(f'Packaged site: {archive}')


if __name__ == '__main__':
    main()
