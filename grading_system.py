import numpy as np
import os

# --- TOPIC: OOPS (Class and Object) ---
class Student:
    def __init__(self, name, roll_no, marks_list):
        # --- TOPIC: Variable and Input (Stored in object) ---
        self.name = name
        self.roll_no = roll_no
        # --- TOPIC: Array vs List ---
        # We take a standard Python LIST of marks, but convert it to a NUMPY ARRAY for calculation
        self.marks = np.array(marks_list) 
        
    def calculate_stats(self):
        # --- TOPIC: NumPy Introduction (Basic aggregations) ---
        total = np.sum(self.marks)
        average = np.mean(self.marks)
        return total, average

    def get_status(self):
        # --- TOPIC: Conditional Statements ---
        _, avg = self.calculate_stats()
        if avg >= 40:
            return "Pass"
        else:
            return "Fail"

# --- TOPIC: Function Argument and Return ---
def save_to_file(student_list):
    # --- TOPIC: File Handling (Write Mode) ---
    try:
        with open("student_data.txt", "w") as f:
            f.write("Name,RollNo,Total,Average,Status\n") # Header
            for s in student_list:
                total, avg = s.calculate_stats()
                status = s.get_status()
                f.write(f"{s.name},{s.roll_no},{total},{avg:.2f},{status}\n")
        print("\n[Success] Data saved to 'student_data.txt'")
    except Exception as e:
        print(f"[Error] Could not save file: {e}")

def main():
    students = []
    
    # --- TOPIC: While Loop ---
    while True:
        print("\n--- MENU ---")
        print("1. Add Student")
        print("2. Generate Analytics (Map/Filter/Lambda)")
        print("3. Save & Exit")
        
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            try:
                name = input("Enter Name: ")
                roll = input("Enter Roll No: ")
                
                # --- TOPIC: Data Types (List comprehension for input) ---
                print("Enter marks for 3 subjects separated by space (e.g., 80 90 75):")
                marks_input = input().split()
                
                # --- TOPIC: Operators (Validation) ---
                if len(marks_input) != 3:
                    print("Error: Please enter exactly 3 marks.")
                    # --- TOPIC: Break and Continue ---
                    continue 
                
                # Convert strings to floats
                marks_list = [float(x) for x in marks_input]
                
                # Create Object
                s_obj = Student(name, roll, marks_list)
                students.append(s_obj)
                print("Student added successfully!")
                
            except ValueError:
                print("Invalid input! Please enter numbers for marks.")

        elif choice == '2':
            if not students:
                print("No data available.")
                continue

            print("\n--- CLASS ANALYTICS ---")
            
            # --- TOPIC: Lambda Function & Map ---
            # Extract all averages using map and lambda
            all_averages = list(map(lambda s: s.calculate_stats()[1], students))
            
            # --- TOPIC: NumPy (Statistical Analysis) ---
            np_avgs = np.array(all_averages)
            print(f"Class Average: {np.mean(np_avgs):.2f}")
            print(f"Highest Score: {np.max(np_avgs):.2f}")
            
            # --- TOPIC: Filter ---
            # Filter students who passed (Average >= 40)
            passed_students = list(filter(lambda s: s.get_status() == "Pass", students))
            print(f"Total Passed: {len(passed_students)}")
            print(f"Total Failed: {len(students) - len(passed_students)}")

        elif choice == '3':
            save_to_file(students)
            print("Exiting program...")
            break # Breaks the while loop
            
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()