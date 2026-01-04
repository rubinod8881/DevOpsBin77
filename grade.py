name=input("Enter your name:")
score=int(input("Enter your score:"))
if score>=90:
    print(f"Hello {name} your score is {score} and you have got 'A' Grade")
elif score>=75:
    print(f"Hello {name} your score is {score} and you have got 'B' Grade")
elif score>=60:
    print(f"Hello {name} your score is {score} and you have got 'C' Grade")
elif score>=50:
    print(f"Hello {name} your score is {score} and you have got 'D' Grade")
else:
    print(f"Hello {name} your score is {score} and you have Failed")