"""
Django command to wait for the database to be available
"""
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as Psycopg2OpError

import time


class Command(BaseCommand):
    """Django Commnad to wait for db"""

    def handle(self, *args, **options):
        """Wait for db command enteryPoint"""
        Db_up = False
        while not Db_up:
            try:
                self.check(databases=['default'])
                Db_up = True
            except (OperationalError, Psycopg2OpError):
                self.stdout.write("Database unavaliable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("database avaliable !"))
