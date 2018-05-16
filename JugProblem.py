class Jug:
    capacity = 0
    level = 0

jug1 = Jug()
jug2 = Jug()

jug1.capacity = 9
jug2.capacity = 5
jug1.level = 0
jug2.level = 0

########################################
# Fill Jug1 1
# Returns remaing fill amount
def fillJug1(amount):
    beforeLevel = jug1.level
    
    if (jug1.level + amount ) >= jug1.capacity:
        print("jug2 is full\n")
        jug1.level = jug1.capacity
    else:
        jug1.level +=  amount
    
    remainingFillAmount = amount - (jug1.level - beforeLevel)
        
    print ("jug1 currently holds " + str(jug1.level) + " litres\n")
    return remainingFillAmount

########################################
def amountLeftInJug1():
    return jug1.level

########################################
# Fill Jug1 2
# Returns remaing fill amount
def fillJug2(amount):
    beforeLevel = jug2.level
    
    if (jug2.level + amount ) >= jug2.capacity:
        print("jug2 is full\n")
        jug2.level = jug2.capacity
    else:
        jug2.level +=  amount
    
    remainingFillAmount = amount - (jug2.level - beforeLevel)
        
    print ("jug2 currently holds " + str(jug2.level) + " litres\n")
    return remainingFillAmount

########################################
def amountLeftInJug2():
    return jug2.level

########################################
def pourFromJug1ToJug2(amount):
    print ("Pouring\n")
    if amount > amountLeftInJug1():
        print ("Insufficent water in Jug1\n")
        return

    remainingAmount = fillJug2(amount)
    jug1.level = jug1.level - remainingAmount


########################################
def pourFromJug2ToJug1(amount):
    print ("Pouring\n")
    if amount > amountLeftInJug2():
        print ("Insufficent water in Jug1\n")
        return

    remainingAmount = fillJug1(amount)
    jug2.level = jug2.level - remainingAmount


########################################
def initialise():
    jug1.level = 0
    jug2.level = 0


print ("The Jug Problem\n")

initialise()
remaining = fillJug2(5)
print ("Amount remaining from fill amount = " + str(remaining) + " litres\n")

pourFromJug2ToJug1(5)

print ("Amount left in Jug 1 = " + str(amountLeftInJug1()) + " litres\n")
print ("Amount left in Jug 2 = " + str(amountLeftInJug2()) + " litres\n")


remaining = fillJug2(5)
print ("Amount remaining from fill amount = " + str(remaining) + " litres\n")

pourFromJug2ToJug1(5)

print ("Amount left in Jug 1 = " + str(amountLeftInJug1()) + " litres\n")
print ("Amount left in Jug 2 = " + str(amountLeftInJug2()) + " litres\n")

