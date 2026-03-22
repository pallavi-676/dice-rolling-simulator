import random

# ASCII dice faces
dice_faces = {
    1: (
        "┌───────┐\n"
        "│       │\n"
        "│   ●   │\n"
        "│       │\n"
        "└───────┘"
    ),
    2: (
        "┌───────┐\n"
        "│ ●     │\n"
        "│       │\n"
        "│     ● │\n"
        "└───────┘"
    ),
    3: (
        "┌───────┐\n"
        "│ ●     │\n"
        "│   ●   │\n"
        "│     ● │\n"
        "└───────┘"
    ),
    4: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│       │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
    5: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│   ●   │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
    6: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "└───────┘"
    )
}


def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        results.append(roll)
    return results


def display_dice(results):
    lines = [""] * 5

    for num in results:
        face = dice_faces[num].split("\n")
        for i in range(5):
            lines[i] += face[i] + "  "

    for line in lines:
        print(line)


def main():
    print("🎲 Dice Rolling Simulator 🎲")

    while True:
        try:
            num_dice = int(input("\nEnter number of dice to roll: "))
            if num_dice <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        results = roll_dice(num_dice)

        print("\n🎯 Results:")
        display_dice(results)
        print("Values:", results)
        print("Total:", sum(results))

        again = input("\nRoll again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye 👋")
            break


if __name__ == "__main__":
    main()