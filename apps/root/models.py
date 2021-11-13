from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
SEX_CHOICES = (('FEMALE', 'FEMALE'), ('MALE', 'MALE'))


class CommonStaff(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10, unique=True)
    sex = models.CharField(max_length=7, choices=SEX_CHOICES)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=17)
    address = models.CharField(max_length=20, default='None')
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + "-" + self.last_name)
        super(CommonStaff, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('reg_staff', kwargs={'slug': self.slug})


class CommonPatient(models.Model):
    WARD_CHOICES = (('OPD', 'OPD'),
                    ('MAT', 'Maternity'),
                    ('LW', 'Labour / Delivery'),
                    ('MW', 'Surgical Ward'),
                    ('SW', 'Surgical Ward'),
                    ('CW', "Childrens' Ward"),
                    ('OTHER', 'Other'))
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, unique=False, blank=False)
    address = models.CharField(max_length=25)
    sex = models.CharField(max_length=7, blank=False, choices=SEX_CHOICES)
    age = models.DateField()
    Phone = models.CharField(verbose_name='Phone', max_length=17)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.sn + "-" + self.first_name)
        super(CommonPatient, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name.upper() + " " + self.Phone}'

    def get_absolute_url(self):
        return reverse('reg_patient', kwargs={'slug': self.slug})


class CommonStaff(models.Model):
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, unique=False, blank=False)
    address = models.CharField(max_length=25)
    sex = models.CharField(max_length=7, blank=False, choices=SEX_CHOICES)
    age = models.DateField()
    Phone = models.CharField(verbose_name='Phone', max_length=17)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name + "-" + self.Phone)
        super(CommonStaff, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name.upper() + " " + self.Phone}'

    def get_absolute_url(self):
        return reverse('reg_staff', kwargs={'slug': self.slug})