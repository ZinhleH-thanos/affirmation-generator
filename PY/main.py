import random
import time

def get_random_affirmation():
    affirmations = [
        "You are capable of amazing things 💫",
        "Keep going — you’re getting better every day 🌱",
        "Believe in yourself. You’ve got this! ✨",
        "Mistakes are proof you're trying 💖",
        "Learning is your superpower 🧠⚡",
        "Your future in AI is sparkling bright! 🤖🌈",
        "One line of code at a time, you’re getting closer 🌟"
    ]
    return random.choice(affirmations)

def main():
    print("｡･ﾟﾟ･🌸 Welcome to the Kawaii Affirmation Generator 🌸･ﾟﾟ･｡")
    name = input("What's your name? ✨ ")
    print("\nGenerating your affirmation...")
    time.sleep(1.5)
    print(f"\n✨ Hey {name}, remember this: ✨\n")
    print(f"💬 {get_random_affirmation()}")
    print("\nHave a wonderful coding day! 💻💕")

if __name__ == "__main__":
    main()
