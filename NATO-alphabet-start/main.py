import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter:row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = ''
while word.lower() not in ['exit', 'quit', 'bye']:
    word = input("Type a word: ")
    codes = [nato_alphabet.get(char.upper(), char) for char in word]
    print(f"code: {' '.join(codes)}")

print()
word = 'good bye!'
codes = [nato_alphabet.get(char.upper(), char) for char in word]
print(f"{' '.join(codes)}")
