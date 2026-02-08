def get_max_sum(n):
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(max(i, res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]))
    return res[n]
