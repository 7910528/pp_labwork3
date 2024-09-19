import os
import pickle

def replace_substring_in_file(file_path, old_substring, new_substring):
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        modified_lines = [line.replace(old_substring, new_substring) for line in lines]
        
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)
        
        print(f"Substrings replaced successfully in '{file_path}'.")
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IOError as io_error:
        print(f"An IOError occurred: {io_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    file_path = input("Enter the path of the text file: ") # D:\учёба\III курс I семестр\PP\Laboratory Work 3\text.txt
    old_substring = input("Enter the substring to replace: ")
    new_substring = input("Enter the new substring: ")
    
    replace_substring_in_file(file_path, old_substring, new_substring)
    
    operation_data = {
        "file_path": file_path,
        "old_substring": old_substring,
        "new_substring": new_substring
    }

    try:
        with open('last_operation.pkl', 'wb') as pickle_file:
            pickle.dump(operation_data, pickle_file)
        print("Operation details saved successfully using pickle.")
    except IOError as io_error:
        print(f"Could not save operation details: {io_error}")

if __name__ == "__main__":
    main()
