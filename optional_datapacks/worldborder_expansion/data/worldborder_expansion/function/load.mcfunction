# Scoreboard used to only run the setup once per world
scoreboard objectives add wbe_data dummy

# The first player might not be loaded yet at load time, so wait 1 second
schedule function worldborder_expansion:setup 20t
