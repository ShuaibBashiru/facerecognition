from django.db import models

#
# # Create your models here.
# class AdminAccount(models.Model):
#     surname = models.CharField(max_length=50)
#     firstname = models.CharField(max_length=50)
#     othername = models.CharField(max_length=50)
#     email_one = models.CharField(max_length=50)
#     phone_one = models.CharField(max_length=50)
#     countryCode = models.CharField(max_length=50)
#     persional_id = models.CharField(max_length=50)
#     account_type = models.CharField(max_length=50)
#     pwd_auth = models.CharField(max_length=50)
#     created_by = models.CharField(max_length=50)
#     date_created = models.CharField(max_length=10)
#     last_modified = models.CharField(max_length=10)
#
#     class Meta:
#         db_table = 'admin_record'
#
#
# class UserAccount(models.Model):
#     surname = models.CharField(max_length=50)
#     firstname = models.CharField(max_length=50)
#     othername = models.CharField(max_length=50)
#     email_one = models.CharField(max_length=50)
#     phone_one = models.CharField(max_length=50)
#     gender = models.CharField(max_length=50)
#     age = models.CharField(max_length=50)
#     countryCode = models.CharField(max_length=50)
#     persional_id = models.CharField(max_length=50)
#     account_type = models.CharField(max_length=50)
#     pwd_auth = models.CharField(max_length=50)
#     created_by = models.CharField(max_length=50)
#     date_created = models.CharField(max_length=10)
#     last_modified = models.CharField(max_length=10)
#
#     class Meta:
#         db_table = 'user_record'
