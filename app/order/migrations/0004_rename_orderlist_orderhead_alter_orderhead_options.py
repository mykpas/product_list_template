# Generated by Django 5.1.5 on 2025-01-31 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_create_time_stamp_order_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderList',
            new_name='OrderHead',
        ),
        migrations.AlterModelOptions(
            name='orderhead',
            options={'verbose_name': 'шапка замовлення ', 'verbose_name_plural': 'шапка замовлень'},
        ),
    ]
