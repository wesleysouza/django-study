# Generated by Django 3.2.8 on 2021-11-07 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('surname', models.CharField(max_length=100, verbose_name='surname')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='nome',
            new_name='name',
        ),
    ]
