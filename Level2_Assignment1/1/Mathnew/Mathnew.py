def sqrt(tempval):
    return tempval**0.5
def addition(tempval1,tempval2,*args):
    sumval = tempval1 + tempval2
    for value in args:
        sumval += value
    return sumval
def subtraction(tempval1,tempval2,*args):
    subval = tempval1 - tempval2
    for value in args:
        subval -= value
    return subval
def multiply(tempval1,tempval2,*args):
    mulval = tempval1 * tempval2
    for value in args:
        mulval *= value
    return mulval
def divide(tempval1,tempval2):
    return tempval1/tempval2


