import random


def main():
    print(f'Coin Flip Game!')
    user = input("Heads or Tails? 1=heads, 2=tails: ")
    coin_sides = ['Heads', 'Tails']
    num_side = random.randint(0, 1)
    print(f"The coin is flipped. It Reveals: {coin_sides[num_side]}")
    if (int(user) == 1 and num_side == 0) or (int(user) == 2 and num_side == 1):
        print("Great! You guessed it correctly.")
    else:
        print("Try again. You guessed it wrong.")


main()
