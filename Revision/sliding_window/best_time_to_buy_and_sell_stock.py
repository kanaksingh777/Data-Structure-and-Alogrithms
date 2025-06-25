def buy_n_sell_stock(prices):


    max_profit = 0

    l,r  = 0,1
    
    while l < r  and r < len(prices): 
        if prices[l] > prices[r]:

            l = r
            r= r+1
        else: 
            max_profit = max(prices[r]-prices[l], max_profit)
            r = r+1

        

    return max_profit  

prices = [5,1,5,6,7,1,10]
print(buy_n_sell_stock(prices))