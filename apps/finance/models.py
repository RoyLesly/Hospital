from django.db import models
from apps.account.models import Account
from django.db.models.signals import post_save
from apps.root.models import CommonStaff


DEPTS = (('admin_1', 'Admin1'), ('admin_2', 'Admin2'))


# ==================== USER FOR FINANCE ========================================================
class FinanceUser(models.Model):
    username = models.OneToOneField(Account, unique=True, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.username)


def create_finUser(sender, **kwargs):
    if kwargs['created']:
        created_obj = Account.objects.all().order_by('date_joined').last().username
        name = created_obj.username
        if name == 'Finance' or name == 'zane' or name == 'admin':
            finUser = FinanceUser.objects.create(username=created_obj)


post_save.connect(create_finUser, sender=Account)

# -----------------------------------------------------------------------------------------------


class FinanceDept(models.Model):
    name = models.CharField(max_length=15, unique=True,
                            default='', choices=DEPTS)

    def __str__(self):
        return str(self.name.upper())


class FinanceStaff(CommonStaff):
    title = models.CharField(max_length=15, unique=True, default='',)

    def __str__(self):
        return str(self.first_name.upper())


class Income(models.Model):
    class IncomeTypes(models.IntegerChoices):
        CONS = 1, "CONSULTATION"
        DONA = 2, "DONATIONS"

    class RInterval(models.IntegerChoices):      # Repetition interval
        NA = 1, "NOT APPLICABLE"
        DAY = 2, "DAYS"
        WEK = 3, "WEEKS"
        MON = 4, "MONTHS"
        YEA = 5, "YEARS"
    amount = models.IntegerField()
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=IncomeTypes.choices)
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices=RInterval.choices)
    repetition_time = models.PositiveSmallIntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Income {self.id} {self.date.strftime("%Y/%m/%d")}'     # %H:%M:%S

    class Meta:
        verbose_name_plural = "incomes"


class Expense(models.Model):
    class ETypes(models.IntegerChoices):
        SAL = 1, "SALARY"
        REN = 2, "BONUS"
        LIG = 3, "LIGHT"
        WAT = 4, "WATER"
        MAI = 5, "MAINTENANCE"
        TAX = 6, "TAX"
        OTH = 7, "OTHERS"

    class RInterval(models.IntegerChoices):  # Repetition interval
        NA = 1, "NOT APPLICABLE"
        DAY = 2, "DAYS"
        WEK = 3, "WEEKS"
        MON = 4, "MONTHS"
        YEA = 5, "YEARS"
    amount = models.IntegerField()
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=ETypes.choices)      # savings etc
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices=RInterval.choices)
    repetition_time = models.PositiveSmallIntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Expenses {self.id} - {self.type} - {self.date.strftime("%Y/%m/%d")}'  # %H:%M:%S

    class Meta:
        verbose_name_plural = "Expenses"


class Balance(models.Model):
    class BTypes(models.IntegerChoices):
        CUR = 1, "CUR"
        SAV = 2, "SAVINGS"
    amount = models.IntegerField()
    date = models.DateField()
    type = models.PositiveSmallIntegerField(choices=BTypes.choices)      # balance of saving or current account
    repetitive = models.BooleanField(default=False)
    date_updated = models.DateField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Balance {self.id} {self.type}'     # %H:%M:%S

    class Meta:
        verbose_name_plural = "Balances"
