# Generated by Django 2.1.7 on 2019-08-10 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190810_0824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_comment',
            old_name='ticket',
            new_name='blog',
        ),
    ]
