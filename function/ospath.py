import os
b = os.path.abspath("test/") #direct file name/ dir name
# print(path.dirname(b)) #get path to direct dir/ file
# print(path.basename(b)) #get name of direct dir/ file
"""Can use path.split(b) to get preceed path and dir/file name at the same time"""
# # print(os.path.exists(a))
print(os.path.exists(b)) #check if b exist
print(os.path.isdir(b)) #check if dir
print(os.path.isfile(b)) #check if file
# print(path.getsize(b)) #get the file size
# """Raise os.error if file does not exist or is inaccessible"""
# print(path.getatime(b)) #access time
# print(path.getmtime(b)) #modified time
# print(path.getctime(b)) #change time ()
# os.chmod(b, 0o777)
