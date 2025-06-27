worldborder add 1 150
execute store result score WORLD_BORDER wb_setup run worldborder get
scoreboard players set @a wb_deaths 0

schedule function worldborder:expand 150s