#!/usr/bin/python3
register_pos = {'a': 0, 'b': 1}

def hlf(pc: int, reg: list[int], args: list[str]) -> int:
	reg[register_pos[args[0]]] //= 2
	return pc + 1

def tpl(pc: int, reg: list[int], args: list[str]) -> int:
	reg[register_pos[args[0]]] *= 3
	return pc + 1

def inc(pc: int, reg: list[int], args: list[str]) -> int:
	reg[register_pos[args[0]]] += 1
	return pc + 1

def jmp(pc: int, reg: list[int], args: list[str]) -> int:
	offset = int(args[0])
	return pc + offset

def jie(pc: int, reg: list[int], args: list[str]) -> int:
	if (int(reg[register_pos[args[0]]]) % 2) == 0:
		return jmp(pc, reg, args[1:])
	else:
		return pc + 1

def jio(pc: int, reg: list[int], args: list[str]) -> int:
	if int(reg[register_pos[args[0]]]) == 1:
		return jmp(pc, reg, args[1:])
	else:
		return pc + 1

def main():
	with open('23.dat') as f:
		data = f.read()
	lines = data.split('\n')
	lines.pop()

	op = []
	pc = 0
	reg = [1, 0]

	for line in lines:
		line = line.replace( ',', '').split()
		op.append(line)

	while pc >= 0 and pc < len(op):
		print(f"{pc}: {op[pc][0]} {', '.join(op[pc][1:])} [a={reg[0]}, b={reg[1]}]")
		pc = globals()[op[pc][0]](pc, reg, op[pc][1:])
	
	print(reg[1])


if __name__ == "__main__":
	main()
