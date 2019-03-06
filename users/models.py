from django.conf import settings
from django.contrib import AbstractUser
from django.db import models


class User(AbstractUser):
    '''
    Implementing multiple roles for users by inheriting from Django's "AbstractUser" model
    by adding boolean fields.
    '''
    is_dealergroup = models.BooleanField(default=False)
    is_dealerbranch = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class DealerGroup(models.Model):
    '''Model representing a dealer group'''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=155, unique=True)
    nick_name = models.CharField(max_length=155, unique=True, blank=True)
    branch = models.OneToOneField('DealerBranch', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class DealerBranch(models.Model):
    '''Model representing the Dealer Branch'''
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'users'
        ordering = ['-timestamp']

    def __str__(self):
        return self.name


class Employee(models.Model):
    '''Class Representing an employee'''
    FEMALE = 'F'
    MALE = 'M'

    GENDER = (
        (FEMALE, 'Female'),
        (MALE, 'Male')
    )

    BRANCH_MANAGER = 'BM'
    SALES_SUPERVISOR = 'SS'
    SALES_CONSULTANT = 'SC'
    SALES_MANAGER = 'SM'
    SALES_COUNTER = 'SC'
    OPERATION_MANAGER = 'OM'

    POSITIONS = (
        (BRANCH_MANAGER, 'Branch Manager'),
        (SALES_SUPERVISOR, 'Sales Supervisor'),
        (SALES_CONSULTANT, 'Sales Consultant'),
        (SALES_MANAGER, 'Sales Manager'),
        (SALES_COUNTER, 'Sales Counter'),
        (OPERATION_MANAGER, 'Operation Manager')
    )
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    slug = models.SlugField(blank=True, null=True)
    picture = models.ImageField(upload_to='users/avatars', default='users/avatars/default.png')
    # employee_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    birth_place = models.CharField(max_length=255)
    birth_date = models.DateField()
    # address fields
    province = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=55)
    nik = models.CharField(max_length=16, unique=True, null=True)
    phonenumber = PhoneNumberField(blank=True)
    mobile_number = PhoneNumberField(blank=True)
    email = models.EmailField(null=True)
    dealer_branch = models.ForeignKey(DealerBranch, on_delete=models.CASCADE, blank=True)
    position = models.CharField(max_length=122, choices=POSITIONS, 
        default=SALES_SUPERVISOR)
    date_joined = models.DateField(auto_now=False)
    # training 
    # work_experience

    class Meta:
        app_label = 'users'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
