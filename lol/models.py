from django.db import models

# Create your models here.
class Test(models.Model):
  text_name = models.CharField(max_length=255, default="")


class Player(models.Model):
    gameName = models.CharField(max_length=255, default="")
    puuid = models.CharField(max_length=255, default="")
    summonerId = models.BigIntegerField(default=0)
    summonerName = models.CharField(max_length=255, default="")


class GameDetail(models.Model):
    championId = models.IntegerField(default=0)
    kills = models.IntegerField(default=0, verbose_name="击杀")
    deaths = models.IntegerField(default=0, verbose_name="死亡")
    assists = models.IntegerField(default=0, verbose_name="助攻")
    doubleKills = models.IntegerField(default=0, verbose_name="双杀次数")
    tripleKills = models.IntegerField(default=0, verbose_name="三杀次数")
    quadraKills = models.IntegerField(default=0, verbose_name="四杀次数")
    pentaKills = models.IntegerField(default=0, verbose_name="五杀")
    item0 = models.IntegerField(default=0)
    item1 = models.IntegerField(default=0)
    item2 = models.IntegerField(default=0)
    item3 = models.IntegerField(default=0)
    item4 = models.IntegerField(default=0)
    item5 = models.IntegerField(default=0)
    item6 = models.IntegerField(default=0)
    totalDamageDealtToChampions = models.IntegerField(default=0, verbose_name="对英雄造成伤害")
    totalDamageTaken = models.IntegerField(default=0, verbose_name="承受伤害")
    win = models.SmallIntegerField(default=0, verbose_name="赢否？")


class Game(models.Model):
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    gameId = models.IntegerField(primary_key=True)
    gameMode = models.CharField(default="", max_length=255)
    gameCreation = models.IntegerField(default=0)
    gameCreationDate = models.DateTimeField()
    gameType = models.CharField(default="", max_length=255)
    gameDetail = models.ForeignKey(to=GameDetail, on_delete=models.CASCADE)
