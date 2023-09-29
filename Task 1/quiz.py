import random


questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "Which gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
    {"question": "Who is known as the father of modern physics?", "answer": "Albert Einstein"},
    {"question": "What is the currency of Japan?", "answer": "Yen"},
    {"question": "How many continents are there on Earth?", "answer": "7"},
    {"question": "What is the largest mammal in the world?", "answer": "Blue whale"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
    {"question": "In which year did the Titanic sink?", "answer": "1912"},
    {"question": "What is the national flower of Japan?", "answer": "Cherry blossom"},
    {"question": "Who is the author of 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the freezing point of water in Fahrenheit?", "answer": "32 degrees"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "Who founded Microsoft Corporation?", "answer": "Bill Gates"},
    {"question": "What is the chemical symbol for silver?", "answer": "Ag"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "Which gas makes up the majority of Earth's atmosphere?", "answer": "Nitrogen"},
    {"question": "Who wrote the 'Harry Potter' book series?", "answer": "J.K. Rowling"},
    {"question": "What is the closest star to Earth?", "answer": "The Sun"},
    {"question": "What is the chemical symbol for carbon?", "answer": "C"},
    {"question": "What is the longest river in the world?", "answer": "Nile River"},
    {"question": "Who is known as the 'Father of India'?", "answer": "Mahatma Gandhi"},
    {"question": "What is the largest desert in the world?", "answer": "Sahara Desert"},
]


random.shuffle(questions)


def play_quiz():
    score = 0
    total_questions = len(questions)

    for question in questions:
        print(question["question"])
        user_answer = input("Your answer: ")

        if user_answer.lower() == question["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")

    print(f"You scored {score}/{total_questions}.")

if __name__ == "__main__":
    print("Welcome to the Quiz Program!")
    play_quiz()
