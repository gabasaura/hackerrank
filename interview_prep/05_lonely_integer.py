
def lonelyinteger(a):
    # Write your code here
    sum = []
    
    for is_alone in a:
        sum = a.count(is_alone)
        if sum == 1:
            return is_alone
        

a = [1, 2, 3, 4, 3, 2, 1]
print('====== TEST ======')
print(lonelyinteger(a))