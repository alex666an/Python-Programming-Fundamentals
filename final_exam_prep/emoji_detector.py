import re

text = input()
coolness_threshold = 0

for emoji in text:
    if emoji.isdigit():
        if coolness_threshold == 0:
            coolness_threshold += int(emoji)
        else:
            coolness_threshold *= int(emoji)

print(f"Cool threshold: {coolness_threshold}")

pattern = r'(::|\*\*)([A-Z][a-z]{2,})\1'
matches = re.findall(pattern, text)
number_of_emojis = len(matches)

print(f"{number_of_emojis} emojis found in the text. The cool ones are:")

for cool_emoji in matches:
    symbols = cool_emoji[0]
    word = cool_emoji[1]
    word_is_cool = 0
    for current_emoji in word:
        word_is_cool += ord(current_emoji)
    if word_is_cool >= coolness_threshold:
        print(f'{symbols}{word}{symbols}')