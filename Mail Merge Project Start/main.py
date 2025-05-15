#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER="[name]"

def get_template():
    with open("Input/Letters/starting_letter.txt", mode="r") as file:
        return file.read()

def get_names():
    with open("Input/Names/invited_names.txt", mode="r") as file:
        return  file.readlines()

def make_letter(letter_template, recipient):
    stripped_name = recipient.strip()
    with open(f"Output/ReadyToSend/letter_{stripped_name}.txt", mode="w") as file:
        letter = letter_template.replace(PLACEHOLDER, stripped_name)
        # letter = letter.replace('Angela', 'Corey')
        file.write(letter)

if __name__ == "__main__":
    template = get_template()
    names = get_names()
    for name in names:
        make_letter(template, name)

