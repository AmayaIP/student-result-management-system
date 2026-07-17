import json
from pathlib import Path

FILE = Path("students.json")

def load_data():
  if FILE.exists():
     try:
       return json.loads(FILE.read_text())
     except json.JSONDecodeError:
       return []
  return []

def save_data(data):
    FILE.write_text(json.dumps(data,
indent=2))

def calc_grade(avg):
    if avg >= 90:
        return "A+"
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 50:
        return "D"
    return "F"

def add_student(data):
    roll = input("Enter roll number:").strip()
    name = input("Enter name: ").strip()
    m1 = float(input("Enter marks 1: "))
    m2 = float(input("Enter marks 2: "))
    m3 = float(input("Enter marks 3: "))
    total = m1 + m2 + m3
    avg = total / 3
    grade = calc_grade(avg)
    data.append({
        "roll": roll,
        "name": name,
        "marks": [m1, m2, m3],
        "total": total,
        "average": avg,
        "grade": grade
    })
    save_data(data)
    print("Student added successfully.")

def show_all(data):
    if not data:
        print("No records found.")
        return
    for s in data:
        print(f"Roll:{s['roll']},Name:{s['name']},Total:{s['total']},Avg:{s['average']:.2f},Grade:{s['grade']}")

def search_student(data):
    roll = input("Enter roll number to search: ").strip()
    for s in data:
        if s["roll"] == roll:
            print(s)
            return
    print("Student not found.")

def delete_student(data):
    roll = input("Enter roll number to delete: ").strip()
    new_data = [s for s in data if s["roll"] != roll]
    if len(new_data) == len(data):
        print("Student not found.")
        return data
    save_data(new_data)
    print("Student deleted successfully.")
    return new_data

def main():
    data = load_data()
    while True:
        print("1. Add Student")
        print("2. Show All")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice:").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            show_all(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            data = delete_student(data)
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

















        



























        












    












    









    
