# Chat GPT Exercises about dictionaries

given_string = 'the quick brown fox jumps over the lazy dog'
occurences = {}
words = given_string.split()
each_word = ''

for items in words:
    counter = words.count(items)
    occurences[items] = counter

for k, v in occurences.items():
    print(f'{k} : {v}')
