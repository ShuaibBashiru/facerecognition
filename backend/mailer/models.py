from django.db import models


class New_password_model(models.Model):
    email_one = models.CharField(max_length=50)
    resetCode = models.CharField(max_length=100)
    status_id = models.IntegerField()
    expire_date = models.TimeField()
    date_created = models.DateField()
    time_created = models.TimeField()
    date_modified = models.DateField()
    time_modified = models.TimeField()

    class Meta:
        db_table = 'reset_password'
