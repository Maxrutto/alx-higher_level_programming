#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    _mylist = my_list[:]
    if idx < 0:
        return _mylist
    if idx > len(_mylist) - 1:
        return _mylist
    else:
        _mylist[idx] = element
        return _mylist
