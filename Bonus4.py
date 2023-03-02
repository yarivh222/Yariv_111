def Max1_Digit(Arr1):
    Max_Number = -1

    for Number in Arr1:
        if 0 <= Number <= 9 and Number> Max_Number:
            Max_Number = Number
    return Max_Number

arr=[-5, 94, 1001, -100, 76, 1, 0, 503]
print(Max1_Digit(arr))
