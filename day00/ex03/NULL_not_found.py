def is_Nan(n):
    if n != n:
        return True
    else:
        return False


def NULL_not_found(object: any) -> int:
    ret = 0
    if object is None:
        print("Nothing", " : None", type(object))
    elif is_Nan(object) is True:
        print("Cheese", " : nan ", type(object))
    elif (object is False):
        print("Fake", " : False", type(object))
    elif object == 0:
        print("Zero", " : 0", type(object))
    elif object == "":
        print("Empty", " : class", type(object))
    else:
        print("Type not Found")
        ret = 1
    return ret
