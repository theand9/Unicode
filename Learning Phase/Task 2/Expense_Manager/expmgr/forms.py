from . import models
from django.forms import ModelForm


class UserLoginForm(ModelForm):
    class Meta:
        model = models.loginDetails
        fields = ['SAP_ID', 'Password']


class UserSignupForm(ModelForm):
    class Meta:
        model = models.userInfo
        fields = ['SAP_ID', 'Full_Name', 'Phone_No', 'Email_ID', 'DOB']


class UserIncomeForm(ModelForm):
    class Meta:
        model = models.incomeStream
        fields = ['SAP_ID', 'Income_Id', 'Income_Stream',
                  'Amount', 'Notes']


class UserExpenseForm(ModelForm):
    class Meta:
        model = models.Expenses
        fields = ['SAP_ID', 'Expense_Id', 'Category',
                  'Price', 'Payment_Mode', 'Notes']
