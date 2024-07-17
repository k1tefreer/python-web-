# Generated by Django 4.0.3 on 2024-01-31 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_rename_titile_order_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('img', models.CharField(max_length=120, verbose_name='头像')),
            ],
        ),
    ]
