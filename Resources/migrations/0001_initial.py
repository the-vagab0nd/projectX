# Generated by Django 3.1 on 2020-08-28 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('College', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('embeded_code', models.CharField(max_length=100)),
                ('lecture', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='College.batch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='College.course')),
            ],
        ),
    ]