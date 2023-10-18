import string
class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        print("Альфобет:",self.letters)
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__('En',string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self.__letters_num

english_alphabet = EngAlphabet()
english_alphabet.print()
print("Номер литары:", english_alphabet.letters_num())

letter = "A"
if english_alphabet.is_en_letter(letter):
    print(f"'{letter}' гэта англ литара")
else:
    print(f"'{letter}' гэта NO англ литара")
