import sys

def setup(core, object):
	
	lootPoolNames_1 = ['Junk']
	lootPoolChances_1 = [100]
	lootGroupChance_1 = 65
	object.addToLootGroups(lootPoolNames_1,lootPoolChances_1,lootGroupChance_1)
	
	lootPoolNames_2 = ['jedi_relic_1']
	lootPoolChances_2 = [100]
	lootGroupChance_2 = 85
	object.addToLootGroups(lootPoolNames_2,lootPoolChances_2,lootGroupChance_2)
	
	lootPoolNames_3 = ['powercrystals_hiq']
	lootPoolChances_3 = [100]
	lootGroupChance_3 = 12
	object.addToLootGroups(lootPoolNames_3,lootPoolChances_3,lootGroupChance_3)
	
	
	
	return 