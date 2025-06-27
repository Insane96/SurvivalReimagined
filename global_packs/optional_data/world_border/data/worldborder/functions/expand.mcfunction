execute as @a run worldborder add 2 0
execute store result score WORLD_BORDER wb_setup run worldborder get
scoreboard players set @a wb_deaths 0

schedule function worldborder:expand 300s