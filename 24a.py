#!/usr/bin/python3

from functools import reduce


def combinations(package: list[int], group: list[int], options: dict, result: list[list[int]]) -> None:
    if group:
        if sum(group) > options["target"]:
            return
        if sum(group) == options["target"]:
            options["max_length"] = len(group)
            result.append(group[:])
            return

        while package:
            item = package.pop()
            group.append(item)
            combinations(package[:], group, options, result)
            group.pop()
    else:
        while package:
            item = package.pop()
            group.append(item)
            combinations(package[:], group, options, result)
            group.pop()


def find_group(package: list[int], target: int) -> list[int]:
    done = False
    result = []
    options = {'target': target, 'max_length': len(package)}
    combinations(package[:], [], options, result)
    result.sort(key=lambda x: (len(x), reduce(lambda a, b: a*b, x)), reverse=True)
    while result and not done:
        test_item = result.pop()
        rest = [item for item in package if item not in test_item]
        subgroup = [test_item[:], [], []]
        i = 1
        tmp = []
        first_seen = None
        while not done:
            if sum(tmp) > target:
                rest.insert(0, tmp.pop())
            elif sum(tmp) == target:
                subgroup[i] = tmp[:]
                i += 1
                tmp = []
            else:
                item = rest.pop()
                if first_seen == item:
                    break
                if not tmp:
                    first_seen = item
                tmp.append(item)
            if i == 3:
                done = True
    return subgroup


def get_groups(package: list[int], target: int) -> list[int]:
    package_copy = package[:]
    package_copy.sort()
    return find_group(package_copy, target)


def main():
    with open('24.dat') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()

    package = [int(weight) for weight in lines]
    target = sum(package) // 3
    print(f"Target weight: {target}")
    group = get_groups(package, target)
    qe = reduce(lambda x, y: x*y, group[0])
    print(f"{qe}")


if __name__ == "__main__":
    main()
