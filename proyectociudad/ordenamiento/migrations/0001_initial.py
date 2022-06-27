# Generated by Django 4.0.5 on 2022-06-27 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo_parroquia', models.CharField(choices=[('urbana', 'URBANA'), ('rural', 'RURAL')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('num_viviendas', models.IntegerField(verbose_name='número de viviendas')),
                ('num_parques', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], verbose_name='número de parques')),
                ('num_edificios', models.IntegerField(verbose_name='número de edificios')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losbarrios', to='ordenamiento.parroquia')),
            ],
        ),
    ]
