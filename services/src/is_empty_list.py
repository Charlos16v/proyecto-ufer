def is_empty_list(array):
    for e in array:
        if e != "":
            return False
        elif e == "":
            return True

if __name__ == '__main__':
    assert is_empty_list(["",["",""]]) == True
    assert is_empty_list(["test",["",""]]) == False