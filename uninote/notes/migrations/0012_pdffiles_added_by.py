# Generated by Django 2.2.2 on 2019-07-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0011_pdffiles_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffiles',
            name='added_by',
            field=models.TextField(default=1, editable=False, max_length=20),
        ),
    ]
