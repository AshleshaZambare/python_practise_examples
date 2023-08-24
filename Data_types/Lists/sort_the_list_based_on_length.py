
def myfunc(ele):
    return len(ele)

list1 = ["hello", "hi", "bye", "ais", "butter"]
list1.sort(key = myfunc)
print(list1)