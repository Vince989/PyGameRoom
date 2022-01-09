# -*- coding: utf-8 -*-
import sys
from PlayingCards.Blackjack import Blackjack

MENU_CHOICES_LIST = ["quit", "poker", "blackjack"]


def main():
    choice = ""

    # Menu handling, will finally quit out after a good choice
    while choice not in MENU_CHOICES_LIST:
        choice = input("Hi there! What you wanna do? (Poker/Blackjack/Quit) : ").lower()

        while choice == "poker":
            print("Starting Poker...")
            break

        while choice == "blackjack":
            print("\nNew Blackjack round...")
            players = 2  # TODO Ask how many would like to play
            blackjack = Blackjack(players)
            blackjack.console_setup()
            blackjack.play_console()
            if input("Want to do another round? ").lower() != "yes":
                break

        if choice == "quit":
            print("Quitting...")
            break

    print("Leaving, all OK...")
    return


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "blackjack":
            players = 2
            blackjack = Blackjack(players)
            blackjack.console_setup()
            blackjack.play_console()
    else:
        main()
