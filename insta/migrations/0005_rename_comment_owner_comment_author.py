# Generated by Django 4.0.3 on 2022-03-15 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_likes_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_owner',
            new_name='author',
        ),
    ]
