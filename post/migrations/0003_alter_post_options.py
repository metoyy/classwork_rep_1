# Generated by Django 4.1.7 on 2023-03-15 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_preview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('id',)},
        ),
    ]
