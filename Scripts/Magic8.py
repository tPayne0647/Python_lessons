import random

name = input("What is your name?: ")
question = input("What is your question?: ")

while not question:
    question = input("What is your question!?")
    
answer = ""
random_number = random.randint(1, 9)


if random_number == 1:
  answer = "Yes - definitely!"

elif random_number == 2:
  answer = "It is decidedly so..."

elif random_number == 3:
  answer = "Without a doubt!"

elif random_number == 4:
  answer = "Reply hazy, try again..."

elif random_number == 5:
  answer = "Ask again later..."

elif random_number == 6:
  answer = "Better not tell you now."

elif random_number == 7:
  answer = "Sorry " + name + ", My sources say no."

elif random_number == 8:
  answer = "Sorry " + name + ", Outlook not so good..."

elif random_number == 9:
  answer = "Sorry " + name + ", Very doubtful..."
else:
  print("Error!!!")


eight_ball = """ 
      ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        '''''........                   
      """


if question == "":
    print(eight_ball)
    print("No question asked...")
    
else:
    if name == "":
        print(eight_ball)
        print(question)
    else:
        print(eight_ball)
        print(name + " asks: " + '"' + question + '"')
print("*******************************************************************************")
print("Magic 8-Ball's answer: " + answer)