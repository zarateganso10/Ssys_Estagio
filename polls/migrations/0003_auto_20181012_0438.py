# Generated by Django 2.2.dev20181005132628 on 2018-10-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_employee_datadenascimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='CPF',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='Nome',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='SobreNome',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='remuneracao',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='tempo_de_servico',
        ),
        migrations.AddField(
            model_name='employee',
            name='Department',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='Email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='Name',
            field=models.CharField(default='empregado', max_length=50),
            preserve_default=False,
        ),
    ]
