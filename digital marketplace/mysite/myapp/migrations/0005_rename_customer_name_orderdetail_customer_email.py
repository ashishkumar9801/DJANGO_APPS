# Generated by Django 4.1.7 on 2023-02-25 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_customer_email_orderdetail_customer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='customer_name',
            new_name='customer_email',
        ),
    ]
