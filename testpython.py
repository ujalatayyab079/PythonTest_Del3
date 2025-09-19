#print("Hello world!")
#Det er første filen
#hello


#Bonus-oppgave
#Tempratur
#import random

#def get_temperature():
   
    #return random.randint(15, 35)


#temperature = get_temperature()
#print("Temperature is:", temperature, "°C")

#if temperature > 25:
    #print("It's a hot day!")
#else:
    #print("It's a cool day.")


#Pustil-Systeminformasjon
import pustil
import time

temps = pustil.sensors_tempratures()

if tems:
    for name, entries in temps.items():
        for entry in entries:
            print(f"{name} - {entry.label or 'CPU'}: {entry.current}°C")

else:
    print("Tempraturdata ikke tilgjengelig på dette systemet.")


uptime_seconds = time.time() - psutil.boot_time()
uptime_hours = int(uptime_seconds // 3600)
uptime_minutes = int((uptime_seconds % 3600) // 60)
print("System har vært oppe i:", uptime_hours,"timer og", uptime_minutes, "minutter")
