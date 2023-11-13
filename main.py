import pandas

data = pandas.read_csv("statics/data/morse.csv")
data_dict = {row.iloc[0]: row.iloc[1] for (index, row) in data.iterrows()}


# Convert letters and symbols to the Morse Alphabet
def morse(user_word):
    output = []
    for char in user_word:
        if char == " ":
            output.append("(space)")
        elif char not in data_dict:
            return "Sorry, you should only enter Latin letters, numbers or some symbols (.'_:;?!–+/()=@)"
        else:
            output.append(data_dict[char])
    return ' '.join(output)


print("This is a Morse code converter!")
converter_on = True
while converter_on:
    user_input = input('Enter the word you want to convert to Morse code:\n').upper()
    print(f"The Morse Code of {user_input} is: {morse(user_input)}")
    next_word = input("Do you want to convert the next word? (Enter yes/no):\n").upper()
    if next_word == 'NO':
        converter_on = False
    while next_word != "YES" and next_word != "NO":
        print('Please,type "yes" or "no"')
        next_word = input("Do you want to convert the next word? (Enter yes/no):\n").upper()


