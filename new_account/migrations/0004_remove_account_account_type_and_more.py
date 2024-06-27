# Generated by Django 5.0.6 on 2024-06-26 14:45

import new_account.utility
import new_account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_account', '0003_rename_account_balance_account_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='Account_Type',
        ),
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default=new_account.utility.generate_account_number, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='pin',
            field=models.CharField(max_length=4, validators=[new_account.validators.validate_pin]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('SAVINGS', 'Savings'), ('CURRENT', 'Current'), ('DOMICILIARY', 'Domiciliary')], default='SAVINGS', max_length=11),
        ),
    ]
