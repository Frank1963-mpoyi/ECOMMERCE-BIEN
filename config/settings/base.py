
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
            )
        )
    )


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8s4yb1v53n)=g_m@^8ufk54is*#5z06g5in%o6%&6r4oy0-=o1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Project Apps
    'ecommerce.apps.system.accounts',
    'ecommerce.apps.system.blog',
    'ecommerce.apps.system.authenticate',
    
    # 3rd party  
    'django_filters',      
    #'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #enable debug tool_bar
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE'    :   'django.db.backends.postgresql',
        'NAME'      :   'ecommerce',
        'USER'      :   'postgres',
        'PASSWORD'  :   'paulin63',
        'HOST'      :   'localhost'
            
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE   = 'en-us'

TIME_ZONE       = 'Africa/Johannesburg'

USE_I18N        = True

USE_L10N        = True

USE_TZ          = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL          = '/static/'
STATIC_ROOT         = os.path.join(BASE_DIR, 'ecommerce/static')

STATICFILES_DIRS    =[
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL           = '/images/'
MEDIA_ROOT          = os.path.join(BASE_DIR, 'ecommerce/static/media')


# Internal Ip for Debug tool bar
#INTERNAL_IPS = ['127.0.0.1']

