import os

# Add your server domain or IP address here in single ('') or double ("") quotes
# to host Alora on your computer/server
#
#       ex. ALLOWED_HOSTS = ['alora.ddns.net']

ALLOWED_HOSTS = ['aloradevs.ddns.net', 'alora.ddns.net', '*']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# change the DATABASES setting to link Alora to a another Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + 'db.sqlite3',
    }
   # 'default': {
    #    'ENGINE': 'django.db.backends.mysql',
     #3   'NAME': 'aloradb',
       # 'USER': 'root',
        #'PASSWORD': '3xtr4S3cur3P455@NoCrackAlora',
        #'HOST': 'aloradevs.ddns.net',
        #'PORT': '3306',
        #'OPTIONS': {'charset': 'utf8mb4'},
    #}
}

# configure the email backend to send emails through Alora
# By default, only available while in Production (while DEBUG = False)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'aloralsteam@gmail.com'
EMAIL_HOST_PASSWORD = 'euvhgmoixzwkrdth'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
