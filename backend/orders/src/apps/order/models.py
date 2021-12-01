from tortoise import fields, models
from tortoise.validators import MinValueValidator


class User(models.Model):
    id = fields.UUIDField(pk=True)
    external_id = fields.UUIDField()
    email = fields.CharField(max_length=100)
    first_name = fields.CharField(max_length=30)
    last_name = fields.CharField(max_length=30)
    username = fields.CharField(max_length=50)
    date_of_birth = fields.DateField()
    is_active = fields.BooleanField(default=True)


class Category(models.Model):
    id = fields.UUIDField(pk=True)
    external_id = fields.UUIDField()
    name = fields.CharField(max_length=50)


class Order(models.Model):
    id = fields.UUIDField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("orders.User")


class Product(models.Model):
    id = fields.UUIDField(pk=True)
    external_id = fields.UUIDField()
    order: fields.ForeignKeyRelation[Order] = fields.ForeignKeyField("orders.Order")
    name = fields.CharField(max_length=100)
    price = fields.DecimalField(max_digits=6, decimal_places=2)
    count = fields.IntField(validators=[MinValueValidator(0)])
    categories: fields.ManyToManyRelation[Category] = fields.ManyToManyField("orders.Category")
