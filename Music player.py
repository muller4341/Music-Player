import os
import pygame

# Initialize pygame
pygame.init()

# Function to create a list of MP3 files in a directory
def get_mp3_files(directory):
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mp3"):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

# Function to play music
def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Main function
def main():
    music_folder = "C:\\Users\\hp\\Music\\audio\\hard work"
    mp3_files = get_mp3_files(music_folder)

    if not mp3_files:
        print("No MP3 files found in the specified folder.")
        return

    print("Available songs:")
    for i, file in enumerate(mp3_files):
        print(f"{i+1}. {os.path.basename(file)}")

    while True:
        try:
            choice = int(input("Enter the number of the song you want to play (0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(mp3_files):
                selected_song = mp3_files[choice - 1]
                print(f"Playing: {os.path.basename(selected_song)}")
                play_music(selected_song)
                pygame.mixer.music.set_endevent(pygame.USEREVENT)
                pygame.event.wait()
            else:
                print("Invalid choice. Please select a valid song or enter 0 to exit.")
        except (ValueError, KeyboardInterrupt):
            print("Invalid input. Please enter a number.")

    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()
