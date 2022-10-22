import random

def GameWin(Computer, You):
    if Computer == You:
        return None

    elif Computer == 'R':
        if You == 'P':
            return True
        elif You == 'S':
            return False

    elif Computer == 'P':
        if You == 'S':
            return True
        elif You == 'R':
            return False

    elif Computer == 'S':
        if You == 'R':
            return True
        elif You == 'P':
            return False

with open('Score', 'r') as s:
    dataScore = int(s.read())

print(f"Your Total Score Is {dataScore}")

username = input("Write Your Name :\n")

print("\t\tGame Started \n") 
print("Computer Turn :\n\t Rock(R) Paper(P) Scissor(S)\n")

RandomNo = random.randint(1, 3)
if RandomNo == 1:
    Computer = 'R'
elif RandomNo == 2:
    Computer = 'P'
elif RandomNo == 3:
    Computer = 'S'  

You = input(f"{username} Turn :\n\t Rock(R) Paper(P) Scissor(S)\n")
print (f"---Computer Chosed ({Computer}) ^_____^ {username} You Chosed ({You})---\n")

a = GameWin (Computer, You)
if a == None:
    print(f"---{username} Unfortunately You Both Lose ✍️ ( ◔ ◡ ◔ )---\n")
elif a == True:
    print(f"---{username} You Won  ( ● ' ◡ ' ● ) CONGRATULATIONS---\n")
elif a == False:
    print (f"--- {username} You lose Unfortunately Computer Won ヾ ( ≧ へ ≦ ) 〃 ---\n")

if a == True:
    dataScore = dataScore + 1
    savedScore = str(dataScore)
    with open('Score', 'w') as f:
        f.write(savedScore)
    print(f"Your New Score is {savedScore} ( ﾉ * ･ ω ･ ) ﾉ")
else:
    None

print(f"\n\n\n\n\n{username} Your Score Will Automatically Save  ( ► __ ◄ )")