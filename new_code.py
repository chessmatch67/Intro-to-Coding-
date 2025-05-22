# file = "file_name.txt"
# new_file_sum = "sum_collum.txt"

# with open(file,'r') as temp:
#     data = temp.read() # read() returns all data as one string
# #     # read_data = f.read()
#     # print(temp)
   
#     # data_list = temp.readline()
#     # print(data_list)

#     # data_list = temp.readlines() # returs a list with each line as a string. 
#     # print(data_list)

# split_data = data.split()
# print(split_data)

# with open(new_file_sum,'r') as temp:

#     data = temp.read()
# def sumColumn(new):
#     num = 0

#     for x in new:
#         num += x
#     print(x)

# sumColumn(data)

# problem number 3 ----------------------------------------------3 
# def open_file(filename,  option='read'):
#     with open(filename, 'r') as f:
#         if option == 'read':
#             return f.read()
        
#         elif option == 'readlines':
#             return f.readlines()
#         else:
#             return None 

# def write_file(filename, a_string, mode):
#     with open(filename, mode) as f:
#         f.write(a_string)


# open_file('sum_collum.txt', "This is just a text second", "r")
# print(open_file)


# problem number 2 ---------------------------------------------------------.

# data = open_file("file_name.txt",'readlines')
# print(data)

# for line in data:
#     print(line.split())

# append adds a new line without deliting the previous data. 
# wrting adds a line and deletes everything.


# def open_file(filename,  option='read'):
#     with open(filename, 'r') as f:
#         if option == 'read':
#             return f.read


# <<<<<<< ---------------------Problem num 4------------------------------>>>>>>>>

# def sum_collum(filename):
    
#     with open(filename, 'r') as f:
#         return f.read()
    
# gotten = sum_collum('sum_collum.txt')
# list_split = gotten.split()
# semi = 0

# for s in list_split:
#     semi += int(s)
# print(semi)

# <<<<<<<<<------------------------problem 5----------------------------->>>>>>>>>>

# def sum_all(filename):
#     with open(filename, 'r') as f:
#         return f.read()

# gotten = sum_all('sum_all.txt')
# list_split = gotten.split()
# semi = 0
# for s in list_split:
#     semi += int(s)
# print(semi)

# -----------------------------problem 6---------------------------------------------->

# def Read_collum(filename, num):
#       with open(filename, 'r') as files:
#           taken = files.readlines()
          
#           for s in taken:
#                new = s.split()
#                print(new[num])    

# taken = Read_collum('Read_colum.txt', 0)

#<<<<<------------------------------problem 7---------------------------------------------->>>>

def counter_wolrd(filename, word):
     with open(filename, 'r') as files:
          taken = files.readlines()
          counter = 0
       
          for find_word in taken:
               new =  find_word.split()
               semi = new.count(word)
               counter += 1

               if counter == len(word):
                    print(counter)

               
counter_wolrd('zenOfPython.txt', 'is')
          