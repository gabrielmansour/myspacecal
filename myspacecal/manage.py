#!/usr/bin/env python

from socket import gethostname
import os
import sys

PRODUCTION_HOSTS = []

if __name__ == "__main__":
    if gethostname() in PRODUCTION_HOSTS:
        settings = "settings.production"
    else:
        settings = "settings.development"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
