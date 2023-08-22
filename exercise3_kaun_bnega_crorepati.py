# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

prizes = (1000,2000,5000)
questions = ['Which planet is known as the "Red Planet"? A) Venus B) Mars C) Jupiter D) Saturn', 'What is the largest mammal on Earth? A) Elephant B) Blue Whale C) Giraffe D) Polar Bear', 'Who wrote the play "Romeo and Juliet"? A) William Shakespeare B) William Wordsworth C) Jane Austen D) Charles Dickens']
answers=('B','B','A')
print("Welcome to Kaun Banega Crorepati!")

for i in range(3):
    print(questions[i])
    answer = input("Enter the answer: A / B / C / D : ")
    if answer.upper() == answers[i]:
        print("You won", prizes[i])
    else:
        print("Oops! Wrong Answer")
        break

print("Game Over!")