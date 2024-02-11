worldborder add 2 0
title @a title {"text": "A day has passed"}
title @a subtitle  {"text": "World Border expanded!"}
execute store result score WORLD_BORDER world_border_setup run worldborder get
scoreboard players set @a wb_deaths 0