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

        if content is not None:
            return content

        path = self.base_path('/resources/docs/' + version + '/' + page + '.md')

        if not os.path.isfile(path):
            return None

        content = self.replace_links(version, mistune.markdown(self.read_file(path), False))

        self.cache.set(cache_key, content, timeout=5 * 60)

        return content

    def get_index(self, version):
        cache_key = 'docs.' + version + '.index'

        content = self.cache.get(cache_key)

        if content is not None:
            return content

        path = self.base_path('/resources/docs/' + version + '/documentation.md')

        if not os.path.isfile(path):
            return None

        content = self.replace_links(version, mistune.markdown(self.read_file(path), False))

        self.cache.set(cache_key, content, timeout=5 * 60)

        return content

    @staticmethod
    def replace_links(version, content):
        return content.replace('{{version}}', version)

    def section_exist(self, version, page):
        return os.path.isfile(self.base_path('/resources/docs/' + version + '/' + page + '.md'))

    @staticmethod
    def base_path(path):
        return os.getcwd() + path

    @staticmethod
    def read_file(path):
        with io.open(path, 'r', encoding='utf8') as f:
            return f.read()
