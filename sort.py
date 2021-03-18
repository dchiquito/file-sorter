# Run me like this:
# python sort.py /path/to/files /path/to/sort/root

import os
import shutil
import sys


def sort_files(src, dest):
    # https://docs.python.org/3/library/os.html?highlight=os#os.listdir
    for f in os.listdir(src):
        # https://docs.python.org/3/library/os.path.html#os.path.splitext
        # https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
        _, dotted_extension = os.path.splitext(f)
        # Trim off the dot
        # https://stackoverflow.com/questions/509211/understanding-slice-notation
        extension = dotted_extension[1:]

        # This is the directory all files with that extension will go into
        # https://docs.python.org/3/library/os.path.html#os.path.join
        dest_dir = os.path.join(dest, extension)
        # If it doesn't exist yet, create it
        # https://docs.python.org/3/library/os.html?highlight=os#os.makedirs
        os.makedirs(dest_dir, exist_ok=True)

        full_source_path = os.path.join(src, f)
        full_dest_path = os.path.join(dest, extension, f)
        # Copy the file
        # https://docs.python.org/3/library/shutil.html#shutil.copy2
        shutil.copy2(full_source_path, full_dest_path)


if __name__ == "__main__":
    # https://docs.python.org/3/library/sys.html#sys.argv
    if len(sys.argv) != 3:
        print("Two arguments required, fool")
        sys.exit(0)

    src = sys.argv[1]
    dest = sys.argv[2]

    sort_files(src, dest)
