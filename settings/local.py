import os
from settings.base import *

SECRET_KEY = os.environ.get('SECRET_KEY', 'default')