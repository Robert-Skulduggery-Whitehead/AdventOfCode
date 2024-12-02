from input import input

input = input('1.txt')

input["left"].sort()
input["right"].sort()



def part1():
    total = 0

    for idx, x in enumerate(input["left"]):
        total += abs(int(input["left"][idx]) - int(input["right"][idx]))

    return total

def part2():
    total = 0
    
    for idx, x in enumerate(input["left"]):
        multiplier = 0
        for y in input["right"]:
            if y == x:
                multiplier += 1
        total += int(x) * multiplier
    
    return total

print("part1")
print(part1())
print("part2")
print(part2())