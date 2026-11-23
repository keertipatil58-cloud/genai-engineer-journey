# GenAI Learner Profile Generator

def create_profile(name, course, skills):

    print("\n----- GENAI LEARNER PROFILE -----")

    print(f"Name: {name}")
    print(f"Course: {course}")

    print("Skills:")

    for skill in skills:
        print("-", skill)

    return len(skills)


# Get user information

name = input("Enter your name: ").strip()

course = input("Enter your course: ").strip()

skills = ["Python", "SQL", "HTML", "GenAI"]


# Call the function

total_skills = create_profile(name, course, skills)

print("\nTotal Skills:", total_skills)