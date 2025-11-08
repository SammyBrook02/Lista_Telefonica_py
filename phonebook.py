people = {
    "Samuel": "+55 83 9 8821-1709",
    "Davi": "+55 83 9 4874-8520",
    "James": "+55 83 9 7423-6549",
    "Lucas": "+55 83 9 6325-7456",
    "Carolina": "+55 21 9 7463-2085",
    "Rafael": "+55 31 9 8215-6497",
    "Juliana": "+55 41 9 9684-1520",
    "Bruno": "+55 51 9 9372-4806",
    "Fernanda": "+55 61 9 8107-2354",
    "Mariana": "+55 71 9 8863-4792",
}

name = input("name: ")

if name in people:
    print(f"Number: {people[name]}")

else:
    print("Not Found!")

