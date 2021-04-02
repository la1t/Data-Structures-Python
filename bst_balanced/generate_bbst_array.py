def GenerateBBSTArray(a):
    if not a:
        return []
    sorted_a = sorted(a)
    depth = calc_min_depth(len(a))
    res = [None] * calc_array_len(depth)
    fill_tree(sorted_a, 0, res)
    return res



def fill_tree(a, curr_index, tree_list):
    if not a:
        return
    mid_index = len(a) // 2
    tree_list[curr_index] = a[mid_index]
    fill_tree(a[:mid_index], curr_index * 2 + 1, tree_list)
    fill_tree(a[mid_index+1:], curr_index * 2 + 2, tree_list)


def calc_min_depth(num_items):
    current_depth = 0
    while True:
        if calc_array_len(current_depth) >= num_items:
            return current_depth
        current_depth += 1


def calc_array_len(depth):
    return 2 ** (depth + 1) - 1
