import os
import shutil

def organize_files_by_type(source_dir, dest_dir):
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        file_extension = filename.split('.')[-1]
        
        # Create a folder for each file type if it doesn't exist
        type_folder = os.path.join(dest_dir, file_extension)
        if not os.path.exists(type_folder):
            os.makedirs(type_folder)
        
        # Move the file to the corresponding folder
        shutil.move(file_path, os.path.join(type_folder, filename))
        print(f'Moved: {filename} to {type_folder}')

def main():
    source_dir = input("Enter the path of the source directory: ")
    dest_dir = input("Enter the path of the destination directory: ")
    
    # Organize files
    organize_files_by_type(source_dir, dest_dir)
    print("File organization complete.")

if __name__ == "__main__":
    main()
