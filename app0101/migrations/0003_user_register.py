# Generated by Django 3.0.8 on 2020-07-15 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app0101', '0002_auto_20200715_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('Idno', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Contact_No', models.IntegerField(unique=True)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]