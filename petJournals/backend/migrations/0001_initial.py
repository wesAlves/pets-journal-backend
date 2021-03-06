# Generated by Django 4.0.2 on 2022-02-28 19:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id_pert', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birthDate', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('weight', models.FloatField(max_length=100)),
                ('weightUnity', models.CharField(max_length=100)),
                ('imgURL', models.CharField(max_length=100)),
                ('femaleOrMale', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('owner', models.CharField(max_length=100)),
                ('haveMedicines', models.CharField(max_length=100)),
                ('haveVaccines', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
