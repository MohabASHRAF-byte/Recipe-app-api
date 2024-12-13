"""
Django command to wait for the database to be available
"""
from django.core.mangement.base import BaseCommnad


class Command(BaseCommand):
    """
    Django Commnad to wait for db 
    """

    def handle(self,*args,**options):
        pass