execute store success score $wbe_gravel wbe_data run place feature ore_gravel ~ ~-20 ~
execute if score $wbe_gravel wbe_data matches 0 store success score $wbe_gravel wbe_data run place feature ore_gravel ~-5 ~-20 ~-5
execute if score $wbe_gravel wbe_data matches 0 store success score $wbe_gravel wbe_data run place feature ore_gravel ~5 ~-20 ~5
execute if score $wbe_gravel wbe_data matches 0 store success score $wbe_gravel wbe_data run place feature ore_gravel ~-5 ~-20 ~5
execute if score $wbe_gravel wbe_data matches 0 store success score $wbe_gravel wbe_data run place feature ore_gravel ~5 ~-20 ~-5

# Gravel placed successfully: finish the setup. Otherwise look for another spot
execute if score $wbe_gravel wbe_data matches 1.. run function worldborder_expansion:finish_setup
execute if score $wbe_gravel wbe_data matches 0 run function worldborder_expansion:spread
