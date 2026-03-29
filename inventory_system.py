# Project: Academic Enrollment System (Unit 5: Dictionaries & Lists) 
def enroll_student():
    # Unit 5: Representing compound data [cite: 17]
    course_catalog = {
        "CSE1021": {"name": "Intro to Problem Solving", "credits": 4, "req": "Nil"},
        "MAT1011": {"name": "Calculus", "credits": 4, "req": "High School Math"},
        "CSE2001": {"name": "Data Structures", "credits": 3, "req": "CSE1021"},
    
        "ENG1001": {"name": "Effective Technical Communication", "credits": 2, "req": "Nil"}}
    
    # Unit 5: Student record 
    student_history = ["High School Math"] 
    current_credits = 18 # Max limit is 21
    
    course_code = input("Enter Course Code to Register: ").upper()
    
    # Unit 3: Conditional validation 
    if course_code not in course_catalog:
        print("Error: Course code does not exist in the syllabus.")
    elif course_code in student_history:
        print("Error: You have already completed this course.")
    else:
        # Unit 3 & 5: Checking Prerequisites and Credit Limits
        required_pre = course_catalog[course_code]["req"]
        course_credits = course_catalog[course_code]["credits"]
        
        if required_pre != "Nil" and required_pre not in student_history:
            print(f"Registration Denied! You must complete {required_pre} first.")
        elif current_credits + course_credits > 21:
            print("Registration Denied! This would exceed your 21-credit limit.")
        elif course_credits >= 4:
            print(f"Success! Registered for {course_code}. Note: This is a high-credit core course.")
            current_credits += course_credits
        else:
            print(f"Success! Registered for {course_code}.")
            current_credits += course_credits

    print(f"Current Total Credits: {current_credits}")
