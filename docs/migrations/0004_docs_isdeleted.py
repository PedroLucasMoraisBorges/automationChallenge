# Generated by Django 5.1.3 on 2024-11-23 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0003_docs_score_alter_docs_dtregister'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
