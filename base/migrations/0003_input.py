# Generated by Django 3.2.13 on 2022-11-20 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_delete_input'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('eye_sight', models.IntegerField()),
                ('tooth_decay', models.IntegerField()),
                ('hearing_power', models.IntegerField()),
                ('max_blood', models.IntegerField()),
                ('size_skin', models.IntegerField()),
                ('length_difference', models.IntegerField()),
            ],
        ),
    ]
