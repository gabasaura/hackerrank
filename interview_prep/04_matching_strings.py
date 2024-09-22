

def matchingStrings(strings, queries):
    # Write your code here
    total = []
    for q in queries:
        count = strings.count(q)
        total.append(count)
    return total


strings = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]

print('====== TEST ======')
print(matchingStrings(strings, queries))
