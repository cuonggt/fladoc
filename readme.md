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

![screenshot](https://photos-2.dropbox.com/t/2/AABM3QWKrC4OTF2IutMSceHYqD6MDD1_pTp8K8p64XC08A/12/2543832/png/32x32/3/1491984000/0/2/Screen%20Shot%202017-04-12%20at%2010.13.20%20AM.png/EI_n-gEYzM68QSAHKAc/HMBRGg5dNWN0kddhgX6_4GQr_1qtTCCEQaYtVolMTCk?dl=0&size=2048x1536&size_mode=3)

## Documentation

The site has two main sections. The welcome page which is located at `templates/welcome.html` and the documentation pages.

The website's documentation is loaded from the `resources/docs` directory. You will need to clone each version of the documentation into this directory. For example, `resources/docs/0.12`, etc. The default index file is `documentation.md`. All of the example documentation is stored on GitHub at [cuonggt/flask-docs](https://github.com/cuonggt/flask-docs).
