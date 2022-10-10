from tkinter import font
from question import Question
import turtle
import random
turtle.setup(575, 575)
pen = turtle.Turtle()
pen.speed(.5)
pen.pensize(100)
pen.hideturtle()
turtle.hideturtle()


def getQuestions():
    questions = []
    with open("assignments\\Hangman\\questions.txt") as file:
        for line in file:
            data = line.replace("\n", "")
            data = data.split(':')
            fileQuestion = data[0].strip()
            fileAnswer = data[1].strip()
            questions.append(Question(fileQuestion, fileAnswer, "", False))
    return questions


def displayQuestion(question):
    currentQuestion = question.getQuestion()
    turtle.up()
    turtle.setpos(-200, 100)
    turtle.down()
    style = ("courier", 20, "bold")
    turtle.write(currentQuestion, font=style, align="left")


def displayAnswer(question):
    global incorrectGuesses, questionSelection, userAnswerCheck, answerLen
    userAnswer = turtle.textinput("Guess", "Enter a Guess: ")
    answerLen = len(questions[questionSelection].getAnswer()) - 1
    currentAnswer = question.getAnswer().lower()
    turtle.up()
    turtle.setpos(-200, 50)
    turtle.down()
    style = ("courier", 20, "bold")
    answerShow = ""
    for i in range(len(currentAnswer)):
        answerShow += "_ "
    turtle.write(answerShow, font=style, align="left")
    iterationCount = 0
    if userAnswer not in currentAnswer:
        incorrectGuesses += userAnswer
        turtle.up()
        turtle.setpos(-200, -50)
        turtle.down()
        turtle.write("Incorrect Guesses: ", font=style, align="left")
        for i in range(len(incorrectGuesses)):
            turtle.up()
            turtle.setpos(-200 + i * 25, -75)
            turtle.down()
            turtle.write(incorrectGuesses[i], font=style, align="left")
    for let in currentAnswer:
        if userAnswer == let:
            turtle.up()
            turtle.setpos(-200 + iterationCount * 32, 50)
            turtle.down()
            turtle.write(userAnswer, font=style, align="left")
            userAnswerCheck += 1
        iterationCount += 1
    if userAnswerCheck >= answerLen:
        turtle.clear()
        turtle.up()
        turtle.setpos(0, 0)
        turtle.down()
        turtle.write("You win!", font=style, align="center")


def clickScreen(x, y):
    global questionSelection
    displayAnswer(questions[questionSelection])


incorrectGuesses = []
questions = getQuestions()
questionSelection = random.randint(0, 3)
userAnswerCheck = 0

displayQuestion(questions[questionSelection])
turtle.onscreenclick(clickScreen)

turtle.done()
