"""
WSGI config for django_faq project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys # 追加

from django.core.wsgi import get_wsgi_application

# 絶対パスを避ける
FILE_PATH = os.path.dirname(__file__)
PROJECT_NAME = os.path.basename(FILE_PATH)

sys.path.append(os.path.dirname(FILE_PATH))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', PROJECT_NAME + '.settings')

application = get_wsgi_application()
