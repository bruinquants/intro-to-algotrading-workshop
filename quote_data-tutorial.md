# Quote Data Tutorial

### What is a Quote?
Stock quote data consists of basic statistics about a certain stock.
-   Quote data generally includes...:
        -   Bid-Ask Spread.
        -   Most recent order size.
        -   Most recent stock price.
        -   Volume.
        -   Day's High/Low.
        -   52 Week High/Low.
        -   and a lot more...
-   For the purposes of this course, we will be focusing on the bid-ask spread and order size.
-   These statistics are especially important for traders and quantitative analysts who uses price movement and stock trends to make decisions.

### What is a Bid-Ask Spread?
A Bid-Ask Spread is the range of prices others are willing to buy or sell a security at.
-   A **Bid** is the maximum price someone is willing to buy a security.
-   An **Ask** is the minimum price someone is willing to sell their security.
        -   Think of buying stocks as an auction--the seller wants to sell at the highest price possible and the buyer wants to buy at the lowest price possible. Ultimately both parties are generally trying to reach a deal (a price they are both happy with).
-   A Bid-Ask Spread is affected by a multitude of factors... :
        -   **Supply & Demand** : The Bid-Ask Spread is in a way a direct representation of the supply and demand of a security.
        -   **Volume** : Related to Supply & Demand; higher volume generally means a smaller Bid-Ask Spread.
        -   **Order Size** : Again relate to Supply & Demand; if an order size is bigger, it will have more of an effect on the Bid-Ask Spread.
        -   and more...
-   The Bid-Ask Spread is important for anyone involved in the financial markets.
        -   The Bid-Ask Spread ultimately determines a security's price.
            -   For stocks with high liquidity, the price of the stock is generally accepted to be the average of the bid price and ask price.
            -   For stocks with low liquidity, the price you have to pay to buy a stock will be closer to the ask price and vice versa for when you want to sell a stock.
        -   The Bid-Ask Spread is especially important for quantitative analysts who use High Frequency Trading that utilize the Bid-Ask Spread.
        -   The "Market Makers" make money by utilizing the difference between the bid price and the ask price.

### What is Order Size?
Order size refers to the number of securities an order calls to buy or sell.
-   Order Size is important because it directly affects the Bid-Ask Spread and therefore the price of the stock.
        -   Example : If you place a limit buy order for 50 shares of `AAPL`, you have effectively changed the price of `AAPL`! Though it would be completely insignificant given Apple's market cap...
-   Through the law of *Supply & Demand*, bigger order sizes will effect the price of a security more.
        -   Example : If you place a limit sell order for 100k shares of a small cap penny stock, you will likely have a direct impact on its price.
-   **Note :** An order does *NOT* have to be filled in order to affect a security's price. As a matter of fact, an order and its order size no longer directly affects the security's price once it has been filled. This is very important to know, especially for quantitative analysis.
        -   This means you can effectively manipulate a stock's price by consecutively placing and cancelling massive orders in one direction. This practice is called *price manipulation* and it becomes *illegal* at a certain extent.
        -   This practice caused the *2010 Flash Crash*, and since then more safeguards have been put in place to avoid this happening in the future.