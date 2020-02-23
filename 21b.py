#!/usr/bin/python3
import copy


class Person:
    hp = 0
    damage = 0
    armor = 0


def fight(hero, boss):
    turn = 0
    while hero.hp > 1 and boss.hp > 1:
        if turn % 2:
            # Boss's turn
            damage = boss.damage - hero.armor
            if damage < 1:
                damage = 1
            hero.hp -= damage
        else:
            # Hero's turn
            damage = hero.damage - boss.armor
            if damage < 1:
                damage = 1
            boss.hp -= damage
        turn += 1
    if hero.hp < 1:
        return False
    return True


def main():
    with open('21.dat') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    boss = Person()
    boss.hp = int(lines[0].split(': ')[1])
    boss.damage = int(lines[1].split(': ')[1])
    boss.armor = int(lines[2].split(': ')[1])

    hero = Person()
    hero.hp = 100
    hero.damage = 0
    hero.armor = 0

    with open('21.weapons') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    lines.pop(0)
    weapons = list()
    for line in lines:
        line = " ".join(line.split())
        weapons.append(line.split())

    with open('21.armor') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    lines.pop(0)
    armor = list()
    for line in lines:
        line = " ".join(line.split())
        armor.append(line.split())

    with open('21.rings') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    lines.pop(0)
    rings = list()
    for line in lines:
        line = line.replace(' +', '+')
        line = " ".join(line.split())
        rings.append(line.split())

    # Calculate all possible equipment combinations and their prices
    comb = list()
    for weapon in weapons:
        mode = 0
        armortype = 0
        ring1type = 0
        ring2type = 0
        skip = False
        equipment = list()
        # We need at least a weapon...
        # We then have 4 modes:
        # * No armor or rings
        # * No rings
        # * No armor
        # * Armor and rings
        while mode < 4:
            price = 0
            equipment = list()
            if mode == 0:
                equipment = [weapon]
                price += int(weapon[1])
                mode += 1
            elif mode == 1:
                equipment = [weapon, armor[armortype]]
                price += int(weapon[1]) + int(armor[armortype][1])
                armortype += 1
                if armortype == len(armor):
                    armortype = 0
                    mode += 1
                    ring1type = 0
            elif mode == 2:
                if ring1type == ring2type:
                    skip = True
                else:
                    if ring2type == -1:
                        price += int(weapon[1]) + int(rings[ring1type][1])
                        equipment = [weapon, rings[ring1type]]
                    else:
                        price += int(weapon[1]) + int(rings[ring1type][1]) +\
                            int(rings[ring2type][1])
                        equipment = [weapon, rings[ring1type],
                                     rings[ring2type]]
                ring1type += 1
                if ring1type == len(rings):
                    ring2type += 1
                    ring1type = 0
                if ring2type == len(rings):
                    mode += 1
                    armortype = 0
                    ring1type = 0
                    ring2type = -1
            else:
                if ring1type == ring2type:
                    skip = True
                else:
                    if ring2type == -1:
                        price += int(weapon[1]) + int(armor[armortype][1]) +\
                            int(rings[ring1type][1])
                        equipment = [weapon, armor[armortype],
                                     rings[ring1type]]
                    else:
                        price += int(weapon[1]) + int(rings[ring1type][1]) +\
                            int(rings[ring2type][1]) + int(armor[armortype][1])
                        equipment = [weapon, armor[armortype],
                                     rings[ring1type], rings[ring2type]]
                ring1type += 1
                if ring1type == len(rings):
                    ring2type += 1
                    ring1type = 0
                if ring2type == len(rings):
                    armortype += 1
                    ring1type = 0
                    ring2type = -1
                    if armortype == len(armor):
                        mode += 1
            if not skip:
                comb.append([price, equipment])
            else:
                skip = False
    comb.sort(reverse=True, key=lambda x: x[0])
    # print(comb)

    win = True
    i = 0
    while win:
        hero.damage = 0
        hero.armor = 0
        print('Boss -- HP:', boss.hp, 'Damage:', boss.damage,
              'Armor:', boss.armor)
        print('After visiting the shop our hero has:')
        for e in comb[i][1]:
            print(e[0])
            hero.damage += int(e[2])
            hero.armor += int(e[3])
        print("spending", comb[i][0], "gold coins.")
        print('Hero -- HP:', hero.hp, 'Damage:', hero.damage,
              'Armor:', hero.armor)
        win = fight(copy.copy(hero), copy.copy(boss))
        i += 1
    print('Hero loses!')


if __name__ == "__main__":
    main()
