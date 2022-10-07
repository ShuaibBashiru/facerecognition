from django.db import models
from django.core.exceptions import ValidationError

class AccountModel(models.Model):
    id = models.IntegerField(primary_key=True)
    personal_id = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 40)
    firstname = models.CharField(max_length = 40)
    othername = models.CharField(max_length = 40, null=True)
    email_one = models.EmailField(max_length = 80)
    phone_code = models.CharField(max_length = 10)
    phone_one = models.CharField(max_length = 50)
    gender_id = models.CharField(max_length = 50, null=True)
    yob = models.CharField(max_length = 50, null=True)
    mob = models.CharField(max_length = 50, null=True)
    dob = models.CharField(max_length = 50, null=True)
    date_created = models.CharField(max_length = 50)
    time_created = models.CharField(max_length = 50)
    generated_id = models.CharField(max_length = 80)

    class Meta:
        db_table = "user_record"
        managed = False


class RecordModel(models.Model):
    id = models.IntegerField(primary_key=True)
    personal_id = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 40)
    firstname = models.CharField(max_length = 40)
    othername = models.CharField(max_length = 40, null=True)
    email_one = models.EmailField(max_length = 80)
    phone_code = models.CharField(max_length = 10)
    phone_one = models.CharField(max_length = 50)
    gender_id = models.CharField(max_length = 50, null=True)
    yob = models.CharField(max_length = 50, null=True)
    mob = models.CharField(max_length = 50, null=True)
    dob = models.CharField(max_length = 50, null=True)
    date_created = models.CharField(max_length = 50)
    time_created = models.CharField(max_length = 50)
    generated_id = models.CharField(max_length = 80)
    file_url = models.TextField()

    class Meta:
        db_table = "vw_user_record"
        managed = False


    def __str__(self):
        return self.personal_id


class UserPassportModel(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length = 20)
    file_name = models.CharField(max_length = 80)
    file_size = models.CharField(max_length = 40)
    file_width = models.CharField(max_length = 40)
    file_height = models.CharField(max_length = 40)
    file_ext = models.EmailField(max_length = 40)
    file_url = models.TextField()
    file_title = models.TextField()
    date_created = models.CharField(max_length = 50)
    time_created = models.CharField(max_length = 50)
    generated_id = models.CharField(max_length = 80)

    class Meta:
        db_table = "user_passport"
        managed = False

    def __str__(self):
        return self.userid