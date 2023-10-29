from sys import argv
first, second = argv

print("{1} {0} {1} {0}".format(first, second))

first = input("update first")
second = input("update second")

print("{1} {0} {1} {0}".format(first, second))