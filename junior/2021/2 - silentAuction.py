bidders = int(input())

biddingSet = set()
biddersArr = []
winner = ""

for i in range(bidders):
    name = input()
    bidding = int(input())
    biddingSet.add(bidding)
    biddersArr.append([name, bidding])

winningNumber = max(biddingSet)

for i in biddersArr:
    if i[1] == winningNumber:
        winner = i[0]
        break

print(winner)


