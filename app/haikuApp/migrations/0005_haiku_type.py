# Generated by Django 3.1.4 on 2020-12-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haikuApp', '0004_remove_question_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='haiku',
            name='type',
            field=models.CharField(default='default', max_length=50),
        ),
    ]