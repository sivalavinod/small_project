# Generated by Django 2.2.7 on 2019-12-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('dept', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('d_o_j', models.DateField()),
            ],
        ),
    ]
