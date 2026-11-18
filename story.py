import random
from classes import *


# The weapon each class finds at the end of chapters 1, 2, 3, 4,
# and the last one is in the secret vault (if you helped Tobin).
weapon_rewards = {
    "Warrior": [Katana, Iron_Sword, Steel_Sword, Greatsword, Worldsplitter],
    "Mage": [Gnarled_Branch, Apprentice_Staff, Staff_of_Embers, Staff_of_the_Archmage, None],
    "Assassin": [Rusty_Dagger, Iron_Dagger, Steel_Dagger, Shadowfang, Venomfang],
    "Archer": [short_bow, short_crossbow, long_bow, short_draconic_shortbow, long_draconic_shortbow],
}


#Helper Functions

def pick(question, options):
    # Shows a numbered list and returns the number the player picks (1, 2, 3...)
    print()
    print(question)
    for i in range(len(options)):
        print(f"  {i + 1}) {options[i]}")
    while True:
        answer = input("> ")
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)
        print("Type one of the numbers.")


def pause():
    input("\n(Press Enter to continue)")


def title(text):
    print()
    print("=" * 50)
    print(text)
    print("=" * 50)


def total_defense(player):
    total = 0
    for piece in [player.helmet, player.chestplate, player.leggings, player.boots]:
        if piece is not None:
            total += piece.defense
    return total


def equip_weapon(player, weapon):
    # In classes.py the player IS its weapon, so we copy the new weapon's stats onto the player
    player.name = weapon.name
    player.damage = weapon.damage
    player.type = weapon.type
    player.hit_amount = weapon.hit_amount
    player.cost_mana = weapon.cost_mana
    player.mana_cost = weapon.mana_cost
    print(f"You found a {weapon.name}! ({weapon.damage} damage x{weapon.hit_amount})")


def equip_armor(player, armor):
    if armor.type == "helmet":
        player.helmet = armor
    elif armor.type == "chestplate":
        player.chestplate = armor
    elif armor.type == "leggings":
        player.leggings = armor
    elif armor.type == "boots":
        player.boots = armor
    print(f"You put on the {armor.name}. (Total defense: {total_defense(player)})")


def weapon_reward(player, number):
    weapon_class = weapon_rewards[player.class_name][number]
    if weapon_class is None:
        return False
    equip_weapon(player, weapon_class())
    return True


def give_gold(player, coins):
    gold = coins * Gold_Coin().value
    player.gold += gold
    print(f"You found {coins} gold coins! (+{gold} gold, you have {player.gold})")


def show_stats(player):
    print(f"\n{player.hero_name} the {player.class_name}")
    print(f"  Health: {player.health}/{player.max_health}")
    if player.mana_cost > 0:
        print(f"  Mana: {int(player.mana)}/{int(player.max_mana)}")
    print(f"  Weapon: {player.name} ({player.damage} damage x{player.hit_amount})")
    print(f"  Defense: {total_defense(player)}   Dodge: {player.dodge}%")
    print(f"  Potions: {player.potions} health, {player.mana_potions} mana   Gold: {player.gold}")


def rest(player):
    player.health = player.max_health
    player.mana = player.max_mana
    print("You make camp and rest. Your health and mana are back to full.")
    show_stats(player)


def hurt(player, amount):
    # Damage from traps. It can't kill you, only leave you with 1 health.
    player.health -= amount
    if player.health < 1:
        player.health = 1
    print(f"(-{amount} health, {player.health}/{player.max_health} left)")


def check(stat_name, chance):
    # A dice roll. chance is out of 100.
    print(f"({stat_name} check: {chance}% chance)")
    return random.randint(1, 100) <= chance


def shop(player, shopkeeper):
    price = health_potion().value
    while True:
        choice = pick(f"{shopkeeper}: 'What would you like?' (You have {player.gold} gold)",
                      [f"Health potion - {price} gold", f"Mana potion - {price} gold", "Leave"])
        if choice == 3:
            break
        if player.gold < price:
            print("You don't have enough gold.")
            continue
        player.gold -= price
        if choice == 1:
            player.potions += 1
            print("You bought a health potion.")
        else:
            player.mana_potions += 1
            print("You bought a mana potion.")


#Combat

def player_turn(player, enemy, enemy_name):
    print(f"\nYour health: {player.health}/{player.max_health}   {enemy_name}'s health: {enemy.health}")
    if player.mana_cost > 0:
        print(f"Your mana: {int(player.mana)}/{int(player.max_mana)}")

    choice = pick("What do you do?", [f"Attack with your {player.name}",
                                      f"Drink a health potion ({player.potions} left)",
                                      f"Drink a mana potion ({player.mana_potions} left)"])

    if choice == 2:
        if player.potions > 0:
            player.potions -= 1
            player.health = min(player.health + 40, player.max_health)
            print(f"You drink a health potion. Health: {player.health}/{player.max_health}")
            return
        print("You don't have any health potions! You attack instead.")

    if choice == 3:
        if player.mana_potions > 0:
            player.mana_potions -= 1
            player.mana = min(player.mana + 50, player.max_mana)
            print(f"You drink a mana potion. Mana: {int(player.mana)}/{int(player.max_mana)}")
            return
        print("You don't have any mana potions! You attack instead.")

    damage = player.damage
    if player.mana_cost > 0:
        if player.mana >= player.mana_cost:
            player.mana -= player.mana_cost
        else:
            print("You don't have enough mana! You whack it with your staff instead.")
            damage = 3

    for hit in range(player.hit_amount):
        if random.randint(1, 100) <= enemy.dodge:
            print(f"The {enemy_name} dodges!")
        else:
            enemy.health -= damage
            print(f"You hit the {enemy_name} for {damage} damage.")
    if enemy.health < 0:
        enemy.health = 0


def enemy_turn(player, enemy, enemy_name):
    if random.randint(1, 100) <= player.dodge:
        print(f"The {enemy_name} attacks, but you dodge it!")
        return

    # Every 10 defense blocks 1 damage
    damage = enemy.damage - total_defense(player) // 10
    if damage < 1:
        damage = 1
    player.health -= damage
    if player.health < 0:
        player.health = 0
    weapon = enemy.name.replace("_", " ")
    print(f"The {enemy_name} hits you with its {weapon} for {damage} damage.")


def fight(player, enemy, enemy_name):
    # Returns True if you win, False if you lose
    print(f"\n--- {enemy_name} attacks! ---")
    print(enemy.description)

    # Bows always shoot first. Otherwise whoever is faster goes first.
    if player.type == "bow" or player.type == "crossbow" or player.speed >= enemy.speed:
        players_turn = True
    else:
        players_turn = False

    while player.health > 0 and enemy.health > 0:
        if players_turn:
            player_turn(player, enemy, enemy_name)
        else:
            enemy_turn(player, enemy, enemy_name)
        players_turn = not players_turn

    if player.health <= 0:
        print("\nYou have been defeated...")
        return False
    print(f"\nYou defeated the {enemy_name}!")
    return True


#Start Of The Game

def create_player():
    choice = pick("Choose your class:", ["Warrior - " + Warrior().description,
                                         "Mage - " + Mage().description,
                                         "Assassin - " + Assassin().description,
                                         "Archer - " + Archer().description])
    if choice == 1:
        player = Warrior()
        player.class_name = "Warrior"
    elif choice == 2:
        player = Mage()
        player.class_name = "Mage"
    elif choice == 3:
        player = Assassin()
        player.class_name = "Assassin"
    else:
        player = Archer()
        player.class_name = "Archer"

    player.hero_name = input("\nWhat is your name? ")
    if player.hero_name == "":
        player.hero_name = "Hero"

    # Extra things the story keeps track of
    player.max_health = player.health
    player.max_mana = player.mana
    player.gold = 0
    player.potions = 2
    player.mana_potions = 0
    if player.class_name == "Mage":
        player.mana_potions = 2
    player.helmet = None
    player.chestplate = Leather_Chestplate()
    player.leggings = None
    player.boots = None
    player.helped_tobin = False
    player.spared_rook = False
    return player


def prologue(player):
    title("Prologue: Fire in the Night")
    print("The valley of Eldmoor has been quiet for a hundred years.")
    print("Then, three nights ago, the sky above Ashen Peak turned red.")
    print(f"\nYou are {player.hero_name}, a {player.class_name} from the village of Emberwick.")
    print("Last night fire fell on the eastern fields. The farmers swear they saw wings as wide as a barn.")
    print("\nAt dawn, Elder Maren calls you to her house.")
    print("'Vharzul is awake,' she says. 'The old dragon under Ashen Peak. It won't stop at a few fields.'")
    print("'The king's soldiers are weeks away. Someone has to climb that mountain. I'm asking you.'")
    print("\nShe gives you 2 health potions and an old Leather Chestplate.")
    print("'Go through the Mirefen, then take the Kingsroad east. And come back alive.'")
    show_stats(player)
    pause()


#Chapters (each one returns True if you survive, False if you die)

def chapter_1(player):
    title("Chapter 1: The Mirefen")
    print("The Mirefen starts where the farmland ends: black trees, grey water and mud that pulls at your boots.")
    print("An old road winds through it. A line of reeds cuts straight across the bog.")

    path = pick("Which way do you go?", ["Stay on the old road", "Cut through the bog"])
    if path == 1:
        print("\nYou keep to the road. It's quiet. Too quiet.")
        print("A goblin drops from the branches above you, grinning with far too many teeth.")
        enemy = goblin()
        enemy.health = 40
        if not fight(player, enemy, "Goblin"):
            return False
    else:
        print("\nHalfway across the bog, the water in front of you bulges, wobbles... and stands up.")
        enemy = slime()
        enemy.health = 30
        if not fight(player, enemy, "Slime"):
            return False
        print("\nThe slime splits in two! The smaller half comes at you.")
        enemy = slime()
        enemy.health = 15
        if not fight(player, enemy, "Small Slime"):
            return False

    print("\nAt the edge of the Mirefen is a goblin camp. One goblin was left on guard, and it has seen you.")
    enemy = goblin()
    enemy.health = 40
    if not fight(player, enemy, "Goblin"):
        return False

    print()
    if path == 1:
        print("The goblin from the road dropped a pouch and a potion it stole.")
        give_gold(player, 3)
        player.potions += 1
        print("You found a health potion!")
    else:
        print("Where the slimes were, the corner of an old treasure chest pokes out of the mud.")
        give_gold(player, 8)
    print("\nThe goblin camp is full of junk stolen from farms around Emberwick. Some of it is useful.")
    weapon_reward(player, 0)
    equip_armor(player, Leather_Helmet())
    equip_armor(player, Leather_Boots())
    pause()
    return True


def chapter_2(player):
    title("Chapter 2: The Kingsroad")
    rest(player)
    print("\nPast the Mirefen, the Kingsroad runs straight toward the hills.")
    print("Around midday you hear shouting. A merchant's wagon lies on its side in a ditch.")
    print("A round man in a green coat is backing away from a bandit with a sword,")
    print("while another bandit aims a bow at him from the ridge above.")
    print("'Please! It's just pots and blankets!' the merchant cries.")

    rook = bandit()
    rook.health = 70
    rook.damage = 8

    choice = pick("What do you do?", ["Help the merchant", "Sneak past while they're busy"])
    if choice == 1:
        print("\nYou shout and charge. The archer on the ridge turns on you first.")
        enemy = ranged_bandit()
        enemy.health = 50
        if not fight(player, enemy, "Ranged Bandit"):
            return False
        print("\nThe swordsman shoves the merchant aside. 'You'll pay for that.' He must be their captain.")
        if not fight(player, rook, "Bandit Captain"):
            return False
        player.helped_tobin = True
        print("\nThe merchant dusts himself off. 'Tobin's the name. You saved my life, and my pots!'")
        print("'Take this potion. And this old map. It marks a vault somewhere in Ironjaw Pass.'")
        player.potions += 1
        print("You got a health potion and Tobin's Map!")
    else:
        if check("Speed", player.speed * 8):
            print("\nYou slip through the tall grass. Behind you the merchant's cries fade away.")
            print("A mile later you find the bandits' camp. Only their captain is there, counting coins.")
            if not fight(player, rook, "Bandit Captain"):
                return False
        else:
            print("\nA branch cracks under your boot. The archer spins around. 'Got another one!'")
            enemy = ranged_bandit()
            enemy.health = 50
            if not fight(player, enemy, "Ranged Bandit"):
                return False
            print("\nWhile you fought, the merchant ran away. The bandit captain steps out from behind the wagon.")
            if not fight(player, rook, "Bandit Captain"):
                return False

    print("\nThe captain lies in the dirt. 'Wait, mercy! My name's Rook. I'll tell you something useful!'")
    choice = pick("What do you do?", ["Spare him", "Finish him"])
    if choice == 1:
        player.spared_rook = True
        print("\n'There's a pale man,' Rook says. 'Pays us to carry crates of bones to the Hollow Crypt.")
        print("Says he's going to own the dragon. Watch out in the crypt: only step on the stones with skulls on them.'")
        print("He limps away into the hills.")
    else:
        print("\nYou finish him. In his coat you find a note: 'Bring the last crates to the Hollow Crypt.")
        print("Soon the dragon will answer to me. - S.'")
        give_gold(player, 4)

    print("\nIn the bandits' stash you find something useful.")
    weapon_reward(player, 1)
    equip_armor(player, Iron_Chestplate())
    equip_armor(player, Iron_Leggings())

    print("\nBy evening you reach the Wayfarer's Rest, an inn at the crossroads.")
    shop(player, "The innkeeper")
    pause()
    return True


def chapter_3(player):
    title("Chapter 3: The Hollow Crypt")
    rest(player)
    print("\nThe Hollow Crypt sits inside a ring of dead oaks. Cold air breathes out of the open doors.")
    print("You go down the steps. Some of the floor stones have little skulls carved into them.")

    if player.spared_rook:
        print("\nYou remember Rook's warning and only step on the skull stones.")
        print("Darts shoot out of the walls behind you and hit nothing.")
    else:
        print("\nClick. The stone under your foot sinks. Darts shoot out of the walls!")
        if check("Dodge", 50 + int(player.dodge * 10)):
            print("You throw yourself flat and the darts fly over you.")
        else:
            print("Two darts hit you in the shoulder.")
            hurt(player, 10)

    print("\nSomething in a rusty helmet shambles out of the dark: a skeleton, still wearing a bandit's coat.")
    enemy = bandit()
    enemy.health = 50
    enemy.description = "The bones of a dead bandit, held together by dark magic."
    if not fight(player, enemy, "Skeleton"):
        return False

    print("\nAt the bottom of the stairs is a stone door covered in glowing runes. It won't open.")
    choice = pick("How do you get through?", ["Read the runes (Intelligence)", "Force it open (Strength)"])
    if choice == 1:
        if check("Intelligence", player.intelligence * 8):
            print("You trace the runes in the right order and the door grinds open.")
        else:
            print("You get the order wrong. The runes burn your hands before the door creaks open.")
            hurt(player, 10)
    else:
        if check("Strength", player.strength * 6):
            print("You put your shoulder into the door and push. It opens.")
        else:
            print("The runes flash as you push, and something in your back goes pop before the door opens.")
            hurt(player, 10)

    print("\nA pale man in black robes stands over an altar of bones.")
    print("'Another hero,' he sighs. 'You're too late. I woke Vharzul myself.")
    print("When the dragon has burned your village, it will answer to me. To Sereth.'")
    sereth = necromancer()
    sereth.damage = 12
    if not fight(player, sereth, "Necromancer"):
        return False

    print("\nSereth crumbles to dust and leaves a journal on the altar. You read the last page:")
    print("'The chain-rune holds the dragon's will. Break the rune and the beast goes free.'")
    print("\nBehind the altar, Sereth kept the belongings of the heroes who came before you.")
    weapon_reward(player, 2)
    equip_armor(player, Steel_Helmet())
    equip_armor(player, Steel_Boots())
    pause()
    return True


def chapter_4(player):
    title("Chapter 4: Ironjaw Pass")
    rest(player)
    print("\nThe road climbs into the mountains. An orc in a wolf-skin hood steps out from behind a rock.")
    print("'Boss says nobody gets to the bridge,' it growls.")
    enemy = orc()
    enemy.health = 60
    if not fight(player, enemy, "Orc Scout"):
        return False

    print("\nPast the scout is a narrow stone bridge over a gorge so deep you can't see the bottom.")
    print("On the other side stands an orc twice your size with an axe on his shoulder.")
    print("'Grukk Ironjaw guards this pass,' he rumbles. 'Nobody crosses. Not you. Not the dragon. Nobody.'")
    grukk = orc()
    grukk.health = 150
    grukk.damage = 14

    choice = pick("What do you do?", ["Walk across and fight him", "Climb around the cliff and ambush him"])
    if choice == 2:
        if check("Speed", player.speed * 7):
            print("You sneak up behind him and hit him before he can turn around! (-40 health)")
            grukk.health -= 40
        else:
            print("A rock breaks under your hand and you slam into the cliff. Grukk laughs. 'Not sneaky enough.'")
            hurt(player, 10)
    if not fight(player, grukk, "Orc Warlord"):
        return False

    print("\nGrukk drops to one knee. 'Strong,' he grunts. 'Maybe strong enough for the dragon.'")
    print("His cave is piled high with things he took from travelers.")
    weapon_reward(player, 3)
    equip_armor(player, Mithril_Chestplate())

    if player.helped_tobin:
        print("\nYou open Tobin's map. The vault is right here, behind a crack in the cliff!")
        print("Inside, it hasn't been touched for hundreds of years.")
        if not weapon_reward(player, 4):
            player.mana_potions += 2
            print("You found 2 mana potions!")
        equip_armor(player, Dragon_Helmet())
    pause()
    return True


def chapter_5(player):
    title("Chapter 5: Ashen Peak")
    rest(player)
    print("\nThe last climb is through ash and smoke. Near the top, an old woman keeps a shrine.")
    print("'Going up? Then you'll want supplies.'")
    shop(player, "The shrine keeper")

    print("\nAt the top, the mountain opens into a crater full of fire. Curled around the lava is Vharzul.")
    print("The dragon's eyes open. On its chest a black rune glows like a chain: the chain-rune from Sereth's journal.")
    print("'ANOTHER ONE,' it roars. 'COME TO DIE LIKE THE OTHERS?'")

    vharzul = dragon()
    vharzul.health = 250
    vharzul.damage = 18

    choice = pick("What do you do?", ["Fight the dragon", "Try to break the chain-rune (Intelligence)"])
    if choice == 2:
        if check("Intelligence", player.intelligence * 8):
            dragonfriend_ending(player)
            return True
        print("The rune burns you like fire. Vharzul screams and knocks you across the crater.")
        hurt(player, 15)
        print("'TRICKS!' the dragon roars. There's no talking now.")

    if not fight(player, vharzul, "Dragon"):
        return False
    dragonslayer_ending(player)
    return True


#Endings

def dragonfriend_ending(player):
    print("\nThe rune cracks like ice. The black chain melts away and the anger leaves Vharzul's eyes.")
    print("'A HUNDRED YEARS I SLEPT,' the dragon rumbles, 'AND THE PALE ONE WOKE ME IN CHAINS.")
    print("YOU HAVE SET ME FREE. EMBERWICK WILL NOT BURN.'")
    print("Vharzul spreads its wings and flies west, to sleep somewhere far away.")
    title("THE DRAGONFRIEND ENDING")
    epilogue(player)


def dragonslayer_ending(player):
    print("\nVharzul crashes into the lava with a sound like the mountain breaking in half.")
    print("You carry one of its teeth back down the mountain.")
    print("When Emberwick sees you coming, they ring every bell in the village.")
    title("THE DRAGONSLAYER ENDING")
    epilogue(player)


def epilogue(player):
    print(f"Elder Maren names {player.hero_name} the protector of Emberwick.")
    if player.helped_tobin:
        print("Tobin opens a shop in the village and gives you a discount for life. Ten percent. He's still Tobin.")
    if player.spared_rook:
        print("Months later, Rook joins the village guard. He nods at you. He doesn't have to say thank you.")
    else:
        print("With Rook gone, the Kingsroad is safe again.")
    show_stats(player)


#Main Game

def play_chapter(chapter, player):
    # If you die, you can try the chapter again.
    # Your potions and gold go back to what you had when the chapter started.
    potions = player.potions
    mana_potions = player.mana_potions
    gold = player.gold
    while True:
        if chapter(player):
            return True
        choice = pick("You have fallen. What now?", ["Try the chapter again", "Quit"])
        if choice == 2:
            return False
        player.health = player.max_health
        player.mana = player.max_mana
        player.potions = potions
        player.mana_potions = mana_potions
        player.gold = gold


def main():
    print("=" * 50)
    print("              EMBERS OF ELDMOOR")
    print("=" * 50)
    player = create_player()
    prologue(player)

    chapters = [chapter_1, chapter_2, chapter_3, chapter_4, chapter_5]
    for chapter in chapters:
        if not play_chapter(chapter, player):
            print("\nThanks for playing!")
            return
    print("\nTHE END - Thanks for playing!")


if __name__ == "__main__":
    main()
