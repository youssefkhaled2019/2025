# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
# ====================================================
# import os 
# dir_path = os.path.dirname(os.path.realpath(__file__)) #pwd
# print(os.path.abspath(__file__) + "\n")#file path
# print( os.path.join(dir_path,"ccc.txt"))
# print(os.getcwd() + "\n")#pwd
# os.path.exists(file_path)
# os.path.isfile("/etc/password.txt")

# os.remove(file_path) #removes a file.
# os.rmdir(file_path) #removes an empty directory.
# ====================================================
# f = open("demofile.txt", "a")
# dir_path = os.path.dirname(os.path.realpath(__file__)) 
# file_path= os.path.join(dir_path,"demofile.txt")
# print(os.path.exists(file_path))
# ====================================================
# f = open("demofile.txt", "r")
# print(f.read()) #read all file 
# print(f.read(5)) # 5 first characters 
# print(f.readline()) #read on line 
# print(f.readlines())#lines in list 

# for x in f:
#   print(x) 

# f.close() 
# ====================================================
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# ====================================================
# import os
# os.remove("demofile.txt") 

# #Check if File exist:
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# # Delete Folder
# os.rmdir("myfolder") 
# ====================================================
 
# ====================================================

