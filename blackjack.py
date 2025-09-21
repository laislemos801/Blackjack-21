import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep_playing = True
keep_getting_cards = True

def sort_initial_cards() -> list[int]:
    chosen_cards = random.choices(cards, k=2)

    return chosen_cards

def sum_cards(cards: list[int]) -> int:
    sum = 0
    for card in cards:
        sum += card

    return sum

def get_another_card(cards: list[int]) -> list[int]:
    new_card = random.choice(cards)
    cards.append(new_card)

    return cards

def print_final_hands(user_cards: list[int], user_sum: int, computer_cards: list[int], computer_sum: int):
    print(f"     Your final hand: {user_cards}, final score: {user_sum}")
    print(f"     Computer's final hand: {computer_cards}, final score: {computer_sum}")

def check_winner(user_cards: list[int], user_sum: int, computer_cards: list[int], computer_sum: int):
    while computer_sum < 17:
        computer_cards = get_another_card(computer_cards)
        computer_sum = sum_cards(computer_cards)

    if user_sum > 21:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("You went over. You lose :(")

    elif computer_sum > 21:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("Opponent went over. You win :)")

    elif user_sum == computer_sum:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("It's a Draw!")

    elif user_sum > computer_sum:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("You win! :)")

    else:
        print_final_hands(user_cards, user_sum, computer_cards, computer_sum)
        print("You lose :(")

while keep_playing:
    user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if user_choice == 'y':
        print(logo)

        user_cards = sort_initial_cards()
        computer_cards = sort_initial_cards()

        user_sum = sum_cards(user_cards)
        computer_sum = sum_cards(computer_cards)

        print(f"     Your cards: {user_cards}, current score: {user_sum}")
        print(f"     Computer's first card: {computer_cards[0]}")

        while keep_getting_cards:
            another_card = input("\nType 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                new_cards = get_another_card(user_cards)
                user_sum = sum_cards(new_cards)

                print(f"     Your cards: {user_cards}, current score: {user_sum}")
                print(f"     Computer's first card: {computer_cards[0]}")

            elif another_card == 'n':
                check_winner(user_cards, user_sum, computer_cards, computer_sum)
                keep_getting_cards = False
            else:
                print("What you typed is not an option. Try again.")

        check_winner(user_cards, user_sum, computer_cards, computer_sum)
        
    elif user_choice == 'n':
        keep_playing = False

    else:
        print("What you typed is not an option. Try again.")