# Generated by Django 3.1.7 on 2021-03-05 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210305_1556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dislikecom',
            old_name='uzer',
            new_name='vlogUser',
        ),
        migrations.RenameField(
            model_name='dislikepost',
            old_name='uzer',
            new_name='vlogUser',
        ),
        migrations.RenameField(
            model_name='likecom',
            old_name='uzer',
            new_name='vlogUser',
        ),
        migrations.RenameField(
            model_name='likepost',
            old_name='uzer',
            new_name='vlogUser',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='uzer',
            new_name='vlogUser',
        ),
    ]