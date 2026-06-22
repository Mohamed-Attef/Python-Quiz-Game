def ask_question(question, options, correct_answer):
    print("\n" + question)

    for option in options:
        print(option)

    answer = input("Enter your answer (A, B, C, or D): ").upper()

    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")
        return 0


def main():
    print("================================")
    print("      Python Quiz Game")
    print("================================")

    score = 0

    questions = [
    {
        "question": "1. Which function is used to display output in Python?",
        "options": [
            "A. input()",
            "B. print()",
            "C. output()",
            "D. display()"
        ],
        "answer": "B"
    },
    {
        "question": "2. Which symbol is used for comments in Python?",
        "options": [
            "A. //",
            "B. <!-- -->",
            "C. #",
            "D. *"
        ],
        "answer": "C"
    },
    {
        "question": "3. What is the correct way to store the number 10 in a variable named age?",
        "options": [
            "A. age = 10",
            "B. 10 = age",
            "C. age := 10",
            "D. int age = 10"
        ],
        "answer": "A"
    },
    {
        "question": "4. Which data type is used to store text in Python?",
        "options": [
            "A. int",
            "B. bool",
            "C. float",
            "D. str"
        ],
        "answer": "D"
    },
    {
        "question": "5. Which loop is commonly used to repeat code while a condition is true?",
        "options": [
            "A. if",
            "B. while",
            "C. print",
            "D. input"
        ],
        "answer": "B"
    }
]

    for q in questions:
        score += ask_question(
            q["question"],
            q["options"],
            q["answer"]
        )

    print("\n================================")
    print(f"Quiz Finished! Your Score: {score}/{len(questions)}")

    if score == len(questions):
        print("Excellent! Perfect Score!")
    elif score >= 3:
        print("Good Job!")
    else:
        print("Keep Practicing!")
    print("================================")


main()