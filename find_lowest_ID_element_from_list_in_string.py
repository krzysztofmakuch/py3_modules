def find_listkey(string, list_of_keys):
    '''Finds an index of the first elemnts found, takes multiple keys.
    The lowest index amongst the indexes found for keys is returned'''

    return min([string.find(x) for x in list_of_keys])
