#This mini project is made by Rohit kumar.
text = 'My name is Rohit 8542 '

count = 0
vowel = 0
total = len(text)
spaces = 0
digit = 0

for i in text.split():
    count += 1
    if i[0] in ['a', 'e', 'i', 'o', 'u']:
        vowel += 1

for i in text:
    if i in [" ", "  ", "   ", "    "]:
        spaces += 1
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        digit += 1


character = total - spaces
consonent = count-vowel
print(f'This text has {count} word.')
print(f'This text has {character} character.')
print(f'This text has {spaces} spaces.')
print(f'This text has {vowel} vowels.')
print(f'This text has {consonent} consonent.')
print(f'This text has {digit} digit.')
