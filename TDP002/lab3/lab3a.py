#! /usr/bin/env python3

#importerar funktionen för att få en slumpmässigt siffra
import random


# ================================================================================
# Kort ADT
# ================================================================================
# Color ska vara antningen 1(svart) eller 2(röd)
# Value får vara fom 1 tom 13 för svart och fom 14 tom 26 för röd plus 27 för båda jokrarna.
def create_card(value, color_nr):
    card = (value, color_nr)
    return card

def show_card (card):
# Jokrar
    if card[0] == 27 and card[1] == 1:
        print("Black joker")
    elif card[0] == 27 and card[1] == 2:
        print("Red joker")
    elif card[1] == 1:
        print(card[0], "of black")
    elif card[1] == 2:
        print(card[0], "of red")
        
def get_value(card):
    return card[0]

def get_suit(card):
    return card[1]


# ================================================================================
# Kortlek ADT
# ================================================================================

def create_deck():
    deck = ["Deck", [], []]
    for i in range (1, 27):
        if i <= 13:
            new_card = create_card(i, 1)
            deck[1].append(new_card)
        elif i > 13:
            new_card = create_card(i, 2)
            deck[1].append(new_card)
    black_joker = create_card(27, 1)
    red_joker = create_card(27, 2)
    deck[1].append(black_joker)
    deck[1].append(red_joker)
    return deck

def show_deck(deck):
    print("{:<10}{:>5}".format("Position", "Card"))
    print("="*20)
    for i in range(len(deck[1])):
        print("{:<5}\t".format(i + 1), end = "")
        show_card(deck[1][i])
    print("Cuted cards:")
    for j in range(len(deck[2])):
        print("{:<5}\t".format(j + 1), end = "")
        show_card(deck[2][j])

    print()

def get_location(deck, value, suit):

    for i in deck[1]:
        if get_value(i) == value and get_suit(i) ==  suit:
            return deck[1].index(i) + 1
    

def cut_deck(deck, start, end):
  
    for i in range (end - 1 , start - 2, -1):
        cut_card = deck[1][i]
        deck[2].insert(0, cut_card)

    del deck[1][start - 1 : end]
        
        
def merge_deck(deck):
    i = len(deck[2]) - 1
    while i >= 0:
        deck[1].insert(0, deck[2][i])
        i -= 1
    deck[2].clear()
    
def get_top_card(deck):
    top_card = deck[1][0]
    return top_card

def get_bottom_card(deck):
    bottom_card = deck[1][-1]
    return bottom_card

def shuffle_cards(deck, key):
    random.seed(key)
    random.shuffle(deck[1])

# step kan vara plus eller minus beroende på om man vill flytta kortet  neråt eller uppåt. Minus för neråt och plus för uppåt
def move_card(deck, suit, step):
    current_index = get_location(deck, 27, suit) - 1
    card_to_move = deck[1][current_index]
    deck[1].remove(card_to_move)
    new_index = (current_index - step)
    if new_index != 27:
        new_index = new_index % 27
    deck[1].insert(new_index, card_to_move )

# ================================================================================
# top_bottom_joker_location
# ================================================================================
def top_bottom_joker_location(deck):
    joker1_location = get_location(deck, 27, 1)
    joker2_location = get_location(deck, 27, 2)
    top_joker_location = joker1_location
    bottom_joker_location = joker1_location
    if joker1_location > joker2_location:
        top_joker_location = joker2_location
    else:
        bottom_joker_location = joker2_location

    return top_joker_location, bottom_joker_location


# ================================================================================
# last_card_location 
# ================================================================================

def last_card_location(deck):
    location = get_location(deck, get_value(get_bottom_card(deck)), get_suit(get_bottom_card(deck)))
    return location


# ================================================================================
# swap_cba funktionen
# (A-B-C) -> (C-B-A)
# ================================================================================

def swap_cba(deck):

    top_joker_location, bottom_joker_location = top_bottom_joker_location(deck)
    cut_deck(deck, 1, top_joker_location - 1)


    top_joker_location, bottom_joker_location = top_bottom_joker_location(deck)
    cut_deck(deck, top_joker_location, bottom_joker_location)


    last_card = last_card_location(deck)
    cut_deck(deck, 1, last_card)

    merge_deck(deck)


# ================================================================================
# bottom_based_cut funktion
# Funkionen flyttar så många kort från övre delen av kortlek som värdet på det understa kortet och sätter in de precis ovanför det understa kortet
# ================================================================================

def bottom_based_cut(deck):

    bottom_card = get_bottom_card(deck)
    value = get_value(bottom_card)

    if value != 27:
        last_card = last_card_location(deck)
        cut_deck(deck, last_card, last_card)


        cut_deck(deck, 1, value)


        last_card = last_card_location(deck)
        cut_deck(deck, 1, last_card)
        
        merge_deck(deck)
        
    else:
        prin("No card has to move!")
            

# ================================================================================
# find_key funktion
# ================================================================================
def find_key(deck):
    top_card = get_top_card(deck)
    value = get_value(top_card)
    key_card = deck[1][value]
    
    key_card_value = get_value(key_card)
    if key_card_value != 27:
        return key_card_value
    else:
        return 0

# ================================================================================
# number_to_char funktionen
# ================================================================================
def number_to_letter(number):

    letter = chr(number + 64)
    return letter

# ================================================================================
# char_to_number funktionen
# ================================================================================
def letters_to_number(string):
    number_list = []
    for i in string:
        i = i.upper()
        number_list.append(ord(i) - 64)
    return number_list

# ================================================================================
# Solitaire_keystream funktionen
# ================================================================================
def solitaire_keystream(lenght, deck):
    
    key_stream = ""
    
    shuffle_cards(deck, 4)
    # print("After shuffling")
    # show_deck(deck)

    condition = 1
    while condition <= lenght:
        move_card(deck, 1, -1)
        move_card(deck, 2, -2)
                      
        swap_cba(deck)
       

        bottom_based_cut(deck)
       

        key = find_key(deck)

        if key != 0:
            key_stream += number_to_letter(key)
            condition += 1

    
    return key_stream

# ================================================================================
# Solitaire_encrypt funktionen
# ================================================================================

def solitaire_encrypt(unfiltered_message, deck):
    message = ""
    for i in unfiltered_message:
        if i.isalpha():
             message += i

    
    print("Encrypting...")
    print("Message to encrypt:\t", message)
    key_stream = solitaire_keystream(len(message), deck)
    print("Keystream generated:\t", key_stream)
    message_number = letters_to_number(message)
    print("Message --> number:\t", message_number)
    key_stream_number = letters_to_number(key_stream)
    print ("Keystream --> number\t", key_stream_number)
    added_numbers = []
    for i in range(len(message_number)):
       j  = (message_number[i] + key_stream_number[i]) % 26
       added_numbers.append(j)
    print("(Message numbers + keystream numbers) mod 26:\t", added_numbers)
    encrypted_message = ""
    for i in added_numbers:
        encrypted_message += number_to_letter(i)
    print("Encrypted message:\t", encrypted_message)
    return encrypted_message
# ================================================================================
# Solitaire_decrypt funktionen
# ================================================================================

def solitaire_decrypt(secret, deck):
    
    print("Decrypting...")
    print("Secret message to decrypt:\t", secret)
    key_stream = solitaire_keystream(len(secret), deck)
    print("Keystream generated:\t", key_stream)
    secret_number = letters_to_number(secret)
    print("Secret message --> number:\t", secret_number)
    key_stream_number = letters_to_number(key_stream)
    print("Keystream --> number:", key_stream_number)
    subtracted_numbers = []
    for i in range(len(secret_number)):
       j  = (secret_number[i] - key_stream_number[i]) % 26
       subtracted_numbers.append(j)
    print("(Secret message number - keystream number):\t", subtracted_numbers)
    decrypted_message = ""
    for i in subtracted_numbers:
        decrypted_message += number_to_letter(i)
    print("Decrypted message:\t", decrypted_message)

# ================================================================================
# Main
# ================================================================================
def main():
    while True:
        selection = int(input("Select one option\n1. Encrypt\n2. Decrypt\n3. Exit\n"))
        if selection == 1:
            message = input("Write your message to start encrypting:\t")
            print()
            deck = create_deck()
            encrypted_message = solitaire_encrypt(message, deck)
        elif selection == 2:
            message = input("Write your secret message to start decrypting:\t")
            print()
            deck = create_deck()
            encrypted_message = solitaire_decrypt(message, deck)
        elif selection == 3:
            break
        print()
                
    

# ================================================================================
# Huvudprogram
# ================================================================================

if __name__ == "__main__":
    main()
# deck1 = create_deck()
# deck2 = create_deck()
# secret_message = solitaire_encrypt("Python3", deck1)
# print("\n\n")
# solitaire_decrypt(secret_message, deck2)




