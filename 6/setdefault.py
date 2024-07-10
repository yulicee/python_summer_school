# user input
input = 'It was a bright cold day in April, and the clocks were striking'

char_count_with_setdefault = {} 
for char in input: 
    char_count_with_setdefault[char] = char_count_with_setdefault.setdefault(char,0) + 1 
    
print(char_count_with_setdefault)