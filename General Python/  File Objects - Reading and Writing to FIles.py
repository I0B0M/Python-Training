# File Objects - Reading and Writing to Files


# r + = reading and writing
# w = writing
# a = append
# r = reading



# f = open('/Users/ibm/Desktop/Python/test.txt','r')


# print(f.mode)
# print(f.name)

# f.close()

# with open('/Users/ibm/Desktop/Python/test.txt','r') as f:
    
#     for line in f :
#         print(line,end ='')
    
#     f_contents = f.read(100)
#     print(f_contents)
    
#     f_contents = f.read(100)
#     print(f_contents)
    
#     f_contents = f.read(100)
#     print(f_contents)

# with open('/Users/ibm/Desktop/Python/test.txt','r') as f:
    
#     size_to_read= 10

#     f_contents = f.read(size_to_read)
    
#     print(f.tell())
    
    # while len(f_contents)>0:
    #     print(f_contents,end='*')
    #     f_contents = f.read(size_to_read)
        
        
    # print(f_contents)
# using f.seek(0) can start the read from the beginning instead of continuing(We can also start from anywhere by adding the character number)




# with open('/Users/ibm/Desktop/Python/test.txt','w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')
    
    
with open('/Users/ibm/Desktop/Python/test.txt','r') as rf:
    with open('/Users/ibm/Desktop/Python/test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)