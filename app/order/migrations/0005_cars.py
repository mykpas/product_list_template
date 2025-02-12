# Generated by Django 5.1.5 on 2025-01-31 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_orderlist_orderhead_alter_orderhead_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=50, null=True, verbose_name='Марка')),
                ('model', models.CharField(blank=True, max_length=50, null=True, verbose_name='Модель')),
                ('color', models.CharField(blank=True, max_length=50, null=True, verbose_name='Колір')),
                ('invoice', models.CharField(blank=True, max_length=50, null=True, verbose_name='Інвойс')),
            ],
            options={
                'verbose_name': 'автомобіль',
                'verbose_name_plural': 'автомобілі',
            },
        ),
    ]
