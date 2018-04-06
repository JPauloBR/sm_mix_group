# Generated by Django 2.1.dev20180403030529 on 2018-04-05 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixGroups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]