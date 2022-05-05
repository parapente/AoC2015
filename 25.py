#!/usr/bin/python3
import re


def next_position(row: int, column: int) -> list[int, int]:
    if row == 1:
        row = column + 1
        column = 1
    else:
        row -= 1
        column += 1
    return [row, column]


def generate_code(row: int, column: int) -> int:
    code = 20151125
    cur_row = 1
    cur_column = 1
    done = False
    while not done:
        code = (code * 252533) % 33554393
        cur_row, cur_column = next_position(cur_row, cur_column)
        if cur_row == row and cur_column == column:
            done = True
    return code


def main() -> None:
    with open('25.dat') as f:
        data = f.read()
    lines = data.split('\n')
    lines.pop()
    m = re.match(r".+ row ([0-9]+), column ([0-9]+).", lines[0])
    row = int(m.group(1))
    column = int(m.group(2))
    code = generate_code(row, column)
    print(code)


if __name__ == "__main__":
    main()
