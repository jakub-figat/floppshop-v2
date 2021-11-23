from tortoise import fields, models


class User(models.Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(max_length=100, unique=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=500)
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    date_of_birth = fields.DateField()
    is_active = fields.BooleanField(default=True)
