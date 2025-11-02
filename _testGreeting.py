import os
import time


def main():
    # Define folder and file paths
    folder_name = "Greet Folder"
    file_name = "greeting.txt"
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_path = os.path.join(folder_path, file_name)

    # Create folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    ### Loop used for Request/Response to greeting.py
    while True:
        # Ask user for name
        name = input("\nEnter your name (or type 'STOP' to quit): ").strip()

        if name.upper() == "STOP":
            print("\nExiting...")
            break

        # Write name to file
        with open(file_path, "w", encoding="utf-8") as file:
            print(f"Writing this name to greeting.txt:\n{name}\n")
            file.write(name)

        # Wait 1 second
        time.sleep(1)

        # Read and print contents of file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        print(f"greeting.txt now says: \n{content}\n")

if __name__ == "__main__":
    main()
