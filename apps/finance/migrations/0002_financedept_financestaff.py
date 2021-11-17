# Generated by Django 3.2.6 on 2021-11-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceDept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('admin_1', 'Admin1'), ('admin_2', 'Admin2')], default='', max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=25)),
                ('sex', models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE')], max_length=7)),
                ('age', models.DateField()),
                ('Phone', models.CharField(max_length=17, verbose_name='Phone')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('title', models.CharField(default='', max_length=15, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]