"""Fan"""
text = input()
unique = set(text)
no_pairs = ""
for char in text:
    if char in unique:
        unique.remove(char)
        if text.count(char) % 2:
            no_pairs += char
print(no_pairs if no_pairs else "fully paired")
