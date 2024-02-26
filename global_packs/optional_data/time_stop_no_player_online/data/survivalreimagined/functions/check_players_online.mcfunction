execute if entity @a run gamerule doDaylightCycle true
execute if entity @a run gamerule doDaylightCycle_tc true
execute unless entity @a run gamerule doDaylightCycle false
execute unless entity @a run gamerule doDaylightCycle_tc false
schedule function survivalreimagined:check_players_online 1s