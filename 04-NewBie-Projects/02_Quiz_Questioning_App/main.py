import time, math


def main():
    questions = ("What is the Tallest building in Earth?", "How many days in an year?", "Which Company created windows?", "Which Material is used in creating Atom Bomb?")

    options = [("Burj Khalifa", "Minar-e-Pakistan", "World Trade Center", "Jedd-ah Tower"), (200, 365, 230, 330), ("Google", "Amazon", "Tesla", "Microsoft"), ("Uranium", "Platinum", "TNT", "Aluminium")]

    correctAnswers = ('A', 'B', 'D', 'A')
    tags = ("A", "B", "C", "D")
    score = 0

    print("************  Welcome to the Quiz  ***********", end="\n\n")

    for index, question in enumerate(questions):
        print(question)
        for i, option in enumerate(options[index]):
            print(f"{tags[i]}. {option}")

        userInput = input("Enter you Choice (A,B,C,D): ").lower()
        if userInput == correctAnswers[index].lower():
            print("You Guess the Answer Right!")
            score += 1
        else:
            print("You didn't guess the right Answer")

        print()
        time.sleep(1)

    print()
    print(f"Your score is {score} / {len(questions)}")



if __name__ == '__main__':
    main()