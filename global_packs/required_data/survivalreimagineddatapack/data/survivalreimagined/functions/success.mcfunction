# Tell the player the setup is complete
tellraw @a {"text": "Found good spawn, good luck", "color": "#FFD700", "bold": true}
tellraw @a {"text": "Due to a glitch in commands, I recommend to re-join the world/server.", "color": "#FF0000"}
# Setup the world border
function iguanatweaksreborn:setup_worldborder
# Remove the setup objective
scoreboard objectives remove world_border_setup
# Re-enable dayLightCycle
gamerule doDaylightCycle true
gamerule doDaylightCycle_tc true
gamerule doWeatherCycle true
time set 0
# Remove effects
effect clear @a
effect give @a instant_health 10

setblock ~ ~ ~ minecraft:torch

# Gamerules
gamerule spawnRadius 0
gamerule iguanatweaks:doLooseRespawn false
gamerule iguanatweaks:painful_world_border 2
gamerule iguanatweaks:deathGrave false