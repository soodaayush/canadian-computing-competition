appleShot = int(input())
appleGoal = int(input())
appleThrow = int(input())
bananaShot = int(input())
bananaGoal = int(input())
bananaThrow = int(input())

appleScore = 3 * appleShot + 2 * appleGoal + 1 * appleThrow
bananaScore = 3 * bananaShot + 2 * bananaGoal + 1 * bananaThrow

if appleScore > bananaScore:
    print("A")
elif appleScore == bananaScore:
    print("T")
elif bananaScore > appleScore:
    print("B")
    