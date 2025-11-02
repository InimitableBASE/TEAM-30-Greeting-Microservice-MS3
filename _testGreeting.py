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


    # ### TEST CASES
    # # Test Cases for Time of Day
    # date = datetime.now()
    # yr = date.year
    # month = date.month
    # day = date.day



    # print(f"\nTESTING 4:59 AM WITH NAME: BUGS BUNNY:")
    # hr = 4
    # min = 59
    # fake_now = datetime(yr, month, day, hr, min, 0)
    # with patch("greeting.datetime") as mock_datetime:
    #     # Make datetime.now() return our fake time
    #     mock_datetime.now.return_value = fake_now
    #     # Let datetime.strftime still behave normally
    #     mock_datetime.strftime = datetime.strftime
    #     print(build_greeting("First Last"))

    # # Test Cases for Holidays
    # print(f"\nTESTING CHRISTMAS MORNING AT 8:30 AM WITH NAME: BUGS BUNNY:")
    # fake_now = datetime(2025, 12, 25, 8, 30, 0)
    # with patch("greeting.datetime") as mock_datetime:
    #     # Make datetime.now() return our fake time
    #     mock_datetime.now.return_value = fake_now
    #     # Let datetime.strftime still behave normally
    #     mock_datetime.strftime = datetime.strftime
    #     print(build_greeting("First Last"))




if __name__ == "__main__":
    main()
