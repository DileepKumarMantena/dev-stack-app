import os

def main():
    print("Select the set to execute from:")
    print("1. Set1")
    print("2. Set2")
    
    set_choice = input("Enter your set choice (1-2): ")

    # Determine the folder based on the set choice
    match set_choice:
        case "1":
            folder = "Set1"
        case "2":
            folder = "Set2"
        case "3":
            folder = "Set3"
        case _:
            print("Invalid set choice!")
            return

    base_path = "C:/Users/user/Downloads/Projects/Mine/dev-stack-app/Backend"
    folder_path = os.path.join(base_path, folder)

    # Dynamically list files named python*.py in the folder
    try:
        files = sorted([f for f in os.listdir(folder_path) if f.startswith("python") and f.endswith(".py")])
    except FileNotFoundError:
        print(f"Folder {folder_path} not found!")
        return

    if not files:
        print(f"No files found in {folder_path}!")
        return

    print("\nSelect the file to execute:")
    for i, file_name in enumerate(files, start=1):
        print(f"{i}. {file_name}")

    file_choice = input(f"Enter your file choice (1-{len(files)}): ")

    try:
        # Convert the user's choice to a valid index
        file_index = int(file_choice) - 1
        if 0 <= file_index < len(files):
            file_to_execute = os.path.join(folder_path, files[file_index])
            exec(open(file_to_execute).read())
        else:
            print("Invalid file choice!")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
