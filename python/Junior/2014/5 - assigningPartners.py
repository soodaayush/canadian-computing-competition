partnerCount = int(input())
partnerList1 = input().split(" ")
partnerList2 = input().split(" ")

partnerDict = {}

goodOrBad = True

for i in range(partnerCount):
    person1 = partnerList1[i]
    person2 = partnerList2[i]

    if person1 == person2:
        goodOrBad = False
    if person1 in partnerDict and partnerDict[person1] != person2:
        goodOrBad = False

    partnerDict[person1] = person2
    partnerDict[person2] = person1

if goodOrBad:
    print("good")
else:
    print("bad")
