ALLOWED_HOSTS = ['wdudek.pythonanywhere.com', 'localhost']

########
# SQLite
########
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#######
# MySQL
#######
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'helloworld',
#         'USER': 'helloworld',
#         'PASSWORD': '@@helloworld@@',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }