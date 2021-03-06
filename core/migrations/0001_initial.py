# Generated by Django 3.2.8 on 2021-10-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ncm', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('data_criacao', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'produto',
            },
        ),
    ]
