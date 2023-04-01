import time 
from playsound import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
print(CLEAR)


print("Enter a number by this input format 00:00")
given_time = input("Enter here: ")

given_time_listed = given_time.split(":")
if len(given_time_listed) != 2:
    print("Please use the given format!")
    exit()

min, sec = given_time_listed

try:
    min = int(min)
    sec = int(sec)
except:
    print(CLEAR, "Wrong input. Pleases use numbers!")
    exit()
    
total_time = min * 60 + sec
min = total_time // 60
sec = total_time - (min*60)

while total_time>=0:
    print(CLEAR_AND_RETURN, f"Will ring in {min:02d}:{sec:02d}")
    total_time -= 1
    min = total_time // 60
    sec = total_time - (min*60)
    time.sleep(1)
    
playsound("Cradles.mp3")