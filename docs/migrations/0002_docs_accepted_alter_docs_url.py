# Generated by Django 5.1.3 on 2024-11-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='docs',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
