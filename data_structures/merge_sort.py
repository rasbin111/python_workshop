# working - merge sort, might be possible to optimize 
numbers = [20, 10, 30, 20, 6, -1]

def merge_sort(array):
    if len(array) == 1 or len(array) == 0:
        return array
    
    mid = len(array) // 2
    
    a1 = merge_sort(array[:mid]) # recursive
    a2 = merge_sort(array[mid:]) # recursive

    i1 = 0  # index for left half of an array
    i2 = 0  # index for right half of an array

    merged_array = []

    for i in range(0, len(a1)+len(a2)):
        if a1[i1] <= a2[i2]:
            merged_array.append(a1[i1])
            i1 += 1
            if i1 == len(a1):
                """ if we reach end of left half array, then simply add remaining 
                element of right half to the merged array """
                for i in range(i2, len(a2)):
                    merged_array.append(a2[i])
                break
        else:
            merged_array.append(a2[i2])
            i2 += 1
            if i2 == len(a2):
                """ if we reach end of right half array, then simply add remaining 
                element of left half array to the merged array """ 
                for i in range(i1, len(a1)):
                    merged_array.append(a1[i])
                break
                

    return merged_array

merged_array = merge_sort(numbers)
print(merged_array)
