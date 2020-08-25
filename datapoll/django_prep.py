import django

import sys
import os


cur_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)))
base_dir = os.path.join(cur_dir, '..')
sys.path.extend([base_dir])

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wifioccupy.settings")
django.setup()

from django.conf import settings
