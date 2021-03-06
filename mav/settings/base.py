from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#((5d6%!g$!-fj&lfl(rk3s0@l1s#6vwrrisl%93xhsp1i+17c'


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
   'apps.base',
   'apps.users',
   'apps.agentes',
   'apps.cpd',
]

THIRD_APPS = [
    "corsheaders" ,
    'rest_framework',
    'rest_framework.authtoken',
    'simple_history',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

# Tiempo de xpiracion del token
TOKEN_EXPIRED_AFTER_SECOND = 900

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mav.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mav.wsgi.application'

# Configuraciuon global de pagination para djangon-rest-framework

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
            'drf_renderer_xlsx.renderers.XLSXRenderer',
        ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

'''
Esta configuraciuon indica desde que host estara permitido recibir peticiones
CORS_ALLOWED_ORIGINS  = [
     "https://example.com" ,
     "https://sub.example.com" ,
     "http: // localhost: 8080" ,
     "http://127.0.0.1:9000" ,
]
'''

# En este caso le indico que sera solo del puerto 3000
CORS_ALLOWED_ORIGINS  = [
     "http://127.0.0.1:3000"
]

# Anteriormente se llamaba a esta configuraci??n CORS_ORIGIN_WHITELIST, 
# que todav??a funciona como un alias, con el nuevo nombre teniendo prioridad.
# Como da error con el valor anterior, configuro tamien con el nombre de WHITELIST

CORS_ORIGIN_WHITELIST  = [
     "http://127.0.0.1:3000"
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
