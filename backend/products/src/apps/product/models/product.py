from tortoise import models, fields


class Product(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=100)
