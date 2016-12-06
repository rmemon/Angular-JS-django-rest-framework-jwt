from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    # category_id = models.IntegerField(blank=True, null=True, db_index=True)
    user_id = models.IntegerField(blank=True, null=True, db_index=True)
    ownername = models.CharField(max_length=255, blank=True, null=True)
    charge_perhour = models.CharField(max_length=15, blank=True, null=True)
    charge_perday = models.CharField(max_length=15, blank=True, null=True)
    charge_perweek = models.CharField(max_length=15, blank=True, null=True)
    i_date = models.IntegerField(blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True, default='y')
    is_deleted = models.CharField(max_length=1, blank=True, null=True, default='n')
    i_by = models.IntegerField(blank=True, null=True)
    u_by = models.IntegerField(blank=True, null=True)