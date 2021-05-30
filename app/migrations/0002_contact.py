# Generated by Django 3.1.7 on 2021-05-28 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Mobile', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.TextField()),
                ('Customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
        ),
    ]
