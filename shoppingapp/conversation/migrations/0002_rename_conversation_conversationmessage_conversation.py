# Generated by Django 4.2.5 on 2023-09-15 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='Conversation',
            new_name='conversation',
        ),
    ]
