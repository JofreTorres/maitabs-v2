# Generated by Django 3.0.2 on 2020-01-19 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_album_artista_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=70)),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=70)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Album')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Artista')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Genero')),
            ],
        ),
    ]