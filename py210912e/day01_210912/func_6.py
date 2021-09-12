"""
Function
function name


identifier
a name given to python entities (incl. variable, constant, function, class)
comply to identifier rules

rules:
_a-zA-Z0-9 valid char
starting with _ or alphabet
avoiding reserved words or keywords

conventions:
try best to use verb. or verb. phrase  (representing a behavior)

it should be unique within a module/python source code file
"""

# good
def travel():
    pass


# not good
def ipad():
    pass


# naming convention
def get_ready():
    pass


def getready():
    pass


def getReady():
    print("2nd getReady()")

def getReady():
    print("1st getReady()")

# def getReady():
# #     print("2nd getReady()")


# main prog.
getReady()





