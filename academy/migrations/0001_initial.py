# Generated by Django 5.0.2 on 2024-04-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enrollment_no', models.IntegerField()),
                ('S_Name', models.CharField(max_length=20)),
                ('S_Age', models.IntegerField()),
                ('Course', models.CharField(max_length=5)),
                ('College', models.CharField(max_length=10)),
            ],
        ),
    ]
