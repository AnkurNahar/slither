# defining 2 sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union combines elements from both sets with no duplicates
union_result = set1.union(set2)
print("union:", union_result)

# intersection gives elements common to both sets
intersection_result = set1.intersection(set2)
print("intersection:", intersection_result)

# difference gives elements in set1 but not in set2
difference_result = set1.difference(set2)
print("difference:", difference_result)

# symmetric difference gives elements in both set that are not common to either
symmetric_difference_result = set1.symmetric_difference(set2)
print("symmetric difference:", symmetric_difference_result)