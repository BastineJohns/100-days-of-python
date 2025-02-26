import random
word_list= [
    "Balloon",  # 'l', 'o'
    "Success",  # 's', 'c'
    "Mississippi",  # 's', 'i', 'p'
    "Assessment",  # 's', 'e'
    "Committee",  # 't', 'e', 'm'
    "Parallel",  # 'l', 'a'
    "Happiness",  # 'p', 's'
    "Bookkeeper",  # 'o', 'k', 'e'
    "Tennessee",  # 'n', 'e', 's'
    "Occasion",  # 'c', 'o'
]

try_string = "HANGMAN"
n_tries = 0
random_word = random.choice(word_list).lower()
blank_string = "_" * len(random_word)
new_blank_string = list(blank_string)
print(random_word)

while n_tries < len(try_string):
    user_input = input("guess a letter: ").lower()
    for i in range(len(random_word)):
        if random_word[i] == user_input:
            new_blank_string[i] = user_input
            blank_string = "".join(new_blank_string)
            
        else :
            continue
    print(blank_string)
    if blank_string == random_word:
        print("You have won")
        break     
    n_tries += 1
if blank_string != random_word:
    print("no more attempts left")
    



