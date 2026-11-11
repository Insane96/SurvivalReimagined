* advancements
    * flint, copper, coal, furnace
    * wooden pickaxe advancement
* Vanilla Backport: unwaxed `minecraft:lightning_rod` doesn't attract lightning (ServerLevelMixin replaces findLightningRod and only checks its `minecraft:lightning_rods` POI, which lacks the base rod). Check on updates, remove the changelog known issue and the second text of the `vanillabackport_lightning_rod` EMI page when fixed
