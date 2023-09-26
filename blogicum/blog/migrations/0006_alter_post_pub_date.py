# Generated by Django 3.2.16 on 2023-09-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации'),
        ),
    ]
