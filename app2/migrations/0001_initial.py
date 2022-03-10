# Generated by Django 3.2.8 on 2021-12-05 01:40

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
                ('gdate', models.DateField()),
                ('ggnum', models.IntegerField()),
                ('gbnum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'grades',
                'ordering': [],
            },
        ),
        migrations.CreateModel(
            name='TempTables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField(default=True)),
                ('sage', models.IntegerField(db_column='age')),
                ('scontend', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
                ('lastTime', models.DateTimeField(auto_now=True)),
                ('createTime', models.DateTimeField(auto_now=True)),
                ('sgrade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.grades')),
            ],
            options={
                'db_table': 'students',
                'ordering': ['-id'],
            },
            managers=[
                ('stuObj', django.db.models.manager.Manager()),
            ],
        ),
    ]