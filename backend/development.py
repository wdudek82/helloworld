# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'helloworld',
        'USER': 'helloworld',
        'PASSWORD': '@@helloworld@@',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}