# You are building a program to help a user decide what to wear based on the current 
# weather conditions. Write a Python program that prompts the user to enter the current
#  temperature in Fahrenheit and whether it is currently raining or not (as a boolean value), 
#  and then suggests an appropriate outfit based on the following criteria:

# If the temperature is less than 50 degrees Fahrenheit, suggest wearing a coat, hat,
#  scarf, and gloves. If the temperature is between 50 and 70 degrees Fahrenheit and it 
#  is not raining, suggest wearing a sweater or light jacket. If the temperature is between 
#  50 and 70 degrees Fahrenheit and it is raining, suggest wearing a rain jacket and boots. 
#  If the temperature is above 70 degrees Fahrenheit and it is not raining, suggest wearing a t-shirt and shorts.
#  If the temperature is above 70 degrees Fahrenheit and it is raining, suggest wearing a light jacket and rain boots.


def get_temperature():

    temp = float(input("What is todays temperature?: "))
    querry = input("Is it raining?")

    if temp < 50:
        print("suggest yo wear a coat, hat,scarf and gloves")
    elif temp >= 50 and temp <= 70 and querry != "True":
        print("suggest you wear a sweater or light jacket. It's not rainning")
    elif temp >= 50 and temp <= 70 and querry == "True":
        print("suggest wearing a rain jacket and boots")
    elif temp > 70 and querry != "True":
        print("suggest you wear a thirt and shorts")
    elif temp > 70 and querry == "True":
        print("suggest wearing a light jacket and rain boots")

get_temperature()
