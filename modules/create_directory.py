from os import getcwd, path, mkdir, chdir
from time import sleep

def create_directory(school):    
    cwd = getcwd()
    dir_school = cwd + '/' + school
    if not path.exists(dir_school) and cwd != dir_school:
        mkdir(school)
        sleep(1)
        chdir(school)
    else:
        chdir(school)
    return