
def plusMinus(arr):
    # Write your code here
    positive = sum(1 for x in arr if x > 0)
    negative = sum(1 for x in arr if x < 0)
    zeros = sum(1 for x in arr if x == 0)
    
    pos_ratio = positive / n
    neg_ratio = negative / n
    zer_ratio = zeros / n
    
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zer_ratio:.6f}")
     
n = 6
arr = [-4, 3, -9, 0, 4, 1]
print('====== TEST ======')
print(plusMinus(arr))
