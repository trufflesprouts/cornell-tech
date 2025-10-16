def add_element(lst, element):
    """
    Appends the given element to the end of the list.
    """
    lst.append(element)
    return lst

def insert_element_at(lst, element, index):
    """
    Inserts the element at the specified index.
    """
    lst.insert(index, element)
    return lst

def remove_element(lst, element):
    """
    Removes the first occurrence of the element from the list.
    """
    lst.remove(element)
    return lst

def pop_element_at(lst, index):
    """
    Pops and returns the element at the specified index.
    """
    return lst.pop(index)
