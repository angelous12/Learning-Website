# Generated by Django 4.0.4 on 2022-06-17 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_delete_homework'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='ip',
        ),
        migrations.RemoveField(
            model_name='contactmessage',
            name='subject',
        ),
    ]