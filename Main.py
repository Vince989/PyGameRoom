# -*- coding: utf-8 -*-
import sys
from PlayingCards.Poker import Poker

MENU_CHOICES_LIST = ["quit", "poker", "blackjack"]


def main():
    choice = ""

    # Menu handling, will finally quit out after a good choice
    while choice not in MENU_CHOICES_LIST:
        choice = input("Hi there! What you wanna do? (Poker/Blackjack/Quit) : ").lower()

        if choice == "poker":
            print("Starting Poker...")
            Poker(1).play()
            break

        elif choice == "blackjack":
            print("Starting Blackjack...")
            # Enter Blackjack
            break

        elif choice == "quit":
            print("Quitting...")
            break

        else:
            print("Invalid choice, try again.")

    # It's all over folks!
    print("Leaving, all OK...")
    return


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "poker":
            Poker(1).play()
    else:
        main()
