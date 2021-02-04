# Static Site + Python

## Python + Html + CSS

- Stack de tecnologías
    - Python
    - Flask / Freeze / Pipenv
    - Jinja
    - Html / CSS / Markdown
    - Deployed on Netlify
    - Hosted on Github

Build:

```
$ pipenv run python freeze.py
```

Virtual ENV

```
$ virtualenv env
$ virtualenv -p /usr/local/bin/python3 env (le digo de usar la v3)
Activar venv: $ source env/bin/activate
Desactivar venv: $ deactivate

```
Run dev entorno PIP

```
$ pipenv run flask run
```

Flask run

```
$ export FLASK_APP=app.py
$ flask run
```

Especie de livereload en dev

```
if __name__ == '__main__':
    app.run(debug=True)
```


*+0+1234 - Sergio Forés - @t0tinspire*