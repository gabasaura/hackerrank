
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min = sum(arr[:4])
    max = sum(arr[1:])
    
    return f"{min} {max}"

print('====== TEST ======')
arr = [1, 2, 3, 4, 5]
print(miniMaxSum(arr))
