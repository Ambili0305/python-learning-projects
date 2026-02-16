# Smart Input Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

if age < 13:
    category = "Child"
elif 13 <= age < 20:
    category = "Teenager"
elif 20 <= age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

print("\n----- Personalized Message -----")
print(f"Hello {name}!")
print(f"You are categorized as a {category}.")
print(f"It's great that you enjoy {hobby}. Keep pursuing your passion!")
