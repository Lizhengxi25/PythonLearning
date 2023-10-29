formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter.format("Hey", "Hoo", "Haa", "Hey"), formatter, formatter, formatter))
print(formatter.format(
"Try your",
"own text here",
"Maybe a poem",
"Or a song after fear"
))

# Questions:
#	In line 6, why does it print
