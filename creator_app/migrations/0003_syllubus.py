# Generated by Django 4.2.2 on 2023-07-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purpose', '0002_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='syllubus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
