#print("Hello world!")
#Det er første filen
#hello


#Bonus-oppgave
import os
import random

def get_temprature():

temp_str = os.popen("vcgencmd measure_temp").readline()

if "temp=" in temp_str:
    temp = temp_str.replace("temp=", "").replace("'C\n","") 
    return float(temp)
else
    return random.randint(15, 35)

temprature = get_temprature()
print("Temprature is:", temprature, "°C")

if temprature > 25:
    print("Its a hot day!")
else:
    print("Its a cool day.")