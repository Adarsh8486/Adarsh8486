# Generated by Django 3.2.7 on 2021-12-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0002_alter_registeruser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=256)),
                ('Quantity_of_product', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('selling_price', models.IntegerField()),
            ],
        ),
    ]
