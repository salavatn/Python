from django.db.models import Model, CharField, IntegerField, ForeignKey, AutoField
from django.db.models import DateField

from django.core.management import execute_from_command_line as django_cli
import django, dj_database_url


from dotenv import load_dotenv

import os, sys
