# Generated by Django 2.2.2 on 2019-09-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('datascience', 'Data Science'), ('machinelearning', 'Machine Learning')], default='datascience', max_length=10),
        ),
    ]