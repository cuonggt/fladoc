from flask import Flask, render_template, redirect, abort
from documentation import Documentation
from lxml import html
from werkzeug.contrib.cache import SimpleCache

DEFAULT_VERSION = '0.12'

app = Flask(__name__, static_url_path='')

docs = Documentation(SimpleCache())


@app.route('/')
def welcome():
    return render_template('welcome.html', current_version=DEFAULT_VERSION)


@app.route('/docs/')
def show_root_page():
    return redirect('/docs/' + DEFAULT_VERSION)


@app.route('/docs/<version>/')
@app.route('/docs/<version>/<page>')
def show(version, page=None):
    if not is_version(version):
        return redirect('/docs/' + DEFAULT_VERSION + '/' + version, 301)

    if not page:
        page = ''

    section_page = page if page else 'installation'

    content = docs.get(version, section_page)

    if not content:
        abort(404)

    title = html.fromstring(content).xpath('//h1')

    section = ''

    if docs.section_exist(version, page):
        section += '/' + page
    elif page:
        return redirect('/docs' + version)

    canonical = ''

    if docs.section_exist(DEFAULT_VERSION, section_page):
        canonical = '/docs/' + DEFAULT_VERSION + '/' + section_page

    return render_template('docs.html',
                           title=title[0].text if len(title) > 0 else None,
                           index=docs.get_index(version),
                           content=content,
                           current_version=version,
                           versions=Documentation.get_doc_versions(),
                           current_section=section,
                           canonical=canonical)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


def is_version(version):
    return version in Documentation.get_doc_versions()
