import os
import filecmp
import itertools

temp_list1 = []
result_dict = {}
unique_files = []
duplicate_files = []
temp_list2 = []
    
input = raw_input("Please enter directory location:")
def file_compare(input): 
    
    for directory, dirnames, filenames in os.walk(input):
        temp_list1 = filenames
    
    for a, b in itertools.combinations(temp_list1, 2):
        #print (a,b)
        result = filecmp.cmp(os.path.abspath(a), os.path.abspath(b))
        
        if result == True :
            duplicate_files.append(a)
            duplicate_files.append(b)
        
        elif result == False and a not in unique_files: 
            unique_files.append(a)
            
        elif result == False and b not in unique_files:
            unique_files.append(b)
    
    for item in duplicate_files:
        if item not in temp_list2:
            temp_list2.append(item)
            
    #print ("temp_list2 items displaying {}".format(temp_list2))
    
    for item1 in temp_list2:
        for item2 in unique_files:
            if item1 == item2:
                unique_files.remove(item2)
        
    result_dict['matches'] = [unique_files]
    result_dict['matches'].append(temp_list2)

'''
result = filecmp.cmp(os.path.abspath("/home/ubuntu/workspace/blog/files/B.csv"), os.path.abspath("/home/ubuntu/workspace/blog/files/C.iso"),shallow=False)
print (result)
if result == True:
    print ("both files are equal")
else:
    print ("not equal")
   
'''
if __name__ == "__main__":
    file_compare(input)
    #print ("unique_files are:",unique_files)
    #print ("duplicate_files are:",temp_list2)
    print ("final result are - >{}".format(result_dict))
