#cofe mohammad

total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0

coffee = {
    "espresso" : 20000,
    "hot ch0colate" : 35000,
    "moka" : 40000,
    "late" : 50000
}

print("welcame to mohammad cofe")
print("Address: sari khzar BLVD")

switch = 0
name = input("pliz enter your name: ")
family = input("pliz enter your family: ")
phone_namber = input("pliz enter phone_namber: ")

pasword_1 = input("pliz create your pasword: ")
pasword_2 = input("pliz enter your pasword: ")
self_checkout = "notdefined"
#************************************************
for pasword in range(2):
    while pasword_1 != pasword_2:
        print("rong pasword")
        pasword_2 = input("try again")
print("your pasword is accepted")

while self_checkout != "done":
    if switch == 0:
        self_checkout = input("dear customer enter your coffee")
    else:
        self_checkout = input("pliz enter your next item")
    while self_checkout not in dict(coffee):
        if self_checkout == "done":
            break
    
    customer = int (input(f"how many {self_checkout} did you ger? "))

    if self_checkout == "espresso":
        total_1 = coffee["espresso"] * customer + total_1
        print(f"total is {total_1}")
    
    elif self_checkout == "hot ch0colate":
        total_2 = coffee["hot ch0colate"] * customer + total_2
        print(f"total is {total_2}")
    
    elif self_checkout == "moka":
        total_3 = coffee["moka"] * customer + total_3
        print(f"total is {total_3}")

    elif self_checkout == "late":
        total_4 = coffee["late"] * customer + total_4
        print(f"total is {total_4}")

    total = total_1 + total_2 + total_3 + total_4

    print("your had been enterd")
    switch=1

print (f"so your total is {total}")
