from django.db import models
from django.db import connection

class ModifyModel(object):

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE {} RESTART IDENTITY CASCADE'.format(cls._meta.db_table))

