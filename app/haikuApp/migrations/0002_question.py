# Generated by Django 3.1.4 on 2020-12-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haikuApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=50)),
                ('question_text', models.CharField(max_length=100)),
            ],
        ),
    ]
