from django.db import models

from twitchscore.apps.summoners.models import Summoner


class Game(models.Model):
    summoner = models.ForeignKey(Summoner, verbose_name='Related summoner')
    riot_id = models.IntegerField(verbose_name='Game ID in RIOT database')
    champion_id = models.PositiveSmallIntegerField(verbose_name='Champion')
    create_date = models.DateTimeField(verbose_name='Create date')
    game_mode = models.CharField(max_length=100, verbose_name='Game mode')
    game_type = models.CharField(max_length=100, verbose_name='Game type')
    invalid = models.BooleanField(verbose_name='Invalid flag')
    ip_earned = models.PositiveIntegerField(verbose_name='IP Earned')
    level = models.PositiveSmallIntegerField(verbose_name='Level')
    map_id = models.PositiveSmallIntegerField(verbose_name='Map')
    spell1 = models.PositiveSmallIntegerField(verbose_name='First summoner spell ID')
    spell2 = models.PositiveSmallIntegerField(verbose_name='Second summoner spell ID')
    sub_type = models.CharField(max_length=100, verbose_name='Game sub-type')
    team_id = models.PositiveSmallIntegerField(verbose_name='Team ID')

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['-pk']


class Player(models.Model):
    game = models.ForeignKey(Game, verbose_name='Related game')
    champion_id = models.PositiveSmallIntegerField(verbose_name='Champion')
    summoner_id = models.PositiveIntegerField(verbose_name='Summoner ID')
    team_id = models.PositiveSmallIntegerField(verbose_name='Team ID')

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['-pk']


class Stats(models.Model):
    game = models.ForeignKey(Game, verbose_name='Related game')
    assists = models.IntegerField(verbose_name='Assists', blank=True, null=True)
    barracks_killed = models.IntegerField(verbose_name='Inhibitors destroyed', blank=True, null=True)
    champions_killed = models.IntegerField(verbose_name='Champions killed', blank=True, null=True)
    combat_player_score = models.IntegerField(verbose_name='Combat player score', blank=True, null=True)
    consumables_purchased = models.IntegerField(verbose_name='Consumables purchased', blank=True, null=True)
    damage_dealt_player = models.IntegerField(verbose_name='Damage dealt player', blank=True, null=True)
    double_kills = models.IntegerField(verbose_name='Double kills', blank=True, null=True)
    first_blood = models.IntegerField(verbose_name='First blood', blank=True, null=True)
    gold = models.IntegerField(verbose_name='Gold', blank=True, null=True)
    gold_earned = models.IntegerField(verbose_name='Gold earned', blank=True, null=True)
    gold_spent = models.IntegerField(verbose_name='Gold spent', blank=True, null=True)
    item0 = models.IntegerField(verbose_name='Item 0', blank=True, null=True)
    item1 = models.IntegerField(verbose_name='Item 1', blank=True, null=True)
    item2 = models.IntegerField(verbose_name='Item 2', blank=True, null=True)
    item3 = models.IntegerField(verbose_name='Item 3', blank=True, null=True)
    item4 = models.IntegerField(verbose_name='Item 4', blank=True, null=True)
    item5 = models.IntegerField(verbose_name='Item 5', blank=True, null=True)
    item6 = models.IntegerField(verbose_name='Item 6', blank=True, null=True)
    items_purchased = models.IntegerField(verbose_name='Items purchased', blank=True, null=True)
    killing_sprees = models.IntegerField(verbose_name='Killing sprees', blank=True, null=True)
    largest_critical_strike = models.IntegerField(verbose_name='Largest critical strike', blank=True, null=True)
    largest_killing_spree = models.IntegerField(verbose_name='Largest killing spree', blank=True, null=True)
    largest_multi_kill = models.IntegerField(verbose_name='Largest multi kill', blank=True, null=True)
    legendary_items_created = models.IntegerField(verbose_name='Legendary items created', blank=True, null=True)
    level = models.IntegerField(verbose_name='Level', blank=True, null=True)
    magic_damage_dealt_player = models.IntegerField(verbose_name='Magic damage dealt player', blank=True, null=True)
    magic_damage_dealt_to_champions = models.IntegerField(verbose_name='Magic damage dealt to champions', blank=True, null=True)
    magic_damage_taken = models.IntegerField(verbose_name='Magic damage taken', blank=True, null=True)
    minions_denied = models.IntegerField(verbose_name='Minions denied', blank=True, null=True)
    minions_killed = models.IntegerField(verbose_name='Minions killed', blank=True, null=True)
    neutral_minions_killed = models.IntegerField(verbose_name='Neutral minions killed', blank=True, null=True)
    neutral_minions_killed_enemy_jungle = models.IntegerField(verbose_name='Neutral minions killed in enemy jungle', blank=True, null=True)
    neutral_minions_killed_your_jungle = models.IntegerField(verbose_name='Neutral minions killed in your jungle', blank=True, null=True)
    nexus_killed = models.BooleanField(verbose_name='Nexus killed', default=False)
    node_capture = models.IntegerField(verbose_name='Node capture', blank=True, null=True)
    node_capture_assist = models.IntegerField(verbose_name='Node capture assist', blank=True, null=True)
    node_neutralize = models.IntegerField(verbose_name='Node neutralize', blank=True, null=True)
    node_neutralize_assist = models.IntegerField(verbose_name='Node neutralize assist', blank=True, null=True)
    num_deaths = models.IntegerField(verbose_name='Number deaths', blank=True, null=True)
    num_items_bought = models.IntegerField(verbose_name='Numbers items bought', blank=True, null=True)
    objective_player_score = models.IntegerField(verbose_name='Objective player score', blank=True, null=True)
    penta_kills = models.IntegerField(verbose_name='Penta kills', blank=True, null=True)
    physical_damage_dealt_player = models.IntegerField(verbose_name='Physical damage dealt player', blank=True, null=True)
    physical_damage_dealt_to_champions = models.IntegerField(verbose_name='Physical damage dealt to champions', blank=True, null=True)
    physical_damage_taken = models.IntegerField(verbose_name='Physical damage taken', blank=True, null=True)
    quadra_kills = models.IntegerField(verbose_name='Quadra kills', blank=True, null=True)
    sight_wards_bought = models.IntegerField(verbose_name='Sight wards bought', blank=True, null=True)
    spell1_cast = models.IntegerField(verbose_name='Number of times first champion spell was cast', blank=True, null=True)
    spell2_cast = models.IntegerField(verbose_name='Number of times second champion spell was cast', blank=True, null=True)
    spell3_cast = models.IntegerField(verbose_name='Number of times third champion spell was cast', blank=True, null=True)
    spell4_cast = models.IntegerField(verbose_name='Number of times fourth champion spell was cast', blank=True, null=True)
    summon_spell1_cast = models.IntegerField(verbose_name='Number of times first summoner spell was cast', blank=True, null=True)
    summon_spell2_cast = models.IntegerField(verbose_name='Number of times second summoner spell was cast', blank=True, null=True)
    super_monster_killed = models.IntegerField(verbose_name='Super monster killed', blank=True, null=True)
    team = models.IntegerField(verbose_name='Team ID', blank=True, null=True)
    team_objective = models.IntegerField(verbose_name='Team objective', blank=True, null=True)
    time_played = models.IntegerField(verbose_name='Time played', blank=True, null=True)
    total_damage_dealt = models.IntegerField(verbose_name='Total damage dealt', blank=True, null=True)
    total_damage_dealt_to_champions = models.IntegerField(verbose_name='Total damage dealt to champions', blank=True, null=True)
    total_damage_taken = models.IntegerField(verbose_name='Total damage taken', blank=True, null=True)
    total_heal = models.IntegerField(verbose_name='Total heal', blank=True, null=True)
    total_player_score = models.IntegerField(verbose_name='Total player score', blank=True, null=True)
    total_score_rank = models.IntegerField(verbose_name='Total score rank', blank=True, null=True)
    total_time_crowd_control_dealt = models.IntegerField(verbose_name='Total time crowd control dealt', blank=True, null=True)
    total_units_healed = models.IntegerField(verbose_name='Total units healed', blank=True, null=True)
    triple_kills = models.IntegerField(verbose_name='Triple kills', blank=True, null=True)
    true_damage_dealt_player = models.IntegerField(verbose_name='True damage dealt player', blank=True, null=True)
    true_damage_dealt_to_champions = models.IntegerField(verbose_name='True damage dealt to champions', blank=True, null=True)
    true_damage_taken = models.IntegerField(verbose_name='True damage taken', blank=True, null=True)
    turrets_killed = models.IntegerField(verbose_name='Turrets killed', blank=True, null=True)
    unreal_kills = models.IntegerField(verbose_name='Unreal kills', blank=True, null=True)
    victory_point_total = models.IntegerField(verbose_name='Victory point total', blank=True, null=True)
    vision_wards_bought = models.IntegerField(verbose_name='Vision wards bought', blank=True, null=True)
    ward_killed = models.IntegerField(verbose_name='Wards killed', blank=True, null=True)
    ward_placed = models.IntegerField(verbose_name='Wards placed', blank=True, null=True)
    win = models.NullBooleanField(verbose_name='Win')

    class Meta:
        verbose_name = 'Stats'
        verbose_name_plural = 'Stats'
        ordering = ['-pk']