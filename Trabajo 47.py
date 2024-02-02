user_word = input("Ingresa una palabra:")
user-wod = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
