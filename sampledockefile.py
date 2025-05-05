name="Bhavansri"
age=25
email="bahvana@gmail.com"
skills={"Python", "docker","aws","jenkkins","sonarqube","jmeter","kubernetes"}
is_available=True
print(f"name {name}")
print(f"age {age}")
print(f"email {email}")
print(f"skills {skills}")
print(f"is_available {is_available}")
#type
print(f"name type is  {type(name)}")
print(f"age type is  {type(age)}")
print(f"email type is  {type(email)}")
print(f"skills type is  {type(skills)}")
print(f"is_available type is  {type(is_available)}")
#conversion of type
age_float=float(age)
skills_tuple=tuple(skills)
print(f"age is convert {age_float}")
print(f"skills converts{skills_tuple}")
