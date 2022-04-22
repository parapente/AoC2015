#!/usr/bin/python3
from copy import copy, deepcopy

class Person:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.damage = 0
        self.mana = 0
        self.armor = 0
        self.total_armor = 0
        self.active_spells = []

    def __init__(self, name: str):
        self.name = name
        self.hp = 0
        self.damage = 0
        self.mana = 0
        self.armor = 0
        self.total_armor = 0
        self.active_spells = []

    def __repr__(self):
        active_spells = ",".join([i.name for i in self.active_spells])
        return f"{self.name}: HP={self.hp}, DAMAGE={self.damage}, MANA={self.mana}, ARMOR={self.armor}, TOTAL_ARMOR={self.total_armor}, ACTIVE_SPELLS[{active_spells}]"
    

class Spell:
    def __init__(self):
        self.name = ""
        self.cost = 0
        self.health = 0
        self.damage = 0
        self.armor = 0
        self.mana = 0
        self.effect = 0

    def __init__(self, data: list):
        self.name = data[0]
        self.cost, self.health, self.damage, self.armor, self.mana, self.effect = [int(i) for i in data[1:]]

    def __repr__(self):
        return f"Spell: {self.name}, {self.cost}, {self.health}, {self.damage}, {self.armor}, {self.mana}, {self.effect}"


def init() -> tuple[Person, Person, list[Spell]]:
    with open('22.dat') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    boss = Person("Boss")
    boss.hp = int(lines[0].split(': ')[1])
    boss.damage = int(lines[1].split(': ')[1])

    hero = Person("Hero")
    hero.hp = 50
    hero.mana = 500

    with open('22.spells') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    lines.pop(0)
    spells = list()
    for line in lines:
        line = " ".join(line.split())
        spells.append(Spell(line.split()))
    return hero, boss, spells


def spell_check(active_spells: list[Spell]) -> None:
    for spell in active_spells:
        if spell.name == "Shield":
            print(f"Shield's timer is now {spell.effect - 1}.")
        if spell.name == "Poison":
            print(f"Poison's deals {spell.damage} damage; its timer is now {spell.effect - 1}.")
        if spell.name == "Recharge":
            print(f"Recharge provides {spell.mana} mana; its timer is now {spell.effect - 1}.")
        if spell.effect == 1:
            print(f"{spell.name} wears off.")

def replay_fight(hero: Person, boss: Person, spells: list[Spell], solution: str) -> None:
    turn = 0
    mana_spend = 0
    max_mana_spend = 100000
    while hero.hp > 0 and boss.hp > 0:
        if turn % 2:
            # Boss's turn
            print("")
            print("-- Boss turn --")
            print(f"- Player has {hero.hp} hit points, {hero.total_armor} armor, {hero.mana} mana")
            print(f"- Boss has {boss.hp} hit points")
            spell_check(hero.active_spells)
            hero, boss, mana_spend = calc_solution(hero, boss, mana_spend, max_mana_spend, spells, "-")
            if boss.hp > 0:
                if hero.total_armor:
                    print(f"Boss attacks for {boss.damage} - {hero.total_armor} = {boss.damage - hero.total_armor} damage!")
                else:
                    print(f"Boss attacks for {boss.damage} damage!")
        else:
            # Hero's turn
            print("")
            print("-- Player turn --")
            print(f"- Player has {hero.hp} hit points, {hero.total_armor} armor, {hero.mana} mana")
            print(f"- Boss has {boss.hp} hit points")
            spell_check(hero.active_spells)
            hero, boss, mana_spend = calc_solution(hero, boss, mana_spend, max_mana_spend, spells, solution[turn])
            spell_name = spells[int(solution[turn])].name
            if spell_name == "MagicMissile":
                print(f"Player casts {spells[int(solution[turn])].name}, dealing {spells[int(solution[turn])].damage} damage.")
            elif spell_name == "Shield":
                print(f"Player casts {spells[int(solution[turn])].name}, increasing armor by {spells[int(solution[turn])].armor}.")
            else:
                print(f"Player casts {spells[int(solution[turn])].name}")
        turn += 1
    if boss.hp <= 0:
        print("This kills the boss and the player wins.")
    else:
        print("This kills the player...")


def calc_solution(hero: Person, boss: Person, mana_spend: int, max_mana_spend: int|None, spells: list[Spell], seed: str) -> tuple[Person, Person, int]:
    if seed != "-": # Hero's turn
        hero.hp -= 1
    if hero.hp > 0:
        # Apply previous effects
        for prev_spell in hero.active_spells:
            if prev_spell.effect != 1:
                if prev_spell.name == "Shield":
                    hero.total_armor = hero.armor + prev_spell.armor
            else:
                if prev_spell.name == "Shield":
                    hero.total_armor = hero.armor
            boss.hp -= prev_spell.damage
            hero.mana += prev_spell.mana
            prev_spell.effect -= 1
        if seed != "-": # Hero's turn
            spell = spells[int(seed)]
            mana_spend += spell.cost
            if mana_spend > max_mana_spend:
                hero.hp = -1
            hero.mana -= spell.cost
            if spell.effect == -1: # Immediate effect
                boss.hp -= spell.damage
                hero.hp += spell.health
            else:
                hero.active_spells.append(copy(spell))
                if spell.name == "Shield":
                    hero.total_armor = hero.armor + spell.armor
        else: # Boss' turn
            if boss.hp > 0:
                total_damage = boss.damage - hero.total_armor
                if total_damage <= 0:
                    total_damage = 1
                hero.hp -= total_damage

    hero.active_spells = [copy(spell) for spell in hero.active_spells if spell.effect > 0]
    return hero, boss, mana_spend


def find_solution(hero: Person, boss: Person, spells: list[Spell]) -> tuple[int, str]:
    solution_min_mana = 100000
    solution_sequence = ""
    max_mana_spend = 100000
    solution = ""
    branches = [str(i) for i in range(len(spells))]
    comb = dict()
    min_mana = 10000 # minimum amount of mana needed to cast a spell
    for spell in spells:
        if spell.cost < min_mana:
            min_mana = spell.cost

    # Calculate all possible spell combinations
    while (branches):
        branch = branches.pop()
        solution = branch
        hero_check = None
        boss_check = None
        if len(solution) == 1:
            hero_check = deepcopy(hero)
            boss_check = deepcopy(boss)
            mana_spend = 0
        else:
            hero_check, boss_check, mana_spend = comb[solution[:-1]]
        comb[solution] = calc_solution(deepcopy(hero_check), deepcopy(boss_check), mana_spend, max_mana_spend, spells, solution[-1])
        if comb[solution][0].hp > 0 and comb[solution][2] < solution_min_mana: # if solution doesn't lead to player losing
            if comb[solution][1].hp <= 0: # if player wins
                # print("Player wins! Solution: " + solution + " cost: " + str(comb[solution][2]))
                if solution_min_mana > comb[solution][2]:
                    solution_min_mana = comb[solution][2]
                    solution_sequence = solution
            elif len(solution) % 2: # Boss' turn
                branches.append(solution + '-')
            elif not (len(comb[solution][0].active_spells) == 0 and comb[solution][0].mana < min_mana): # if you can still cast a spell
                # Hero's turn
                if comb[solution][0].active_spells:
                    active = [i.name for i in comb[solution][0].active_spells if i.effect > 1]
                else:
                    active = []
                #print(active)
                for i in range(len(spells)):
                    if spells[i].name not in active and comb[solution][0].mana >= spells[i].cost:
                        branches.append(solution + str(i))

    return solution_min_mana, solution_sequence


def main():
    hero, boss, spells = init()
    min_mana, solution = find_solution(deepcopy(hero), deepcopy(boss), spells)
    print(min_mana, solution)
    if solution:
        replay_fight(hero, boss, spells, solution)
    else:
        print("No solution found")



if __name__ == "__main__":
    main()
