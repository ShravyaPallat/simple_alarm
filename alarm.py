import time
import os
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# ANSI escape sequences for clearing the screen and returning the cursor to the home position
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds, sound_file):
    # Initialize the time elapsed
    time_elapsed = 0
    # Clear the screen
    print(CLEAR)
    # Loop until the elapsed time equals the total time (in seconds)
    while time_elapsed < seconds:
        # Wait for 1 second
        time.sleep(1)
        # Increment the time elapsed by 1 second
        time_elapsed += 1
        # Calculate the remaining time
        time_left = seconds - time_elapsed
        # Calculate the remaining hours, minutes, and seconds
        hours_left = time_left // 3600
        minutes_left = (time_left % 3600) // 60
        seconds_left = time_left % 60
        
        # Print the remaining time in HH:MM:SS format, clearing and returning the cursor each second
        print(f"{CLEAR_AND_RETURN}{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}")
    
    # Play the alarm sound when the time is up
    print("Time's up! The alarm is ringing.")
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Play the sound in a loop
    while True:
        # Prompt the user to turn off the alarm
        status = int(input("Enter 1 to turn off the alarm: "))
        if status == 1:
            pygame.mixer.music.stop()
            break

# List of available Windows alarm sounds
windows_media_path = os.path.join(os.environ['WINDIR'], 'Media')
alarm_sounds = {
    "1": os.path.join(windows_media_path, "Alarm01.wav"),
    "2": os.path.join(windows_media_path, "Alarm02.wav"),
    "3": os.path.join(windows_media_path, "Alarm03.wav")
}

# Display the available alarm sounds
print("Select an alarm sound: ")
for key, value in alarm_sounds.items():
    print(f"{key}: {value}")

# Get user selection for the alarm sound
sound_choice = input("Enter the number of the alarm sound you want to use: ")

# Validate the user's choice
while sound_choice not in alarm_sounds:
    print("Invalid choice. Please select a valid alarm sound.")
    sound_choice = input("Enter the number of the alarm sound you want to use: ")

# Get user input for the number of hours, minutes, and seconds to wait
hours = int(input("How many hours to wait: "))
minutes = int(input("How many minutes to wait: ")) 
seconds = int(input("How many seconds to wait: ")) 

# Calculate the total time in seconds
total_seconds = hours * 3600 + minutes * 60 + seconds      

# Call the alarm function with the total time and selected sound
alarm(total_seconds, alarm_sounds[sound_choice])
