name = input("Enter your name: ")
topic = input("What did you learn today? ")
learning = input("What did you understand? ")

with open("learning_journal.txt", "a") as file:
    file.write(f"\nName: {name}\n")
    file.write(f"Topic: {topic}\n")
    file.write(f"What I learned: {learning}\n")

print("\nYour learning journal is saved!")

with open("learning_journal.txt", "r") as file:
    print("\n----- MY LEARNING JOURNAL -----")
    print(file.read())