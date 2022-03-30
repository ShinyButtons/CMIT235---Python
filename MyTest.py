# Created by Jennifer Langford on 3/24/22 for CMIT235 - Week 1 Assignment
# This is an ongoing effort weekly for the duration of this course.
# The program will be complete at the end of the course.

import numpy as np
import CMIT235_Package.CMIT235_Tools as cm

lst = cm.mySubList1 + cm.mySubList2 + cm.mySubList3 #combining the lists in to list
print("The whole list: \n", lst) #output to screen the combined lists
arr = np.array(lst) #creates a numpy array of the combined lists
print("The lowest value is: \n", np.min(arr)) #output to screen the min value
print("The maximum value is: \n", np.max(arr)) #output to screen the max value
print("The unique values are: \n", np.unique(arr)) #output to screen the unique values

for i in (cm.mySubList1, cm.mySubList2, cm.mySubList3): #for loop
    arr1 = np.array(i)
    print("The array: \n", arr1) #prints the array
    print("The dimension of the array: \n", arr1.ndim) #prints the dimension
    print("The shape of the array: \n", arr1.shape) #prints the shape
    print("Last item of the array: \n", arr1[1, -1]) #prints the last item
    print("Column 0: \n", arr1[0:, 0]) #prints column 0
    print("Second row: \n", arr1[1:]) #prints the 2nd row


