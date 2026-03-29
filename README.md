# University-Course-Registration-Checker
This project implements a University Course Registration and Prerequisite checker using Python. It utilizes Python data structures, specifically dictionaries for course catalogues and lists for student records—to represent compound data effectively. By applying algorithm design techniques, the system evaluates academic eligibility in real-time.
# University Course Registration & Prerequisite Checker

## 1. Overview
The **University Course Registration System** is a Python-based automation tool designed to manage student enrollments. The system validates academic eligibility based on **prerequisite completion** and **credit hour limits**.

## 2. Significance
This project applies **Computational Thinking** to solve a common administrative challenge. It matters because:
* **Accuracy**: It eliminates human error in manual transcript verification.
* **Safety**: It enforces a strict **21-credit cap** to ensure a balanced academic workload.
* **Logic Application**: It demonstrates the "Logic of Exclusion," where registration only succeeds if it passes multiple validation gates.

---

## 3. Setup and Execution

### A. Environment Setup
1.  **Install Python**: Download and install Python 3.x from [python.org](https://www.python.org/).
2.  **Verify Version**: Open your terminal and run:
    ```bash
    python --version
    ```
3.  **Editor**: Any text editor (VS Code, IDLE, or Notepad++) is compatible.

### B. Dependency Installation
* This project uses the **Python Standard Library**.
* **No external packages** (like `pip install`) are required, ensuring the program is lightweight and portable.

### C. Configuration
The system parameters are defined within the script for easy modification:
* **Course Catalog**: A dictionary containing `name`, `credits`, and `req`.
* **Credit Limit**: A variable `max_credits` set to **21**.
* **Student History**: A list of strings representing previously completed courses.

### D. Execution
1.  **Save the Script**: Save the code as `registration_checker.py`.
2.  **Run the Program**:
    ```bash
    python registration_checker.py
    ```
3.  **Interact**: Follow the on-screen prompt to enter a Course Code (e.g., `CSE1021`).

---

## 4. Logical Flow
The system follows a strict hierarchical check to ensure "Program Verification":
1.  **Existence**: Is the course in the syllabus?
2.  **Redundancy**: Has the student already passed this course?
3.  **Prerequisites**: Does the student have the required background?
4.  **Capacity**: Will this exceed the 21-credit limit?

---

