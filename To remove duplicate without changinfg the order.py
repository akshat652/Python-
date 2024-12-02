#To remove the duplicate items of the list by converting into set and without changing the order

def org_list(lst):
    seen = set()
    return [x for x in lst if not(x in seen or seen.add(x))]
    
my_list = [1,1,5,7,8,9,55,44,22,22,22,11,5,7,88,9]
result = org_list(my_list)
print(result)