def get_grade(marks):
    """Return grade based on marks."""
    if 90 <= marks <= 100:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    elif 0 <= marks < 50:
        return "F"
    else:
        return None  # Invalid marks

def main():
    print("=== Student Grading System ===")
    while True:
        name = input("Enter student name: ").strip()
        
        
        try:
            marks = int(input("Enter marks (0-100): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue
        
        grade = get_grade(marks)
        if grade is None:
            print("❌ Marks must be between 0 and 100.")
        else:
            print(f"✅ {name} scored {marks} and received grade: {grade}")
        
        
        choice = input("Do you want to enter another student? (y/n): ").lower()
        if choice != 'y':
            print("🎓 Grading system closed. Goodbye!")
            break

if __name__ == "__main__":
    main()
