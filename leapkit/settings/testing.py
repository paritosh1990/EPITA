
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
		}
}
TEST_DISCOVER_TOP_LEVEL = BASE_DIR
TEST_DISCOVER_ROOT 		= BASE_DIR
TEST_DISCOVER_PATTERN 	= 'test_'