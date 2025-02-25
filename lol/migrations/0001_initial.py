# Generated by Django 3.2.13 on 2024-10-16 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('championId', models.IntegerField(default=0)),
                ('kills', models.IntegerField(default=0)),
                ('deaths', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('doubleKills', models.IntegerField(default=0)),
                ('tripleKills', models.IntegerField(default=0)),
                ('quadraKills', models.IntegerField(default=0)),
                ('pentaKills', models.IntegerField(default=0)),
                ('item0', models.IntegerField(default=0)),
                ('item1', models.IntegerField(default=0)),
                ('item2', models.IntegerField(default=0)),
                ('item3', models.IntegerField(default=0)),
                ('item4', models.IntegerField(default=0)),
                ('item5', models.IntegerField(default=0)),
                ('item6', models.IntegerField(default=0)),
                ('totalDamageDealtToChampions', models.IntegerField(default=0)),
                ('totalDamageTaken', models.IntegerField(default=0)),
                ('win', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameName', models.CharField(default='', max_length=255)),
                ('puuid', models.CharField(default='', max_length=255)),
                ('summonerId', models.IntegerField(default=0)),
                ('summonerName', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('gameId', models.IntegerField(primary_key=True, serialize=False)),
                ('gameMode', models.CharField(default='', max_length=255)),
                ('gameCreation', models.IntegerField(default=0)),
                ('gameCreationDate', models.DateTimeField()),
                ('gameType', models.CharField(default='', max_length=255)),
                ('gameDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lol.gamedetail')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lol.player')),
            ],
        ),
    ]
