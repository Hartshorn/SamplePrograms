# CSCI 1521 - Fall 2013
# wed 4:00-6:00p and online

# Student Name: Michael Palmer
# Date complete: Tuesday, November 5th, 2013

# the problem here is not getting the slice off the first list
# and reversing it onto the second list, but making sure those
# items are REMOVED from the first list. Just slicing them does
# does not remove them from list1. Instead we have to pop them
# out. But when one entry is popped out, the index varies for
# all of the others. So, in effect, we have to stay in the same
# index location as we pull the items off of the first list.
# The solution is to make a new list, create a while loop to run
# for as long as the difference between the two slice values (r1
# and r2), and to append the new list with entries from the starting
# location over and over again by popping them off of the original list.
# This way we are left with a new list which is the section we want,
# and the original list no longer has those entries. We then simply
# append the second list with the items popped off the end of the newList.

# begin transform function definition
def transform(list1,list2,r1,r2):
    newList = []
    i = 0
        
    while(i < (r2 - r1)):				# this loop will pop off the needed values
        newList.append(list1.pop(r1))
        i += 1
        
    while(newList != []):				# this loop will append the values to list2
        list2.append(newList.pop())
                
    return list2
# end transform function definition
        
# here is some sample data that will run to show
# the function working

l = [1,2,3,4,5,6,7,8,9]
r = [9,8,7,6,5,4,3,2,1]

print("BEFORE (values of entered lists)")
print("r = ", r)
print("l = ", l)

transformedList = transform(l,r,0,4)
print("\nFunction Returns: ", transformedList)

print("\nAFTER (new values of entered lists)")
print("r = ", r)
print("l = ", l)


