import os
import shutil

def mkdir(path=None):
    if path == None:
        print("no path for mkdir")
        exit(1)
    os.makedirs(path, exist_ok=True)
    print(f"directory created successfully: {path}")

def clean(path=None):
    if path ==None:
        print("No path for clean")
        exit(1)
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"clean success: {path}")
    else:
        print(f"clean path is not valid:{path}")