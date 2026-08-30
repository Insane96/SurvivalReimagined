# Count the logs near the candidate spawn point
execute store result score $wbe_logs wbe_data run clone ~-6 ~-12 ~-6 ~6 ~8 ~6 ~-6 ~-12 ~-6 filtered #logs force
# If there aren't enough, look for another spot
execute if score $wbe_logs wbe_data matches ..6 run function worldborder_expansion:spread
# Otherwise try to generate some gravel nearby
execute if score $wbe_logs wbe_data matches 7.. run function worldborder_expansion:try_placing_gravel
