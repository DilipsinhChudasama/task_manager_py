import os
import hashlib

USERS_FILE = "users.txt"

def hash_password(password: str) -> str:
    """
    Returns the SHA-256 hash of the given password string.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """
    Registers a new user by adding their username and hashed password
    to USERS_FILE. Checks for duplicate usernames.
    """
    print("\n----- REGISTER -----")
    username = input("Enter a new username: ").strip()
    password = input("Enter a new password: ").strip()

    # Check if user already exists
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                existing_user, _ = line.strip().split(",")
                if existing_user == username:
                    print("Username already exists. Please try logging in or choose another username.")
                    return

    # Hash the password
    hashed = hash_password(password)

    # Append to users file
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{hashed}\n")

    print("Registration successful. Please log in.")

def login_user():
    """
    Prompts for username and password, checks against the stored hashed
    password in USERS_FILE. Returns the username on successful login, or None if failed.
    """
    print("\n----- LOGIN -----")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    hashed_input = hash_password(password)

    if not os.path.exists(USERS_FILE):
        print("No users registered yet. Please register first.")
        return None

    with open(USERS_FILE, "r") as f:
        for line in f:
            stored_user, stored_hash = line.strip().split(",")
            if stored_user == username and stored_hash == hashed_input:
                print("Login successful!")
                return username

    print("Invalid username or password.")
    return None

def get_tasks_file(username: str) -> str:
    """
    Returns the filename that stores tasks for a given username.
    Example: tasks_<username>.txt
    """
    return f"tasks_{username}.txt"

def load_tasks(username: str) -> list:
    """
    Loads tasks from the user's tasks file and returns a list of tuples (id, description, status).
    """
    tasks_filename = get_tasks_file(username)
    tasks = []
    if os.path.exists(tasks_filename):
        with open(tasks_filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) == 3:
                    task_id, description, status = parts
                    tasks.append((task_id, description, status))
    return tasks

def save_tasks(username: str, tasks: list):
    """
    Saves the given list of tasks (tuples) to the user's tasks file.
    Each line: id|description|status
    """
    tasks_filename = get_tasks_file(username)
    with open(tasks_filename, "w") as f:
        for t in tasks:
            f.write("|".join(t) + "\n")

def generate_task_id(tasks: list) -> str:
    """
    Generates a new numeric task ID based on existing tasks.
    For simplicity, use the max ID + 1 approach.
    """
    if not tasks:
        return "1"
    else:
        # Extract IDs and convert to int
        existing_ids = [int(t[0]) for t in tasks]
        return str(max(existing_ids) + 1)

def add_task(username: str):
    """
    Adds a new task for the logged-in user.
    """
    tasks = load_tasks(username)
    description = input("Enter task description: ").strip()
    task_id = generate_task_id(tasks)
    status = "Pending"
    tasks.append((task_id, description, status))
    save_tasks(username, tasks)
    print(f"Task added successfully with ID {task_id}!")

def view_tasks(username: str):
    """
    Displays all tasks for the logged-in user.
    """
    tasks = load_tasks(username)
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print("\n----- VIEW TASKS -----")
    print("ID | Description               | Status")
    print("----------------------------------------")
    for t in tasks:
        task_id, description, status = t
        print(f"{task_id:2} | {description:25} | {status}")
    print()

def mark_task_completed(username: str):
    """
    Marks a task as completed based on the user-inputted task ID.
    """
    tasks = load_tasks(username)
    if not tasks:
        print("No tasks to update.")
        return

    task_id = input("Enter the Task ID to mark completed: ").strip()
    updated = False

    for i, t in enumerate(tasks):
        if t[0] == task_id:
            tasks[i] = (t[0], t[1], "Completed")
            updated = True
            break

    if updated:
        save_tasks(username, tasks)
        print("Task marked as completed!")
    else:
        print("Task ID not found.")

def delete_task(username: str):
    """
    Deletes a task based on the user-inputted task ID.
    """
    tasks = load_tasks(username)
    if not tasks:
        print("No tasks to delete.")
        return

    task_id = input("Enter the Task ID to delete: ").strip()
    new_tasks = [t for t in tasks if t[0] != task_id]

    if len(new_tasks) == len(tasks):
        print("Task ID not found.")
    else:
        save_tasks(username, new_tasks)
        print("Task deleted successfully.")

def main_menu(username: str):
    """
    Displays the main task manager menu for the logged-in user.
    """
    while True:
        print("\n----- TASK MANAGER MENU -----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Logout")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(username)
        elif choice == "2":
            view_tasks(username)
        elif choice == "3":
            mark_task_completed(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\n========================================")
        print("  Welcome to Task Manager")
        print("========================================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            username = login_user()
            if username:
                main_menu(username)
        elif choice == "2":
            register_user()
        elif choice == "3":
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
