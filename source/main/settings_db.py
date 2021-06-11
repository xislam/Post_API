ALLOWED_HOSTS = ['localhost']
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'developstoday',
        'USER': 'islam',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }

}