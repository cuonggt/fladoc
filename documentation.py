import io
import os
import mistune


class Documentation:
    def __init__(self, cache):
        self.cache = cache

    @staticmethod
    def get_doc_versions():
        return {
            'master': 'Master',
            '0.12': '0.12'
        }

    def get(self, version, page):
        cache_key = 'docs.' + version + '.' + page

        content = self.cache.get(cache_key)

        path = self.page_path(version, page)

        return content if content else self.read_content_and_cache(version, path, cache_key)

    def read_content_and_cache(self, version, path, cache_key):
        if not os.path.isfile(path):
            return ''

        content = self.replace_links(version, mistune.markdown(self.read_file(path), False))

        self.cache.set(cache_key, content, timeout=5 * 60)

        return content

    def get_index(self, version):
        return self.get(version, 'index')

    def section_exist(self, version, page):
        return os.path.isfile(self.page_path(version, page))

    def page_path(self, version, page):
        return self.base_path('/resources/docs/' + version + '/' + page + '.md')

    @staticmethod
    def replace_links(version, content):
        return content.replace('{{version}}', version)

    @staticmethod
    def base_path(path):
        return os.getcwd() + path

    @staticmethod
    def read_file(path):
        with io.open(path, 'r', encoding='utf8') as f:
            return f.read()
