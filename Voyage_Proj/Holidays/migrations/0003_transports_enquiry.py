# Generated by Django 3.0 on 2020-10-05 13:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Holidays', '0002_delete_transport_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transports_Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(default='', max_length=159)),
                ('Phone', models.CharField(default='', max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,12}$')])),
                ('Email', models.EmailField(max_length=159)),
                ('Jouryney_Date', models.DateField()),
                ('Journey_By', models.CharField(choices=[('Train', 'Train'), ('Bus', 'Bus')], max_length=129)),
            ],
        ),
    ]