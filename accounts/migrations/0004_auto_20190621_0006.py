# Generated by Django 2.1 on 2019-06-20 18:36

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190619_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='SIG',
        ),
        migrations.AddField(
            model_name='status',
            name='SIG_aux',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('SR', 'Script'), ('VR', 'Vriddhi'), ('RO', 'Robotics'), ('CA', 'Capital'), ('ME', 'Media')], max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='status',
            name='SIG_main',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('CO', 'Code'), ('GD', 'Gadget'), ('GR', 'Garage')], max_length=8, null=True),
        ),
    ]
