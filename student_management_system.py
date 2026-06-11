"""Student Management System (file-persisted)

Stores students in `students.json` with simple CRUD operations.
"""
import json
import os

DB_PATH = "students.json"


def load_students():
    if not os.path.exists(DB_PATH):
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_students(students):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)


def find_by_roll(students, roll):
    for s in students:
        if s.get("roll") == roll:
            return s
    return None


def main():
    students = load_students()
    while True:
        print("\nStudent Manager — commands: add, list, find, update, remove, quit")
        cmd = input("cmd> ").strip().lower()
        if cmd in ("q", "quit", "exit"):
            break
        if cmd == "add":
            name = input("Name: ").strip()
            roll = input("Roll #: ").strip()
            age = input("Age: ").strip()
            course = input("Course: ").strip()
            students.append({"name": name, "roll": roll, "age": age, "course": course})
            save_students(students)
            print("Added")
        elif cmd == "list":
            if not students:
                print("No students")
            for s in students:
                print(f"{s['roll']}: {s['name']} — age {s['age']} — {s['course']}")
        elif cmd == "find":
            key = input("Roll or name: ").strip()
            found = [s for s in students if s['roll'] == key or s['name'].lower() == key.lower()]
            if not found:
                print("Not found")
            for s in found:
                print(s)
        elif cmd == "update":
            roll = input("Roll #: ").strip()
            s = find_by_roll(students, roll)
            if not s:
                print("Not found")
                continue
            age = input(f"Age [{s.get('age')}]: ").strip() or s.get('age')
            course = input(f"Course [{s.get('course')}]: ").strip() or s.get('course')
            s['age'] = age
            s['course'] = course
            save_students(students)
            print("Updated")
        elif cmd == "remove":
            roll = input("Roll #: ").strip()
            before = len(students)
            students = [st for st in students if st.get('roll') != roll]
            if len(students) < before:
                save_students(students)
                print("Removed")
            else:
                print("Not found")
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
