# django-opengauss-backend

openGauss database dialect for django

## Requirements

- openGauss psycopg2
- django >= 2.2

## Install

```shell
pip install django-opengauss-backend
```

## Usage

You can set the name in your Django project `settings.py` as:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django_opengauss_backend',
        'NAME': '<database name>',
        'USER': '<database username>',
        'PASSWORD': '<database password>',
        'HOST': '<database host>',
        'PORT': '5432',
    }
}
```
