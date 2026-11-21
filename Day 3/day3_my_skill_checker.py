name = input("Enter your name: ")
language = int(input("How many programming languages do you know? "))
skills = ["Python", "Java", "C", "C++"]

if language >= 2:
    print("Good programming foundation!")
else:
    print("Keep learning programming!")

for skill in skills:
    print(skill)
print(f"\nHello, {name}!")
print(f"\nTotal skills: {len(skills)}")