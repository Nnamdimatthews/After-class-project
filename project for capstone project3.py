# Introduction🔍
print("Welcome to quizies.😁 In this quiz, there will be 7 questions & 5 options. good luck😉")

# questions, answers & options
question = ("what is 4*3?","who is the fastest person on earth", "who is has the most subscribers on youtube", "what is the biggest star", "who is the biggest giant human in history",)
options = (("A. 16","B. 20","C. 12","D. 15"), ("A. dan","B. goldilocks","C. snowwhite","D.Usain Bolt"), ("A. Mr beast","B. juny","C. cillerenda","D. tony"), ("A. Jett","B. UY Scuti","C. Dizzy","D. Donnie"), ("A. Ryan","B. Skye","C. Sonic","D. Robert Pershing Wadlow"), (""), (""))
answers = ("C.","D.","A.","B.","D.")
guesses = []
score = 0
question_num = 0

for questions in question:
    print("---------------------------")
print(question)
for option in options[question_num]:
       print(option)


guess = input("Enter (A, B, C, D): ").upper()
guesses.append(guess)
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")
else:
    print("INCORRECT!")
    print(f"{answers[question_num]} is the correct answer")
question_num += 1

print("---------------------")
print("       RESULT        ")
print("---------------------")

print("answers:", end="")
for answer in answers:
    print("answers:", end=" ")
print()

print("answers:", end="")
for answer in answers:
     print(answer, end=" ")
print()

score = int(score / len(questions ) * 100)
print = int(f"Your score is: ")