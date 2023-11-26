text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
words = text.split(' ')
words = [word.strip(',') for word in words]
words = [word.strip('.') for word in words]
words = [word.strip('\n') for word in words]
words = [word for word in words if word != '']
print(words)
numberofletters = [len(word) for word in words]
pi=''
for number in numberofletters:
    pi += str(number)
print(pi)

