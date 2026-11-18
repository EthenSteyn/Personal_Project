class Classes:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Stats:
    def __init__(self, health, strength, intelligence, speed, endurance, mana=0, dodge=0):
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed
        self.endurance = endurance
        self.mana = mana
        self.dodge = dodge

class Weapons:
    def __init__(self, name, damage, weapon_type, cost_mana = False, mana_cost = 0, hit_amount = 1, rarity = "common"):
        self.name = name # Name is the name of the weapon, such as "Sword" or "Bow".
        self.damage = damage  # Damage is the amount of damage the weapon can inflict on an enemy. It is a numerical value that represents the weapon's offensive power.
        self.type = weapon_type # Weapon type is the category of the weapon, such as "sword" or "bow".
        self.cost_mana = cost_mana # Cost_mana is a boolean value that indicates whether the weapon requires mana to use. If cost_mana is True, then the weapon requires mana to use. If cost_mana is False, then the weapon does not require mana to use.
        self.mana_cost = mana_cost # Mana cost is the amount of mana required to use the weapon.
        self.hit_amount = hit_amount # Hit amount is the number of times the weapon can hit in one attack. For example, a dagger can hit twice in one attack, while a sword can only hit once.
        self.rarity = rarity # Rarity is how rare the weapon is, such as "common" or "legendary".

#Character Classes
class  Warrior(Classes, Stats, Weapons):
        def __init__(self):
            super().__init__("Warrior", "A fierce combatant who excels in melee combat.")
            Stats.__init__(self, health=100, strength=15, intelligence=4, speed=6, endurance=8, dodge= 6 * 0.25)
            Weapons.__init__(self, name="Starter_Sword", damage=12, hit_amount=1, weapon_type="two-handed sword")

class Mage(Classes, Stats, Weapons):
        def __init__(self):
            super().__init__("Mage", "A master of arcane arts who wields powerful spells.")
            Stats.__init__(self, health=100, strength=3, intelligence=10, speed=6, endurance=4, mana= 10 * 15 * 1.05, dodge= 6 * 0.25)
            Weapons.__init__(self, name="Starter_Staff", damage=8, hit_amount=1, weapon_type="staff", cost_mana=True, mana_cost=5)

class Assassin(Classes, Stats, Weapons):
        def __init__(self):
            super().__init__("Assassin", "A stealthy and agile fighter who strikes from the shadows.")
            Stats.__init__(self, health=100, strength=6, intelligence=5, speed=9, endurance=5, dodge= 9 * 0.25)
            Weapons.__init__(self, name="Starter_Dagger", damage=7, hit_amount=2, weapon_type="dagger")

class Archer(Classes, Stats, Weapons):
        def __init__(self):
            super().__init__("Archer", "A skilled marksman who excels at ranged combat.")
            Stats.__init__(self, health=100, strength=5, intelligence=6, speed=8, endurance=5, dodge= 8 * 0.25)
            Weapons.__init__(self, name="Starter_Bow", damage=10, hit_amount=1, weapon_type="bow")


#Enemy Classes
class Enemy(Classes, Stats, Weapons):
        def __init__(self, name, description, strength, intelligence, speed, endurance, weapon_name, weapon_damage, weapon_type):
            super().__init__(name, description)
            Stats.__init__(self, health=100, strength=strength, intelligence=intelligence, speed=speed, endurance=endurance)
            Weapons.__init__(self, name=weapon_name, damage=weapon_damage, hit_amount=1, weapon_type=weapon_type)

class goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", "A small, green creature that is quick and cunning.", strength=4, intelligence=3, speed=7, endurance=5, weapon_name="Rusty_Dagger", weapon_damage=5, weapon_type="dagger")

class slime(Enemy):
    def __init__(self):
        super().__init__("Slime", "A gelatinous creature that can split into smaller slimes.", strength=3, intelligence=2, speed=4, endurance=6, weapon_name="Acid_Spit", weapon_damage=4, weapon_type="acid")

class orc(Enemy):
    def __init__(self):
        super().__init__("Orc", "A brutish and aggressive creature that excels in close combat.", strength=8, intelligence=4, speed=5, endurance=7, weapon_name="Battle_Axe", weapon_damage=10, weapon_type="axe")

class dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", "A legendary creature that breathes fire and has impenetrable scales.", strength=10, intelligence=8, speed=7, endurance=10, weapon_name="Fire_Breath", weapon_damage=15, weapon_type="fire")

class bandit(Enemy):
    def __init__(self):
        super().__init__("Bandit", "A rogue who preys on travelers and caravans.", strength=5, intelligence=4, speed=6, endurance=5, weapon_name="Short_Sword", weapon_damage=6, weapon_type="sword")

class ranged_bandit(Enemy):
    def __init__(self):
        super().__init__("Ranged Bandit", "A rogue who attacks from a distance with a bow.", strength=4, intelligence=5, speed=7, endurance=4, weapon_name="Short_Bow", weapon_damage=5, weapon_type="bow")

class necromancer(Enemy):
    def __init__(self):
        super().__init__("Necromancer", "A dark mage who raises the dead to do their bidding.", strength=3, intelligence=9, speed=5, endurance=4, weapon_name="Dark_Staff", weapon_damage=8, weapon_type="staff")


#Loot Classes
class Loot:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

class health_potion(Loot):
    def __init__(self):
        super().__init__("Health Potion", "A potion that restores health when consumed.", value=50)

class mana_potion(Loot):
    def __init__(self):
        super().__init__("Mana Potion", "A potion that restores mana when consumed.", value=50)

class Gold_Coin(Loot):
    def __init__(self):
        super().__init__("Gold Coin", "A shiny coin that can be used to purchase items.", value=10)

class treasure_chest(Loot):
    def __init__(self):
        super().__init__("Treasure Chest", "A chest that contains valuable items.", value=15)

# Swords
class Iron_Sword(Weapons):
    def __init__(self):
        super().__init__("Iron Sword", damage=24, hit_amount=1, weapon_type="sword", rarity="uncommon")

class Steel_Sword(Weapons):
    def __init__(self):
        super().__init__("Steel Sword", damage=30, hit_amount=1, weapon_type="sword", rarity="rare")

class Greatsword(Weapons):
    def __init__(self):
        super().__init__("Greatsword", damage=60, hit_amount=1, weapon_type="two-handed sword", rarity="epic")

class Katana(Weapons):
    def __init__(self):
        super().__init__("Katana", damage=18, hit_amount=1, weapon_type="sword", rarity="rare")

class Worldsplitter(Weapons):
    def __init__(self):
        super().__init__("Worldsplitter", damage=80, hit_amount=2, weapon_type="two-handed sword", rarity="legendary")

# Staffs
class Gnarled_Branch(Weapons):
    def __init__(self):
        super().__init__("Gnarled Branch", damage=15, hit_amount=1, weapon_type="staff", rarity="common", cost_mana=True, mana_cost=15)

class Apprentice_Staff(Weapons):
    def __init__(self):
        super().__init__("Apprentice Staff", damage=22, hit_amount=1, weapon_type="staff", rarity="uncommon", cost_mana=True, mana_cost=20)

class Staff_of_Embers(Weapons):
    def __init__(self):
        super().__init__("Staff of Embers", damage=30, hit_amount=1, weapon_type="staff", rarity="rare", cost_mana=True, mana_cost=22)

class Staff_of_the_Archmage(Weapons):
    def __init__(self):
        super().__init__("Staff of the Archmage", damage=40, hit_amount=1, weapon_type="staff", rarity="legendary", cost_mana=True, mana_cost=30)

# Daggers
class Rusty_Dagger(Weapons):
    def __init__(self):
        super().__init__("Rusty Dagger", damage=10, hit_amount=2, weapon_type="dagger", rarity="common")

class Iron_Dagger(Weapons):
    def __init__(self):
        super().__init__("Iron Dagger", damage=12, hit_amount=2, weapon_type="dagger", rarity="uncommon")

class Steel_Dagger(Weapons):
    def __init__(self):
        super().__init__("Steel Dagger", damage=15, hit_amount=3, weapon_type="dagger", rarity="rare")

class Shadowfang(Weapons):
    def __init__(self):
        super().__init__("Shadowfang", damage=20, hit_amount=4, weapon_type="dagger", rarity="epic")

class Venomfang(Weapons):
    def __init__(self):
        super().__init__("Venomfang", damage=25, hit_amount=4, weapon_type="dagger", rarity="legendary")

# Bows
class short_bow(Weapons):
    def __init__(self):
        super().__init__("Short Bow", damage=10, hit_amount=1, weapon_type="bow", rarity="common")

class short_crossbow(Weapons):
    def __init__(self):
        super().__init__("Short Crossbow", damage=12, hit_amount=2, weapon_type="crossbow", rarity="uncommon")

class long_bow(Weapons):
    def __init__(self):
        super().__init__("Long Bow", damage=26, hit_amount=1, weapon_type="bow", rarity="rare")

class short_draconic_shortbow(Weapons):
    def __init__(self):
        super().__init__("Short Draconic Shortbow", damage=15, hit_amount=3, weapon_type="bow", rarity="epic")

class long_draconic_shortbow(Weapons):
    def __init__(self):
        super().__init__("Long Draconic Shortbow", damage=20, hit_amount=4, weapon_type="bow", rarity="legendary")


#Armor Classes

class Armor:
    def __init__(self, name, defense, armor_type, rarity="common"):
        self.name = name
        self.defense = defense
        self.type = armor_type
        self.rarity = rarity

# Helmet Classes
class Leather_Helmet(Armor):
    def __init__(self):
        super().__init__("Leather Helmet", defense=5, armor_type="helmet", rarity="common")

class Iron_Helmet(Armor):
    def __init__(self):
        super().__init__("Iron Helmet", defense=10, armor_type="helmet", rarity="uncommon")

class Steel_Helmet(Armor):
    def __init__(self):
        super().__init__("Steel Helmet", defense=15, armor_type="helmet", rarity="rare")

class Mithril_Helmet(Armor):
    def __init__(self):
        super().__init__("Mithril Helmet", defense=20, armor_type="helmet", rarity="epic")

class Dragon_Helmet(Armor):
    def __init__(self):
        super().__init__("Dragon Helmet", defense=25, armor_type="helmet", rarity="legendary")

# Chestplate Classes

class Leather_Chestplate(Armor):
    def __init__(self):
        super().__init__("Leather Chestplate", defense=10, armor_type="chestplate", rarity="common")

class Iron_Chestplate(Armor):
    def __init__(self):
        super().__init__("Iron Chestplate", defense=20, armor_type="chestplate", rarity="uncommon")

class Steel_Chestplate(Armor):
    def __init__(self):
        super().__init__("Steel Chestplate", defense=30, armor_type="chestplate", rarity="rare")

class Mithril_Chestplate(Armor):
    def __init__(self):
        super().__init__("Mithril Chestplate", defense=40, armor_type="chestplate", rarity="epic")

class Dragon_Chestplate(Armor):
    def __init__(self):
        super().__init__("Dragon Chestplate", defense=50, armor_type="chestplate", rarity="legendary")

# Leggings Classes

class Leather_Leggings(Armor):
    def __init__(self):
        super().__init__("Leather Leggings", defense=8, armor_type="leggings", rarity="common")

class Iron_Leggings(Armor):
    def __init__(self):
        super().__init__("Iron Leggings", defense=16, armor_type="leggings", rarity="uncommon")

class Steel_Leggings(Armor):
    def __init__(self):
        super().__init__("Steel Leggings", defense=24, armor_type="leggings", rarity="rare")

class Mithril_Leggings(Armor):
    def __init__(self):
        super().__init__("Mithril Leggings", defense=32, armor_type="leggings", rarity="epic")

class Dragon_Leggings(Armor):
    def __init__(self):
        super().__init__("Dragon Leggings", defense=40, armor_type="leggings", rarity="legendary")


# Boots Classes

class Leather_Boots(Armor):
    def __init__(self):
        super().__init__("Leather Boots", defense=5, armor_type="boots", rarity="common")

class Iron_Boots(Armor):
    def __init__(self):
        super().__init__("Iron Boots", defense=10, armor_type="boots", rarity="uncommon")

class Steel_Boots(Armor):
    def __init__(self):
        super().__init__("Steel Boots", defense=15, armor_type="boots", rarity="rare")

class Mithril_Boots(Armor):
    def __init__(self):
        super().__init__("Mithril Boots", defense=20, armor_type="boots", rarity="epic")

class Dragon_Boots(Armor):
    def __init__(self):
        super().__init__("Dragon Boots", defense=25, armor_type="boots", rarity="legendary")

# Player Class
class Player(Classes, Stats, Weapons, Armor):
    def __init__(self, name, description, health, strength, intelligence, speed, endurance, weapon_name, weapon_damage, weapon_type):
        super().__init__(name, description)
        Stats.__init__(self, health=health, strength=strength, intelligence=intelligence, speed=speed, endurance=endurance)
        Weapons.__init__(self, name=weapon_name, damage=weapon_damage, hit_amount=1, weapon_type=weapon_type)
        Armor.__init__(self, name="Starter_Armor", defense=5, armor_type="armor", rarity="common")
