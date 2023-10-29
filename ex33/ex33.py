i = 0
numbers = []

def loop_assign(maxx):
    i = 0
    while i < maxx:
        numbers.append(i)
        i += 1

def Zed_loop(maxx):
    i = 0
    while i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

Zed_loop(6)

print("The numbers: ")

for num in numbers:
    print(num)
