class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.content = ""
    
    def read_file(self):
        with open(self.filename, 'r+') as file:
            self.content = file.read()
    
    def count_lines(self):
        return self.content.count('\n') + 1
    
    def count_words(self):
        return len(self.content.split())
    
    def count_characters(self):
        return len(self.content.replace(" ", "").replace("\n", ""))
    
    def find_longest_word(self):
        return max(self.content.split(), key=len)

def input_with_default(prompt, default):
    user_input = input(prompt)
    print(type(user_input))
    return user_input if user_input else default

def main():
    filename = input_with_default("Enter the filename: ", "sample.txt")
    analyzer = TextAnalyzer(filename)
    analyzer.read_file()
    
    num_lines = analyzer.count_lines()
    num_words = analyzer.count_words()
    num_characters = analyzer.count_characters()
    longest_word = analyzer.find_longest_word()
    
    print(f"File Analysis for '{filename}':")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of characters (excluding spaces): {num_characters}")
    print(f"Longest word: '{longest_word}'")

if __name__ == "__main__":
    main()
