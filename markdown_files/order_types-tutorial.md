# Order Types Tutorial

### What is an Order?
Like the name implies, an order is a request to buy or sell a security.
-    There are 2 main types of orders :
        -   **Market Order :** Used to purchase or sell a security regardless of the price. Best option when you would like to have your order fufilled regardless of price fluctuations.
               -   **Warning :** A market order can be "dangerous" when the security has low volume (liquidity) because of the wide bid-ask spread. Additionally, you are less likely to get the "best price" despite being more likely to have your order filled. 
               -   **Note :** Many brokerages do *not* allow you to use market orders during premarket and afterhours hours, because the low liquidty relative to regular market hours can cause massive fluctations in price.
        -   **Limit Order :** Used to purchase or sell a security above or below a certain price. This is the most comon
               -   **Note :** You are less likely to have your order filled if you use a limit order. This is because you are bidding or asking a certain price, which the market may or may not agree with.
-   Depending on the security's liquidity and how much you need your order to get filled, you should pick which order type to use accordingly.
- **Note :** A market order where you sell a security is referred to as a *market sell order*, a limit order where you buy a security is referred to as a *limit buy order*, etc.

### What is a Stop Loss?
A stop loss is a conditional order that is automatically executed by your brokerage if a certain condition that you set is met.
-   Most commonly a stop loss is a *conditional market sell order* that is executed when a certain security goes below a predetermined value.
       -   Example : If you set a stop loss for a certain stock you own at $50.50, a *market sell order* will be executed if the stock dips below $50.50.
       -   **Warning :** Because a stop loss is ultimately a *market order*, you must be careful when you use it.
-   There are other types of stop losses such as *trailing stop losses*, *stop limits*, etc. For the purposes of this course, you don't have to know all of them, but they are mostly self-explainatory.

### Example Scenarios
**Disclaimer : These are informative examples, and shouldn't be treated as investment advice or recommendations. If you choose to trade in the financial markets, you are liable for the decisions that you make.**

Example 1 : You would like to buy Apple stock `NASDAQ:AAPL` because you are *confident* that the stock will go up at open. What order type should you use?
-   Because `AAPL` is a highly liquid stock and you are *confident* that the stock will go up, you would more likely want to use a *market buy order*.

Example 2 : You would like to daytrade Hertz stock `OTCMKTS:HTZGQ` which has relatively low volume and is a penny stock. What order type should you use?
-   Because `HTZGQ` is a relatively illiquid stock with high volatility, you would more likely want to use a *limit order*.

Example 3 : You would like to buy Amazon stock `NASDAQ:AMZN` because you believe that Amazon is a good long term investment. What order type should you use?
-   Trick question. There is no correct answer, but you would generally want to use *limit buy orders* unless you have a very good reason to use a *market buy order*.

Example 4 : You have a few shares of Tesla `NASDAQ:TSLA` and you are afraid that the stock will tank. What order type should you use to protect your gains?
-   Another trick question. Ideally you would use a *limit sell order* to sell your stocks when you cannot take any more risk, but it would also be valid to use a *stop loss*.

All in all, you generally want to use more *limit orders* than *market orders* or *stop losses* because you have more control over your capital and your securities.