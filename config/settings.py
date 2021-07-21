import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-j5x3szct0-23x0161iq2yfjwh9v$6yqsce*yt6cd2pmxgu^v%t'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


INSTALLED_APPS = [
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'basket',
    'payment',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories',
                'basket.context_processors.basket'

                # we have access to the categories in every template
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Basket session ID
BASKET_SESSION_ID = "basket"

# setup custom dashboard model
AUTH_USER_MODEL = "account.UserBase"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"

PASSWORD_RESET_TIMEOUT_DAYS = 2
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

######## Stripe payment
os.environ.setdefault("STRIPE_PUBLISHABLE_KEY", "pk_test_51JCUg3KvELx4Sm5hsZduoTWMBghBv5URhepTSx55zH7Bu2Cccnc6dO8r56xzy7TtcYsFyVpbH564ozEihRAWpyLT00pTGCmmv7")
STRIPE_SECRET_KEY = "sk_test_51JCUg3KvELx4Sm5hfSomtogvUhgSZTH0bTL8AIO3tA3os8jQYXVxiDlJSD7ao07xiuwCLcZI2rIb4oCxaDTLI2DZ00KEgxP5bQ"

# Stripe Payment
STRIPE_ENDPOINT_SECRET = "whsec_1mcU0Oe0zvlheUQOJiQZiBsHWbf9X99s"
# Stripe listen --forward-to localhost:8000/payment/webhook