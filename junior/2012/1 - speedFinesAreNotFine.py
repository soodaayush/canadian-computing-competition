speedLimit = int(input("Enter the speed limit:"))
carSpeed = int(input("Enter the recorded speed of the car:"))

if carSpeed <= speedLimit:
    print("Congratulations, you are within the speed limit!")
elif speedLimit < carSpeed <= speedLimit + 20:
    print("You are speeding and your fine is $100.")
elif speedLimit < carSpeed <= speedLimit + 30 and carSpeed > speedLimit + 20:
    print("You are speeding and your fine is $270.")
elif carSpeed >= speedLimit + 31:
    print("You are speeding and your fine is $500.")
