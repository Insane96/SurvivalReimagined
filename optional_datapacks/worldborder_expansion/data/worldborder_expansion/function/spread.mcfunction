# Temporarily widen the border so a new spot can be searched for
worldborder set 30000000
spreadplayers ~ ~ 8 512 true @a
schedule function worldborder_expansion:find_spawn 10t
