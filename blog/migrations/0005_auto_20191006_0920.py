# Generated by Django 2.0.8 on 2019-10-06 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190526_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除1')], default=1, verbose_name='状态'),
        ),
    ]
