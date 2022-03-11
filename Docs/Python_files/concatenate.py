import os

actual_dir = os.getcwd()
actual_dir = str(actual_dir)

dirs = os.listdir()

paths = [os.path.join(actual_dir, dir) for dir in dirs]

list = zip(dirs, paths)

for dir, path in list:
    os.chdir(path)
    f = open('./TOTENERGY.OUT','r')
    lines = f.readlines()
    print(dir, lines[-1])