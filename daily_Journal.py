import os
from datetime import datetime

def save():
    date=datetime.now().strftime("%Y-%M-%D")
    filename=f"{date}.txt"

user=input(f"Enter the daily journal entry  for {date}:")

with open("filename","a") as file:
    file.write(f"{ datetime.now().strftime("%Y-%M-%D,%H:%M:%s")}")
    file.write(user)

print("Journal Entry Saved in {filename}.")


def list():
    files=[f for filee in list]
    if not files:
        print("No Entry found.")
    else:
        print("Available Journal Entry.")
        for i in file in enumerate(sorted(files)):
            print(f"{i+1}.file")
            return files
        

def read(): #Allow user to select and read previous journal entry
    files=list()
    if not files:
        return
    


choice = int(input("Enter the number of Journal entry you want to read:"))
if 1<=choice<=len(files):
    filename=files[choice-1]
    with open(filename,"r") as file:
        print(f"\nJournal entry for {filename[:-4]}:\n")
        print(file.read)
else:
   print("Invalid Section")




   def main():
    """Main program loop to handle user interaction."""
    while True:
        print("\n1. Create a new journal entry")
        print("2. Read a previous journal entry")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice=='1':
            save()
        elif choice=='2':
            read()
        elif choice=='3':
            print("Byee")
        else:
            print("Invalid choices!")


            
if __name__ == "__main__":
    main()



  
    


