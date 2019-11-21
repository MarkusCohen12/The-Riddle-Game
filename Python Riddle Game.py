# The Riddle Game

import time

print("Welcome")
time.sleep(1.8)
print("In this game you will come across some riddles")
time.sleep(2.8)
print("difficult they are so move little by little")
time.sleep(2.9)
print("answer the questions and get through the maze")
time.sleep(2.8)
print("but be aware, if you mess up you will experience delays")
time.sleep(3.1)
print("take your time because the journey is long")
time.sleep(2.8)
print("follow the steps to choose whats right and whats wrong\n")
time.sleep(3.0)
print("LETS BEGIN \n")
time.sleep(2.7)
print("Q1) The more you take, the more you leave behind. What Am I?\n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("footsteps","steps"):
    time.sleep(1.3)
    print("    😭 Unlucky Try again 💩\n")
    time.sleep(2.7)
    print("Q1) The more you take, the more you leave behind. What Am I?\n ")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    👣 Baby steps 😪 [Score:1/10]\n")

time.sleep(3.5)
print("Q2) What has a head, a tail, is brown, and has no legs?\n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("coin","penny"):
    time.sleep(1.3)
    print("    😱 Wrong LMAO 🤭\n")
    time.sleep(2.7)
    print("Q2) What has a head, a tail, is brown, and has no legs?\n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    😉 Beginners Luck 🤨 [Score:2/10]\n")

time.sleep(3.5)
print("Q3) First you eat me, then you get eaten. What am I?\n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("fishook","a fishook","fishooks"):
    time.sleep(1.3)
    print("    🤯 Game Over 😖\n")
    time.sleep(2.7)
    print("Q3) First you eat me, then you get eaten. What am I?\n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    😎 Surprising 👏 [Score:3/10]\n")

time.sleep(3.5)
print("Q4) What belongs to you, but other people use it more than you?\n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("your name", "name"):
    time.sleep(1.3)
    print("    😤 Oh Dear 🤦‍♂️ \n")
    time.sleep(2.7)
    print("Q4) What belongs to you, but other people use it more than you?\n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    🤑 Wow Correct 🤓 [Score:4/10]\n")  

time.sleep(3.5)
print("Q5) What room do ghosts avoid?\n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("the living room", "living room"):
    time.sleep(1.3)
    print("    👎 Embarrasing 😶 \n")
    time.sleep(2.7)
    print("Q5) What room do ghosts avoid?\n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    👻 Clever Clogs 🧠 [Score:5/10]\n")

time.sleep(3.5)
print("Q6) What has many keys, but can't even open a single door?\n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("a piano", "the piano", "piano"):
    time.sleep(1.3)
    print("    😑 Dissapointing 😤 \n")
    time.sleep(2.7)
    print("Q5) What has many keys, but can't even open a single door?\n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    🤩 Nearly there 😍 [Score:6/10]\n")

time.sleep(3.5)
print("Q7) I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?\n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("fire", "a fire", "flames"):
    time.sleep(1.3)
    print("    😴 So Near Yet So Far 🔜 \n")
    time.sleep(2.7)
    print("Q7) I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?\n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    🙀 Nailed It 🔨 [Score:7/10]\n")

time.sleep(3.5)
print("Q8) You see me out and about, but i am not alive. I have a neck but no head i have two arms but no hands. What am I?\n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("t shirt", "shirt", "jumper", "hoodie", "pullover"):
    time.sleep(1.3)
    print("    😴 So Near Yet So Far 🔜 \n")
    time.sleep(2.7)
    print("Q7) You see me out and about, but i am not alive. I have a neck but no head i have two arms but no hands. What am I?\n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    🤪 Very Impressive 👕 [Score:8/10]\n")

time.sleep(3.5)
print("Q9) I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? \n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("a map", "map", "maps"):
    time.sleep(1.3)
    print("    😴 So Near Yet So Far 🔜 \n")
    time.sleep(2.7)
    print("Q8) I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? \n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    🤑 Incredible! 🤘 [Score:9/10]\n")

time.sleep(3.5)
print("Q10) I'm tall when I'm young, I'm short when I'm old. What am I? \n")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("a candle", "a pencil", "candle", "pencil"):
    time.sleep(1.3)
    print("    😴 So Near Yet So Far 🔜 \n")
    time.sleep(2.7)
    print("Q9) I'm tall when I'm young, I'm short when I'm old. What am I? \n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    🤝 Completion 💯 [Score:10/10]\n")

time.sleep(3.5)
print("Bonus Question) Every night I get told what to do and Every morning I do what im told; but i still cannot escape your scold. What am I?")
time.sleep(3.3)
answer = input("    Answer: ")
print("")
answer = answer.lower()
while answer not in ("a alarm clock", "an alarm clock", "clock", "a clock", "alarm clock"):
    time.sleep(1.3)
    print("    😴 So Near Yet So Far 🔜 \n")
    time.sleep(2.7)
    print("Q9) I'm tall when I'm young, I'm short when I'm old. What am I? \n")
    time.sleep(3.1)
    answer = input("    Answer: ")
    print("")
    answer = answer.lower()
    time.sleep(1.7)
else:
    print("    🌟 You're A God 🌟\n")




























