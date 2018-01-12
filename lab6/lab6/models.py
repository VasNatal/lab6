from django.db import models

# Create your models here.
class BookModel(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    year = models.CharField(max_length=6)
    description = models.CharField(max_length=255)
    picture = models.CharField(max_length=100)

class UserModel(models.Model):
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    avatar = models.CharField(max_length=100)

    def validate_unique(self, *args, **kwargs):
        super(UserModel, self).validate_unique(*args, **kwargs)
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        if not self.login:
            print("fgngmhjhgbfdghjmhgbfhjm")
            if self.__class__.objects.filter(...).exists():
                print("bbbbbbbbbbbbbbbbbbbbbbbbbbb")
                raise models.ValidationError('Person with same ... already exists.')

class OrdersModel(models.Model):
    book_id = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
