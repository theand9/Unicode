from django.utils import timezone
from django.conf import settings
from django.db import models
import uuid


class loginDetails(models.Model):
    SAP_ID = models.IntegerField(primary_key=True)
    Password = models.CharField(max_length=100, unique=True)
    Two_Step = models.BooleanField(default=False)

    def ___str___(self):
        return "SAP_ID: {}".format(self.SAP_ID)


class userInfo(models.Model):
    SAP_ID = models.OneToOneField(
        loginDetails,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Full_Name = models.CharField(max_length=50, unique=True)
    Phone_No = models.IntegerField(unique=True)
    Email_ID = models.EmailField(unique=True)
    DOB = models.DateField()

    def ___str___(self):
        return "SAP ID: {}, Full Name: {}, Phone No: {}, Email ID: {}, DOB: {}".format(self.SAP_ID, self.Full_Name, self.Phone_No, self.Email_ID, self.DOB)


class userAcc(models.Model):
    SAP_ID = models.OneToOneField(
        loginDetails,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Balance = models.IntegerField()
    Savings_Goal = models.IntegerField()

    def ___str___(self):
        return "SAP ID: {}, Balance: {}, Savings Goal: {}".format(self.SAP_ID, self.Balance, self.Savings_Goal)

    @property
    def Goal_Achieved(self):
        return (self.Savings_Goal - self.Balance) * 100 / self.Savings_Goal if self.Savings_Goal >= self.Balance else "Goal Achieved!! Balance: {} above set goal".format(self.Balance - self.Savings_Goal)


class incomeStream(models.Model):
    class Meta:
        unique_together = (("SAP_ID", "Income_Id"),)

    SAP_ID = models.ForeignKey(
        loginDetails,
        on_delete=models.CASCADE,
    )
    Income_Id = models.UUIDField(
        unique=True, help_text="Auto Generate UID for each user", default=uuid.uuid4)
    Income_Stream = models.CharField(max_length=50)
    Amount = models.IntegerField()
    Income_Date = models.DateTimeField(auto_now_add=True)
    Notes = models.TextField(blank=True, null=True)

    def ___str___(self):
        return "SAP_ID: {}, Income ID: {}, Income Stream: {}, Amount: {}, Income Date: {}".format(self.SAP_ID, self.Income_Id, self.Income_Stream, self.Amount, self.Income_Date)


class Expenses(models.Model):
    class Meta:
        unique_together = (("SAP_ID", "Expense_Id"),)

    EXPENSE_CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Shopping", "Shopping"),
        ("Travel", "Travel"),
        ("Stationery", "Stationery"),
        ("Phone Bill", "Phone Bill"),
        ("Personal", "Personal"),
        ("Leisure", "Leisure"),
        ("Misc", "Miscellaneous"),
    ]

    METHOD_TO_PAY = [
        ("Cash", "Cash"),
        ("Card", "Card"),
        ("E-Wallet", "E-Wallet"),
    ]

    SAP_ID = models.ForeignKey(
        loginDetails,
        on_delete=models.CASCADE,
    )
    Expense_Id = models.UUIDField(
        unique=True, help_text="Auto Generate UID for each user", default=uuid.uuid4)
    Category = models.CharField(
        max_length=10, choices=EXPENSE_CATEGORY_CHOICES)
    Price = models.IntegerField()
    Expense_Date = models.DateTimeField(auto_now_add=True)
    Payment_Mode = models.CharField(max_length=8, choices=METHOD_TO_PAY)
    Bill_Img = models.FileField(
        null=True, blank=True, help_text="Insert bill image here")
    Notes = models.TextField(blank=True, null=True)

    def ___str___(self):
        return "SAP ID: {}, Expense ID: {}, Price: {}, Expense Date: {}, Category: {}, Payment Mode: {}".format(self.SAP_ID, self.Expense_Id, self.Price, self.Expense_Date, self.Category, self.Payment_Mode)
