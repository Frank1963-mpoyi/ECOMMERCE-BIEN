# import configparser

from .base import *


# DEBUG = True

ALLOWED_HOSTS = [
    'localhost',  '127.0.0.1'
]



#DATABASE_ROUTERS = ['config.router.AuthRouter']

# CONFIG_DIR = os.path.join(BASE_DIR, 'config')

# parser = configparser.ConfigParser()
# parser.read_file(open(os.path.join(CONFIG_DIR, 'app.ini')))

# DATABASES = {
#     'default': {
#         'ENGINE'    : 'django.db.backends.postgresql',
#         'NAME'      : parser.get('blog', 'name'),
#         'USER'      : parser.get('blog', 'user'),
#         'PASSWORD'  : parser.get('blog', 'password'),
#         'HOST'      : parser.get('blog', 'host'),
#         'PORT'      : parser.getint('blog', 'port'),
#     }
# }










ENVIRONMENT = 'DEVELOPMENT'

print("\n")
print("DEBUG        = ", DEBUG)
print("MODE         = ", ENVIRONMENT)
print("TEMPLATES    = ", TEMPLATES[0]['DIRS'])
print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT)
print("\n")
