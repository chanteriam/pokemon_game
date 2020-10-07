# Pokemon types: Psychic, water & fire

class Pokemon:
    def __init__(self, name, poke_type, level=1):
        self.name = name
        self.pokemon_type = poke_type.capitalize()
        self.level = level
        self.max_health = level * 10
        self.health = level * 10
        self.is_KO = False
        self.revivals = level
        self.num_attacks = 0
        self.attack_damage = 2 * level
        self.health_increases = 3
        self.max_health_increase = level
        self.points = 0

    def __repr__(self):
        return """{name} is a level {level} pokémon of type {type}. They currently have {health} hit points.
                """.format(name=self.name, level=self.level, type=self.pokemon_type, health=self.health)

    # method for pokemon gaining health
    def gain_health(self):
        if self.is_KO:
            print("Sorry, you cannot gain health while you are knocked out. Use a revival instead!")
        else:
            if self.health_increases != 0:
                self.health += self.max_health_increase
                if self.health > self.max_health:
                    self.health = self.max_health
                print("{}'s now has {} hit points".format(self.name, self.health))
            else:
                print("{} is out of health increases!".format(self.name))
        print()

    def knock_out(self):
        self.is_KO = True
        print("{} is now knocked out.".format(self.name))

    # method for pokemon losing health
    def lose_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
            self.knock_out()
            print("{} is now knocked out!".format(self.name))
        else:
            print("{} lost some hit points! They now have {} health".format(self.name, self.health))
        print()

    # method for reviving KO'ed poké; revivals limited to level
    def revive(self):
        if self.revivals > 0:
            if self.is_KO:
                self.is_KO = False
                self.health = self.max_health / 2
                self.revivals -= 1
                print("""{} has been revived! You now have {} hit points.
                You have {} revival(s) left""".format(self.name, self.health, self.revivals))
        else:
            print("""{} only had {} revival(s), and they are now out! 
                    To gain revivals, level up!""".format(self.name, self.level))
        print()

    # method for attacking poké
    def attack(self, other_poke):
        # standard damage = 2 * pokemon level
        # for fire types, they do half damage to other fire or water types and full damage to psychic types
        if self.is_KO:
            print("Sorry, you cannot attack when you are knocked out!")
        else:
            if self.pokemon_type == "Fire":
                if (other_poke.pokemon_type == "Fire") or (other_poke.pokemon_type == "Water"):
                    self.attack_damage = self.attack_damage / 2
            # for water types, they do 2x damage to fire types and normal damage to psychic types
            elif self.pokemon_type == "Water":
                if other_poke.pokemon_type == "Fire":
                    self.attack_damage = self.attack_damage * 2
                elif other_poke.pokemon_type == "Water":
                    self.attack_damage = self.attack_damage / 2
            # for psychic types, they do regular damage to fire and water types
            elif self.pokemon_type == "Psychic":
                if other_poke.pokemon_type == "Psychic":
                    self.attack_damage = self.attack_damage / 2
                else:
                    self.attack_damage = self.attack_damage
            else:
                print("Sorry, we don't have an attack for pokémon of type {} yet".format(self.pokemon_type))

        other_poke.health -= self.attack_damage
        self.revivals += 1
        self.points += 1
        print("""{name} did {attack} points of damage on {other}.
                """.format(name=self.name, attack=self.attack_damage, other=other_poke.name))
        if other_poke.health < 0:
            other_poke.health = 0
            other_poke.knock_out()
        else:
            print("""{other} now has {other_health} hit points left!
                         """.format(other=other_poke.name, other_health=other_poke.health))
        print("{} gained 1 point for a total of {} points!".format(self.name, self.points))
        print("{} gained 1 revival and has {} revival(s) total!".format(self.name, self.revivals))
        print()

        if self.points == 3:
            self.level_up()

        # reset attack damage
        self.attack_damage = 2 * self.level

    def level_up(self):
        # re-calculates stats after level up
        if self.points == 3:
            print("{} now has 3 points and is able to level up!".format(self.name))
            self.level += self.level
            self.health = self.level * 10
            self.max_health = self.level * 10
            self.revivals = self.level
            self.attack_damage = 2 * self.level
            self.points = 0
            print("""Here are {name}'s new stats: \n
                   Level: {level}
                   {health} hit points
                   {max_health} maximum hit points
                   {revivals} revivals
                   {damage} points of regular damage
                   {points} points
            """.format(name=self.name, level=self.level, health=self.health, max_health=self.max_health,
                       revivals=self.revivals, damage=self.attack_damage, points=self.points))
            print()
        else:
            print("{} only has {} revival(s) and is not eligible to level up".format(self.name, self.revivals))
            print()

# ********************************************************
# FIX ME: finish making trainer class


class Trainer:
    def __init__(self, name, current_pokemon, potions=3):
        self.name = name
        self.pokemons = 0
        self.current_pokemon = current_pokemon
        self.potions = potions


# ********************************************************

# samples pokes: one of each type
# poke1 = Pokemon("Abra", "psychic")
# print(poke1.pokemon_type)

# poke2 = Pokemon("Magmar", "Fire")

# poke3 = Pokemon("Samurott", "Water")

# poke1.attack(poke2)

# poke1.attack(poke3)
# print(poke1)

# poke3.attack(poke1)

# adding some user interaction


# displays game rules
def game_rules():
    print("************************************************************************************************")
    print("                            Welcome to the Pokémon Tournamet!")
    print("************************************************************************************************")
    print("We are currently working on increasing game functionality, but here are the current rules:")
    print()
    print("                                           RULES")
    print("This is a two-player game. Each player will be instructed to enter their pokemon name and type.")
    print("(Right now, this game only supports types Fire, Water, and Psychic.)")
    print("Every pokemon starts at level one. The stats of level one are as follows: ")
    print()
    print("""Level: 1\nMaximum Health: 10\nCurrent Health: 10\nRevivals: 1\nNumber of attacks = 0\nAttack damage = 2""")
    print()
    print("• Every player is able to use their turn to increase their health by their level number.")
    print("  You only get 3 health increases, so use them wisely!")
    print("• If you get knocked out, you have to use a revival in order to attack on your next round.")
    print("• Each player will take a turn for a total of ten rounds. To level up, gain three revivals!")
    print()
    print("                                           DAMAGE")
    print("Each pokémon type has different damage statistics. The statistics for water, fire, and psychic types are:")
    print()
    print("Water attack:")
    print("Water -> Fire: 2x damage\n"
          "Water -> Psychic: 1x damage\n"
          "Water -> Water: 1/2 damage")
    print()
    print("Fire attack:")
    print("Fire -> Water: 1/ 2 damage\n"
          "Fire -> Psychic: 1x damage\n"
          "Fire -> Fire: 1/2 damage")
    print()
    print("Psychic attack:")
    print("Psychic -> Fire: 1x damage\n"
          "Psychic -> Water: 1x damage\n"
          "Psychic -> Psychic: 1/2 damage")
    print()
    print("You got all that? Alright, let's play!")
    print("************************************************************************************************")
    print()


def choose_pokemon(name, poke_type):
    poke = Pokemon(name, poke_type)
    return poke


def game_stats(player1_points, player1_level, player2_points, player2_level):
    print("************************************************************************************************")
    print("                                            GAME OVER")
    print("************************************************************************************************")
    print("Game point summary:")
    print("Player 1: " + str(player1_points) + " points at level " + str(player1_level))
    print("Player 2: " + str(player2_points) + " points at level " + str(player2_level))

    if player1_points > player2_points:
        print("Player 1 wins!")
    elif player2_points > player1_points:
        print("Player 2 wins!")
    else:
        print("It was a tie!")


play = True
rounds = 10
remaining_rounds = 10

while play:
    game_rules()
    user_play = input("Are you ready to play (Y/N)?: ")
    user_play = user_play.upper()
    while user_play == "Y":
        poke_name1 = input("Please enter player 1's Pokémon name: ".capitalize())
        poke_type1 = input("Please enter player 1's Pokémon type (fire, water, or psychic): ".capitalize())
        poke_name2 = input("Please enter player 2's Pokémon name: ").capitalize()
        poke_type2 = input("Please enter player 2's Pokémon type (fire, water, or psychic): ".capitalize())

        poke1 = choose_pokemon(poke_name1, poke_type1)
        poke2 = choose_pokemon(poke_name2, poke_type2)

        while remaining_rounds != 0:
            for round_num in range(rounds):
                if round_num == 0 or round_num == 2 or round_num == 4 or round_num == 6 or round_num == 8:
                    print("It's {}'s turn!".format(poke1.name))
                    player1_turn = input("Would you like to attack, revive, increase health, or pass?: ").capitalize()
                    print()
                    if player1_turn == "Revive":
                        poke1.revive()
                    elif player1_turn == "Increase health":
                        print("You can gain {} point(s) of health based on your level".format(poke1.level))
                        poke1.gain_health()
                    elif player1_turn == "Attack":
                        poke1.attack(poke2)
                    else:
                        pass
                    remaining_rounds -= remaining_rounds

                else:
                    print("It's {}'s turn!".format(poke2.name))
                    player2_turn = input("Would you like to attack, revive, increase health, or pass?: ").capitalize()
                    print()
                    if player2_turn == "Revive":
                        poke2.revive()
                    elif player2_turn == "Increase health":
                        print("You can gain {} point(s) of health based on your level".format(poke2.level))
                        poke2.gain_health()
                    elif player2_turn == "Attack":
                        poke2.attack(poke1)
                    else:
                        pass
                    remaining_rounds -= remaining_rounds

        game_stats(poke1.points, poke1.level, poke2.points, poke2.level)
        user_play = input("Do you want to play again (Y/N)?: ")
        user_play = user_play.upper()
    play = False
