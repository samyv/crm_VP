from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import PermissionsMixin

SEX_CHOICES = (
    ("M", "MALE"),
    ("F", "FEMALE"),
    ("X", "Other")
)

# class User(AbstractUser):
#     pass

class Race(models.Model):
    race_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.race_name}"

class Dog(models.Model):
    name = models.CharField(max_length=50)
    race = models.ForeignKey("Race", on_delete=models.SET_NULL, null=True)
    sex = models.CharField(choices=SEX_CHOICES,max_length=500)
    # puce = models.IntegerField(max_length=15)
    # vaccin_PLH = models.DateField()
    # vaccin_carre = models.DateField()
    # vaccin_toux = models.DateField()
    # vaccin_rage = models.DateField()
    # carnet = models.CharField(max_length=20)
    responsibles = models.ManyToManyField("Member", related_name="responsibles")
    conducteurs = models.ManyToManyField("Member", related_name="conducteurs")
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.id} {self.name}"

# =============================================================
# class User(AbstractUser):
#     pass

class Member(models.Model):
    
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    sex = models.CharField(choices=SEX_CHOICES,max_length=500)
    address = models.ForeignKey("Address",on_delete=models.SET_NULL, null=True)
    birthdate = models.DateField()
    created_on = models.DateField(auto_now_add=True)


    
    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"

class Address(models.Model):
    country = models.CharField(max_length=20, default="Belgium")
    street = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=8)
    number = models.IntegerField()
    boxcode = models.CharField(max_length=4, null=True)

    def __str__(self):
        return f"{self.id} {self.street} {self.number} {self.zipcode} {self.country}" 



class Insurance(models.Model):
    insurance_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

class Insurance_contract(models.Model):
  contract_number = models.CharField(max_length=50)
  expiry_date = models.DateField()
  subscriber = models.ForeignKey(Member, on_delete=models.CASCADE)
  insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)




