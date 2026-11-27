# Phase 5: Supplementaries (4.1.4). Sources: the decompiled jar (RedMerchantEntity, RedMerchantSpawnerMixin,
# EvokerRedMerchantWololooSpellGoal added to every Evoker in ServerEvents, PlundererEntity), the pack's Red Merchant
# trade overrides and config/supplementaries-common.toml (galleon off, naval_raid_chance 0.75).
# The Red Merchant only rolls when the Wandering Trader's spawn attempt fails, with a chance that grows with the
# area's local difficulty, the world difficulty and a killed Ender Dragon.

S = "supplementaries"
PAGES = {
    (S, "red_merchant"): (["Sometimes comes when the Wandering Trader doesn't, more often in places you've spent a long time in, on harder difficulties and once the Ender Dragon is dead. Evokers can also turn a Wandering Trader into one. It sells explosives, Cannons and Rope, throws Bombs at Zombies and raiders, and leaves after a while."], []),
    (S, "plunderer"): (["Comes with raids on villages near water, steering the Pillagers' boats in from the sea. It fights with a Golden Sword, fires Cannons it finds nearby, sometimes carries a Parrot on its shoulder and slowly heals over time."], []),
}
