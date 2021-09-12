"""
Function

[syntax] led by the keyword of def(ine)

def function_name():
    \"""docstring\"""
    # body of function
"""


def getReady():
    """
    get ready
    :return:
    """
    print("getting up ")
    print("put on cloths")
    print("brush teeth")
    print("do washing")
    print("have breakfast")
    print("close your door")


def travel():
    """
    travel to my school
    :return:
    """
    print("getting my opus card")
    print("walk to bus stop")
    print("get to subway station")
    print("get on board")
    print("get off")
    print("go into campus")


# main program
getReady()
travel()

print(getReady.__doc__)
print(travel.__doc__)

