import io
import os
import mistune


class Documentation:
    @classmethod
    def get_doc_versions(cls):
        return {
            'master': 'Master',
            '0.12': '0.12'
        }

    @classmethod
    def get(cls, version, page):
        path = cls.base_path('/resources/docs/' + version + '/' + page + '.md')

        if not os.path.isfile(path):
            return None

        return cls.replace_links(version, cls.markdown(cls.read_file(path)))

    @classmethod
    def get_index(cls, version, page):
        path = cls.base_path('/resources/docs/' + version + '/documentation.md')

        if not os.path.isfile(path):
            return None

        return cls.replace_links(version, cls.markdown(cls.read_file(path)))

    @classmethod
    def replace_links(cls, version, content):
        return content.replace('{{version}}', version)

    @classmethod
    def markdown(cls, text):
        return mistune.markdown(text, False)

    @classmethod
    def section_exist(cls, version, page):
        return os.path.isfile(cls.base_path('/resources/docs/' + version + '/' + page + '.md'))

    @classmethod
    def base_path(cls, path):
        return os.getcwd() + path

    @classmethod
    def read_file(cls, path):
        with io.open(path, 'r', encoding='utf8') as f:
            return f.read()
