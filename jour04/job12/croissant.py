def tri_selection(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
ma_liste = [3, 4, 1, 7, 9, 2]
print(tri_selection(ma_liste))