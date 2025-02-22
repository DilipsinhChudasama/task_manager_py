Below is the complete README file for your project:

---

# Task Manager with User Authentication

A simple command-line application that allows users to register, log in, and manage their personal tasks. Each user’s tasks are stored separately, ensuring privacy and persistent storage through file handling.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [File Structure](#file-structure)
4. [Setup and Installation](#setup-and-installation)
5. [Usage Instructions](#usage-instructions)
6. [Technical Details](#technical-details)
7. [Example Workflow](#example-workflow)
8. [Possible Enhancements](#possible-enhancements)

---

## Project Overview

In today's world, keeping track of tasks in an organized manner is essential. This project implements a **Task Manager** with **user authentication**. Users can register with a unique username and password. After logging in, they can create, view, update, and delete their tasks. Passwords are stored securely using SHA-256 hashing, and each user's tasks are maintained in a separate file.

---

## Features

1. **User Registration**

   - Create an account with a unique username and password.
   - Passwords are hashed before storage for basic security.

2. **User Login**

   - Authenticate using your username and password.
   - Only registered users can access their tasks.

3. **Task Management**

   - **Add Task:** Input a description for a new task.
   - **View Tasks:** Display all tasks with their unique IDs, descriptions, and status.
   - **Mark as Completed:** Update the status of a task to "Completed".
   - **Delete Task:** Remove a task from your list.

4. **Logout**
   - Securely log out from your session, returning you to the main menu.

---

## File Structure

```
project_root/
│
├─ task_manager.py           # Main Python source code
├─ users.txt                 # Stores user credentials (username,hashed_password)
├─ tasks_<username>.txt      # Stores tasks for each user (e.g., tasks_alice.txt)
└─ README.md                 # Project documentation (this file)
```

- **`task_manager.py`**: Contains all logic for user registration, login, and task management.
- **`users.txt`**: Each line contains a username and its corresponding hashed password, separated by a comma.
- **`tasks_<username>.txt`**: Each user’s tasks are stored in a file named after their username, with each line formatted as:
  ```
  task_id|task_description|task_status
  ```

---

## Setup and Installation

1. **Prerequisites**

   - Ensure Python 3.x is installed on your system.

2. **Download or Clone**

   - Place all project files in the same directory.

3. **(Optional) Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

4. **Run the Application**
   - Open a terminal/command prompt in the project directory.
   - Execute the script:
     ```bash
     python task_manager.py
     ```

---

## Usage Instructions

1. **Starting the Application**

   - Run `task_manager.py` to see the main menu with options to Login, Register, or Exit.

2. **Registration**

   - Choose "Register" if you are a new user.
   - Enter a unique username and password.
   - The system will hash your password and store it in `users.txt`.

3. **Login**

   - Enter your credentials to log in.
   - Upon successful login, you will access the Task Manager Menu.

4. **Task Manager Menu Options**

   - **Add Task:** Input a task description.
   - **View Tasks:** Display all tasks (ID, description, and status).
   - **Mark Task as Completed:** Update the status of a selected task.
   - **Delete Task:** Remove a task from your list.
   - **Logout:** End your session and return to the login/register screen.

5. **Exiting**
   - From the main menu, choose "Exit" to close the application.

---

## Technical Details

- **File Handling:**

  - User credentials are stored in `users.txt` in the format:
    ```
    username,hashed_password
    ```
  - Each user’s tasks are stored in a file named `tasks_<username>.txt` with each line formatted as:
    ```
    task_id|task_description|task_status
    ```

- **Password Security:**

  - Uses Python's `hashlib.sha256` to hash passwords before storage, ensuring that passwords are not stored in plain text.

- **Unique Task IDs:**
  - Each task is assigned a unique numeric ID, typically by incrementing the maximum existing ID by one.

---

## Example Workflow

```
========================================
  Welcome to Task Manager
========================================
1. Login
2. Register
3. Exit
Enter your choice: 2

----- REGISTER -----
Enter a new username: alice
Enter a new password: ****
Registration successful. Please log in.

========================================
  Welcome to Task Manager
========================================
1. Login
2. Register
3. Exit
Enter your choice: 1

----- LOGIN -----
Enter username: alice
Enter password: ****
Login successful!

----- TASK MANAGER MENU -----
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Logout
Enter your choice: 1

Enter task description: Buy groceries
Task added successfully with ID 1!
```

---

## Possible Enhancements

1. **Database Integration:**

   - Consider using a database (e.g., SQLite) for better scalability and data management.

2. **Enhanced Password Security:**

   - Use libraries like `bcrypt` or `argon2` for more robust password hashing.

3. **Graphical or Web Interface:**

   - Develop a GUI or web-based version for improved usability.

4. **Task Sorting and Filtering:**
   - Add functionality to sort tasks by status or filter by keywords.

---

**Thank you for using the Task Manager with User Authentication!**  
For any questions or further support, please contact the project maintainer.

---
