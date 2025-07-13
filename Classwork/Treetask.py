
def count_bridges(tree1, tree2):
    count = 0
    sum1 = sum(tree1)
    sum2 = sum(tree2)

    # Try moving each element from tree1 to tree2 (value doubles in tree2)
    for i in range(len(tree1)):
        value = tree1[i]
        new_sum1 = sum1 - value
        new_sum2 = sum2 + (value * 2)
        if new_sum1 == new_sum2:
            count += 1

    # Try moving each element from tree2 to tree1 (value stays same)
    for i in range(len(tree2)):
        value = tree2[i]
        new_sum2 = sum2 - value
        new_sum1 = sum1 + value
        if new_sum1 == new_sum2:
            count += 1

    return count

# Example trees
tree1 = [1, 2, 3]
tree2 = [4, 5]

result = count_bridges(tree1, tree2)
print(f"Number of bridges (moves making trees equal): {result}")
