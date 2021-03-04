def add_element(my_set, elem):
    if (elem >0):
        my_set.add(elem)
    return my_set
#Create a method that removes negative values from a set.
def remove_negative_values(my_set):
    return set([x for x in list(my_set) if x >= 0])
#Create a method that returns the sum of all elements in a set.
def sumset(my_set):
    return sum(list(my_set))