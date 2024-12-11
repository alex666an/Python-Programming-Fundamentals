import re

number_of_inputs = int(input())

for current_text in range(number_of_inputs):
    pattern = r'^(\$([A-Z][a-z]{2,})\$|\%([A-Z][a-z]{2,})\%): (\[\d+\]\|\[\d+\]\|\[\d+\]\|)$'
    text = input()
    matches = re.match(pattern, text)
    if not matches:
        print("Valid message not found!")
        continue

    decrypted_groups = []
    for group in matches.group(4).split('|'):
        decrypted_group = ''.join(chr(int(num[1:-1])) for num in re.findall(r'\[\d+\]', group))
        decrypted_groups.append(decrypted_group)

    decrypted_output = ''.join(decrypted_groups)
    tag = matches.group(2) or matches.group(3)
    print(f"{tag}: {decrypted_output}")