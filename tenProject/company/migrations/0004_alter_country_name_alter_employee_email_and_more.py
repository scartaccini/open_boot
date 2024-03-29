# Generated by Django 4.1.3 on 2022-12-01 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_employee_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='amount',
            field=models.IntegerField(unique=True),
        ),
    ]
