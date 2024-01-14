voteCount = int(input())
votes = str(input())

aCount = votes.count("A")
bCount = votes.count("B")

if aCount > bCount:
    print("A")
elif bCount > aCount:
    print("B")
else:
    print("Tie")
