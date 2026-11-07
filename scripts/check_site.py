#!/usr/bin/env python3
"""Check actual Hwaro output, including project-subpath links and anchors."""
import json
import sys
import tomllib
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.ids = [], set()
        self.titles = self.headings = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        self.titles += tag == 'title'
        self.headings += tag == 'h1'
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])


def check(output):
    base = tomllib.loads(Path('config.toml').read_text())['base_url'].rstrip('/')
    origin = urlsplit(base)
    prefix = origin.path.rstrip('/')
    parsed = {f: Page(f.read_text()) for f in output.rglob('*.html')}
    errors = []

    def resolve(url, source):
        parts = urlsplit(url)
        if parts.scheme not in ('http', 'https') or parts.netloc != origin.netloc:
            return
        path = unquote(parts.path)
        if prefix and path != prefix and not path.startswith(prefix + '/'):
            errors.append(f'{source}: link escapes project path: {url}')
            return
        path = path[len(prefix):].lstrip('/')
        target = output / path
        if target.is_dir() or not path:
            target = target / 'index.html'
        if not target.is_file():
            errors.append(f'{source}: missing target: {url}')
        elif parts.fragment and target in parsed and unquote(parts.fragment) not in parsed[target].ids:
            errors.append(f'{source}: missing anchor: {url}')

    for file, page in parsed.items():
        relative = file.relative_to(output).as_posix()
        current = base + '/' + relative
        if relative.endswith('index.html'):
            current = current[:-len('index.html')]
        if page.titles != 1 or page.headings != 1:
            errors.append(f'{relative}: expected one title and one h1')
        for link in page.links:
            if '{{' in link or '@/' in link:
                errors.append(f'{relative}: unresolved link: {link}')
            resolve(urljoin(current, link), relative)

    for required in ('index.html', 'css/site.css', 'js/site.js', 'favicon.svg', 'search.json', 'sitemap.xml',
                     'css/typography.css', 'images/cloudflare.svg',
                     'fonts/geist-variable-latin.woff2', 'fonts/geist-mono-variable-latin.woff2'):
        if not (output / required).is_file():
            errors.append(f'Missing required output: {required}')
    index_path = output / 'search.json'
    if index_path.is_file():
        index = json.loads(index_path.read_text())
        if not isinstance(index, list) or not index:
            errors.append('Search index must be a nonempty array')
        else:
            for entry in index:
                url = entry.get('url', '')
                if not url:
                    errors.append('Search entry has no URL')
                    continue
                if url.startswith('/') and not (prefix and (url == prefix or url.startswith(prefix + '/'))):
                    url = origin.scheme + '://' + origin.netloc + prefix + url
                resolve(urljoin(base + '/', url), 'search.json')
    if not parsed:
        errors.append('No HTML pages generated')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f'Checked {len(parsed)} HTML pages, local links, anchors, assets and search index.')


if __name__ == '__main__':
    check(Path(sys.argv[1] if len(sys.argv) > 1 else 'public'))
