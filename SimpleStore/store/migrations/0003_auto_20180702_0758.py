# Generated by Django 2.0.6 on 2018-07-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180702_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imglink',
            field=models.CharField(default='0000000', editable=False, max_length=800),
        ),
    ]
