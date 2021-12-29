from os import path

def read_file_2_list(filename):
    filepath = path.join("../file_repo", filename)
    file_obj = open(filepath, "r")
    return file_obj.readlines()