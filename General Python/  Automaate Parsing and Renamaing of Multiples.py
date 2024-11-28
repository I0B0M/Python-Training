# Automaate Parsing and Renamaing of Multiple Files

import os
os.chdir('/Users/ibm/Desktop/Python')

print(os.getcwd)

for x in os.listdir():
    
    file_name,file_ext = os.path.splitext(x)
    
    # print(os.path.splitext(x))
    
    # print(file_name)
    
    print(file_name.split('-)'))
    
    f_title,f_course,f_num =file_name.split('-')
    
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)
    
    
    print('{}-{}{}'.format(f_num,f_title,file_ext)
          
    new_name = ('{}-{}{}'.format(f_num,f_title,file_ext)
    
    os.rename(f,new_name)
    