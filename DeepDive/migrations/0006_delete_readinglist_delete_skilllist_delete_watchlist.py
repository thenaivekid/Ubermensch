# Generated by Django 4.1 on 2022-10-17 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DeepDive', '0005_rename_agreableness_personalitytraits_agreeableness'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReadingList',
        ),
        migrations.DeleteModel(
            name='SkillList',
        ),
        migrations.DeleteModel(
            name='WatchList',
        ),
    ]
