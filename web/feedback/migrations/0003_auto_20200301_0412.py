# Generated by Django 3.0.3 on 2020-03-01 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_answers_questions_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]