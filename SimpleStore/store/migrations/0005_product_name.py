# Generated by Django 2.0.6 on 2018-07-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20180702_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='0000000', max_length=500),
        ),
    ]