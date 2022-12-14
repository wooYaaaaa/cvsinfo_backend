# Generated by Django 4.1.3 on 2022-12-14 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvsinfo', '0008_rename_imageurl_product_imgurl_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('parcel', models.BooleanField()),
                ('coffee', models.BooleanField()),
                ('fried', models.BooleanField()),
                ('atm', models.BooleanField()),
                ('toto', models.BooleanField()),
                ('hour24', models.BooleanField()),
                ('loto', models.BooleanField()),
            ],
            options={
                'db_table': 'feature',
            },
        ),
    ]
