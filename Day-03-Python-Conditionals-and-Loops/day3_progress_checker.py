name = input("Enter your name: ")

topics = ["Data Types", "Strings", "Lists", "Dictionaries"]

completed_topics = int(input("How many topics have you completed? "))

if completed_topics == 4:
    print("Excellent! You completed all topics.")

elif completed_topics >= 2:
    print("Good progress! Keep learning.")

else:
    print("Keep practising. You can do it!")

print("\n----- LEARNING PROGRESS -----")

for topic in topics:
    print(topic)

print("\nTotal topics:", len(topics))
print("Completed topics:", completed_topics)