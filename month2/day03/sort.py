
def bubbleSort(list_):
    """

    """
    # i = 1
    for i in range(len(list_)-1):
        for j in range(len(list_)-1-i):
            if (list_[j]>list_[j+1]):
                list_[j],list_[j+1] = list_[j+1],list_[j]

def sampleSort(list_):
    """
    sample select sort
    """
    for i in range(len(list_)-1):
        temp = i
        for j in range(i+1,len(list_)):
            if (list_[j]<list_[temp]):
                temp = j
        list_[i],list_[temp] = list_[temp],list_[i]

def inserSort(list_):
    for j in range(1,len(list_)):
        temp = list_[j]
        i = j -1
        while i>-1 and temp<list_[i]:
            list_[i+1] = list_[i]
            i -= 1
        list_[i+1] = temp




list01 = [3,6,2,8,9,34,78,3,5,1,0,73]
inserSort(list01)
print (list01)