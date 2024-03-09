import os
import shutil
import sys
 
def copy_file(copy_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    for item in os.listdir(copy_dir):
        items = os.path.join(copy_dir, item)
        copied_path = os.path.join(destination_dir, item)
        if os.path.isdir(items):
            copy_file(items, copied_path)
        else:
            files = os.path.splitext(item)[1]
            dotdir = os.path.join(destination_dir, files[1:])
            if not os.path.exists(dotdir):
                os.makedirs(dotdir)
            shutil.copy(items, dotdir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py source_directory [destination_directory]")
        sys.exit(1)
    source = sys.argv[1]
    wh_copied = "dist" if len(sys.argv) < 3 else sys.argv[2]

    try:
        copy_file(source, wh_copied)
        print("Files copied successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
