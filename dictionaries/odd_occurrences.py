words = input().split()
dictionary = {}

for word in words:
    word_in_lower_case = word.lower()
    if word_in_lower_case not in dictionary:
        dictionary[word_in_lower_case] = 0
    dictionary[word_in_lower_case] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')
