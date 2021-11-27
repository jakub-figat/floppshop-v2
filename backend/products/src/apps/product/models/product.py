from tortoise import fields, models


class Category(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=50)


class Product(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=6, decimal_places=2)
    categories: models.ManyToManyRelation[Category] = fields.ManyToManyField("products.Category")
