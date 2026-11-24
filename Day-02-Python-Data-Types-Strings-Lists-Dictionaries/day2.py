#python program to demonstrate the use of different data types
name = "Keerti"
age = 21
cgpa = 8.7
is_learning_genai = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_learning_genai))



#python program to demonstrate the use of python strings
message = "Welcome to GenAI Engineering"
print(message.upper())
print(message.lower())
print(len(message))


#python program to demonstrate the use of python lists
skills = ["Python", "SQL", "HTML", "Git"]
print(skills)
print(skills[0])
print(skills[1])
print(skills[2])
print(skills[3])
skills.append("GenAI")
print(skills)

#python program to demonstrate the use of python dictionaries
student = {   
    "name": "Keerti",
    "degree": "BE CSE",
    "cgpa": 8.7,
}
print(student)
print(student["name"])
print(student["degree"])
print(student["cgpa"])
student["goal"] = "GenAI Engineer"
print(student)
