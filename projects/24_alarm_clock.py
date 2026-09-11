import time
import datetime
import pygame

def alarm_clock(set_alarm):
    print(f"Alarm time set for {set_alarm}")
    sound_file = r"C:\Users\Dell\Desktop\arunangshubanerjee-live-football-match-stadium-crowd-cheering-563439.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == set_alarm:
            print("WAKE UP! ⏰")
            
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

    
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False

        time.sleep(1)  

if __name__ == "__main__":
    set_alarm = input("Enter your time (HH:MM:SS): ")
    alarm_clock(set_alarm)

