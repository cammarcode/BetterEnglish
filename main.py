import random

def quick_sort(data, start=0, end=None):

    if end == None:
        end = len(data)


    if end-start<=1:
        return 1
 
    pivot_index = start
    store_index = start+1
    comparisons = 0

    for i in range(start+1, end):
        comparisons += 1
        if len(data[i]) < len(data[pivot_index]):
            store_index += 1
            data[i], data[store_index-1] = data[store_index-1], data[i]


    data[pivot_index], data[store_index-1] = data[store_index-1], data[pivot_index]
    return comparisons + quick_sort(data, start, store_index-1) + quick_sort(data, store_index, end)

def selection_sort(data):

    count = 0
    for c in range(len(data)):
        index_of_lowest = c
        for i in range(c, len(data)):
            count +=1
            if len(data[i]) < len(data[index_of_lowest]):
                index_of_lowest = i
        data[c], data[index_of_lowest] = data[index_of_lowest], data[c]
    return data
def create_sorted():
    f = open("list.txt", "r")
    tlist = []
    for i in range(10000):
        tlist.append(str(f.readline()))
    f.close()
    random.shuffle(tlist)
    selection_sort(tlist)
    print(tlist)
    f = open("sorted.txt", "w")
    f.writelines(tlist)
    f.close()

comlist = []
slist = []
f = open("list.txt", "r")
for i in range(10000):
    comlist.append(str(f.readline()[:-1]))
f.close()
f = open("sorted.txt", "r")
for i in range(10000):
    slist.append(str(f.readline()[:-1]))
f.close()

while True:
    text = input("ENTER TEXT:").split(' ')
    output = ""
    for i in text:
        val = -1
        for x in range(len(comlist)): 
            if comlist[x] == i.lower():
                val = x
                break
        if val == -1:
            output += i
        else:
            output += slist[val]
        output += ' '
    print(output)