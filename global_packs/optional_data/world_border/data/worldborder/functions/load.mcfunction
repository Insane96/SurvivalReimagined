scoreboard objectives add wb_deaths deathCount
scoreboard objectives add wb_setup dummy
# scoreboard objectives setdisplay sidebar wb_setup

scoreboard players reset WORLD_BORDER_LOGS wb_setup
scoreboard players reset WORLD_BORDER_GRAVEL wb_setup

# tellraw @a [{"text": "Finding a good spawn. Please stand by."}]
gamerule iguanatweaks:doLooseRespawn false
gamerule iguanatweaks:deathGrave false

schedule function worldborder:try_setup 1s