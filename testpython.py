#print("Hello world!")
#Det er første filen
#hello


#Bonus-oppgave
import random

def get_temperature():
   
    return random.randint(15, 35)


temperature = get_temperature()
print("Temperature is:", temperature, "°C")

if temperature > 25:
    print("It's a hot day!")
else:
    print("It's a cool day.")
