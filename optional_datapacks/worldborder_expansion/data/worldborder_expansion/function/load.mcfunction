# Scoreboard usato per far partire il setup una sola volta per mondo
scoreboard objectives add wbe_data dummy

# Il primo player potrebbe non essere ancora caricato al momento del load, quindi si aspetta 1 secondo
schedule function worldborder_expansion:setup 20t
