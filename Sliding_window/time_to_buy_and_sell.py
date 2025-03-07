def max_profit(prices):

    l,r =0,1
    max_profit = 0
    while l<r and r <= len(prices)-1:

        if prices[l] > prices[r]:
            l = r
            r += 1
        else:
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit,curr_profit)

            r = r+1
    
    return max_profit 


prices = [2,1,2,1,0,1,2]
ans = max_profit(prices)
print(ans)