text = input().split()
filtered = [text for text in text if len(text) % 2 == 0]
print("\n".join(filtered))