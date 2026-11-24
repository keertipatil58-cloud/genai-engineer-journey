
# GenAI Learner Profile

# Step 1: Get information from the user
name = input("Enter your name: ").strip()
language = input("Which programming language do you know? ").strip()
goal = input("What is your career goal? ").strip()

# Step 2: Store skills in a list
skills = ["Python", language, "Git"]

# Step 3: Store profile information in a dictionary
profile = {
    "name": name,
    "degree": "BE CSE",
    "skills": skills,
    "career_goal": goal,
    "learning_genai": True
}

# Step 4: Display the profile
print("\n----- GENAI LEARNER PROFILE -----")

print(f"Name: {profile['name']}")
print(f"Degree: {profile['degree']}")
print(f"Skills: {profile['skills']}")
print(f"Career Goal: {profile['career_goal']}")
print(f"Learning GenAI: {profile['learning_genai']}")

# Step 5: Add one more skill
profile["skills"].append("Prompt Engineering")

print("\nUpdated Skills:", profile["skills"])
