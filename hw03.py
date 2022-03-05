## Ex2: ternary search
def ternarySearch(arr, k, buff=0):
    # Check input
    if arr != sorted(arr):  return -1
    if k < arr[0] or k > arr[len(arr)-1]:    return -1
    
    # Break point
    if len(arr) < 4:
        for i in range(0, len(arr)):
            if arr[i] == k:    return i + buff
        return -1;

    # arr range: a1__a2__a3__a4
    a1, a4 = 0, len(arr)
    a2 = a1 + (int)((a4-a1)/3)
    a3 = a2 + (int)((a4-a1)/3)

    if k < arr[a2]: return ternarySearch(arr[:a2+1], k, buff=buff)
    if k < arr[a3]: return ternarySearch(arr[a2:a3], k, buff=a2 + buff)
    return ternarySearch(arr[a3:], k, buff=a3 + buff)

def binary_insertion_sort(arr):
    ans = arr[:1]
    for i in range(1, len(arr)):
        index = binary_search_to_insert(ans, arr[i])
        ans.insert(index, arr[i])
        # print(ans + arr[i+1:])
    return ans

def binary_search_to_insert(arr:list , k, buff=0):
    # Check input
    if arr != sorted(arr):  return -1
    if k < arr[0]:  return buff
    # print("1")
    if k > arr[len(arr)-1]: return buff + len(arr)
    # print("1")

    # Break point
    # print("1")
    if len(arr) < 4:
        for i in range(0, len(arr)):
            # print("1")
            if arr[i] >= k:    return i + buff
        return -1;

    # arr range: a1__a2__a3
    a1, a3 = 0, len(arr)
    a2 = a1 + (int)((a3-a1)/2)

    # print("1")
    if k < arr[a2]: return binary_search_to_insert(arr[:a2], k, buff= buff)
    return binary_search_to_insert(arr[a2:], k, buff= a2 + buff)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        # count = 2
        while j > 0 and arr[j] < arr[j-1]:
            # count += 2
            
            t = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = t
            j -= 1
    # print(f"insertion: {count}")
    return arr

if __name__ == "__main__":
    a = [7, 4, 3, 8, 1, 5, 4, 2]
    print(binary_insertion_sort(a))
    print(insertion_sort(a))
