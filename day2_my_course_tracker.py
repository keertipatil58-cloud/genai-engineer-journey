name = input("Enter your name: ").strip()
course = input("Which course are you learning? ").strip()
topics = input("What topics have you covered so far? ").strip()

tracker = {
    "name": name,
    "course": course,
    "topics": ['data types', 'strings', topics, 'dictionaries'],
    "learning_status": True
}

print("\n----- MY COURSE TRACKER -----")
print(f"Name: {tracker['name']}")
print(f"Course: {tracker['course']}")
print(f"Topics: {tracker['topics']}")
print(f"Status: {tracker['learning_status']}")

tracker["completed_topics"] = len(tracker["topics"])

print(f"Total Topics Completed: {tracker['completed_topics']}")