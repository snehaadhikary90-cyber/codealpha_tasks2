
# Stock Portfolio Tracker

# Dictionary containing predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 175,
    "MSFT": 420
}

total_investment = 0

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Take user input
num_stocks = int(input("\nHow many different stocks do you want to buy? "))

portfolio = {}

for i in range(num_stocks):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            investment = stock_prices[stock_name] * quantity
            total_investment += investment

            portfolio[stock_name] = quantity

            print("Investment in", stock_name, "=", "$", investment)
        else:
            print("Quantity must be greater than zero.")

    else:
        print("Stock not available!")

# Display portfolio
print("\n================================")
print("       YOUR STOCK PORTFOLIO")
print("================================")

for stock, quantity in portfolio.items():
    print(stock, "-", quantity, "shares")

print("\nTotal Investment: $", total_investment)

# Save result in a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(stock + " - " + str(quantity) +
                   " shares = $" + str(investment) + "\n")

    file.write("\nTotal Investment: $" + str(total_investment))

print("\nPortfolio saved successfully in portfolio.txt!")
print("Thank you for using Stock Portfolio Tracker!")
