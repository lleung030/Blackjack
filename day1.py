# Create a function that given a list of numbers as an input (nums_list) return True if the numbers are in consecutive order, return False if not.
# Example Input: [1,2,3,4,5]
# Example Output: True
# Example Input: [2,4,6,8,10]
# Example Output: False
# Example Input: [10,11,12,13,14]
# Example Output: True

def move_0(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
        return lst
    print(lst)

print(move_0([0,0,1,2,3,4]))
# print(move_0([0,1,2,3,0,4]))
