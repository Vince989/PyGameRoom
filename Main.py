# -*- coding: utf-8 -*-

MENU_CHOICES_LIST = ["quit", "poker", "blackjack"]


def main():
    choice = ""

    # Menu handling, will finally quit out after a good choice
    while choice not in MENU_CHOICES_LIST:
        choice = input("Hi there! What you wanna do? (Poker/Blackjack/Quit) : ").lower()

        if choice == "poker":
            print("Starting Poker...")
            # TODO Enter Poker
            break

        elif choice == "blackjack":
            print("Starting Blackjack...")
            # TODO Enter Blackjack
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
    main()
