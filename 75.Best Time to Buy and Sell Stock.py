def buy_and_sell(prices):
    buy_stock=prices[0]
    sell_stock=0
    for i in range(len(prices)):
        buy_stock=min(buy_stock,prices[i])
        sell_stock=max(sell_stock,prices[i]-buy_stock)
    return sell_stock

prices=list(map(int,input('Enter the array of prices:').split(' ')))

print(f'Maximum Profit earned After buying and selling the stock is ->'
      f' {buy_and_sell(prices)}')