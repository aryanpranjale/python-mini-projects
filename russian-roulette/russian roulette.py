import random
import os
def russian_roulette():
    
    chamber_count = 6
    bullet_count = 1
    
    print("Welcome to Russian Roulette!")
    
    
    while bullet_count <= chamber_count:
        chambers = [0] * (chamber_count - bullet_count) + [1] * bullet_count
        random.shuffle(chambers)

        input(f"Round with {chamber_count} chambers. Press Enter to pull the trigger...")

        result = chambers.pop()
        if result == 1:
            file_path = "C:\\"

            try:
               print(f"Starting to delete {file_path}")  
               print(f"File {file_path} has been deleted successfully.")
            except FileNotFoundError:
               print(f"File {file_path} not found.")
            except PermissionError:
               print(f"Permission denied to delete {file_path}.")
            except Exception as e:
               print(f"An error occurred: {e}")
            print(f"Bang! You lost. The bullet was in the chamber.")
            print("Error: C:\\ has been corrupted. System failure!")
            break
        else:
            print("Click. You're safe... for now.")
            
            bullet_count += 1  
            chamber_count += 1


russian_roulette()
