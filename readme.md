# Fladoc

This is a **modern** markdown versionable documentation skeleton based on [Flask framework](http://flask.pocoo.org/docs/0.12/).

## Installation

To get started with Fladoc, you must install Python 2.7 and `virtualenv` to create a virtual environment for the project.
  
    git clone git@github.com:cuonggt/fladoc.git
    cd fladoc
    virtualenv -p python .venv
    source .venv/bin/activate
    
Next, install Fladoc's dependencies:

    pip install -r requirements.txt
    

Then, you can start Fladoc:

    export FLASK_APP=fladoc.py
    flask run

Default, Fladoc will run on http://127.0.0.1:5000/.

![screenshot](https://cloud.githubusercontent.com/assets/8156596/25067246/942b4f24-2267-11e7-8777-8592b6b03946.png)

## Documentation

The site has two main sections. The welcome page which is located at `templates/welcome.html` and the documentation pages.

The website's documentation is loaded from the `resources/docs` directory. You will need to clone each version of the documentation into this directory. For example, `resources/docs/0.12`, etc. The default index file is `documentation.md`. All of the example documentation is stored on GitHub at [cuonggt/flask-docs](https://github.com/cuonggt/flask-docs).

    cd resources
    mkdir docs
    git clone git@github.com:cuonggt/flask-docs.git 0.12
    git clone git@github.com:cuonggt/flask-docs.git master
    
## License

Fladoc is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).
