# Generated by Django 3.0.5 on 2020-05-20 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.IntegerField(primary_key='true', serialize=False)),
                ('idUsuario', models.IntegerField()),
                ('fiebre', models.BooleanField()),
                ('tos_seca', models.BooleanField()),
                ('asfixia', models.BooleanField()),
                ('perdida_sentidos', models.BooleanField()),
                ('repentino', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.IntegerField(primary_key='true', serialize=False)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=1)),
                ('cp', models.CharField(max_length=5)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
            ],
        ),
    ]
