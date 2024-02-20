
def find_pair_with_sum(lst, target):
    seen = set()

    for num in lst:
        complement = target - num
        if complement in seen:
            return [complement, num]
        seen.add(num)

    return None


list1 = [2, 1, 4, 8, 10, 7, 5]
target = 9
result = find_pair_with_sum(list1, target)

if result:
    print(f"Pair with sum {target}: {result}")
else:
    print(f"No pair found with sum {target}")
