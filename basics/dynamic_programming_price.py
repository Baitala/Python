# dynamic programming

def count_min_cost(N, price:list):
    cost =([float("-inf"), price[1], price[1]
            + price[2]] + [0] * (N - 2))
    for i in range(3, N + 1):
        cost[i] = price[i] + min(cost [i - 2], cost[i - 1])
    return cost[N]