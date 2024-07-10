# Mapping digits to words
digit_to_words = {
    '0': 'null',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

def number_to_words(number):
    number_str = str(number)
    words = [digit_to_words[digit] for digit in number_str]
    return ' '.join(words)

# Example usage
input_number = int(input("Enter a number: "))
words_representation = number_to_words(input_number)
print(f"{input_number} in words: {words_representation}")
