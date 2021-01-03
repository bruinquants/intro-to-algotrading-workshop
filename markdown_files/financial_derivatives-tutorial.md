# Financial Derivatives Tutorial

### What is a Financial Derivative?
A Financial Derivative is a financial instrument that is derived from some other security.
-    In almost every case, owning a financial derivative gives you the right to purchase the underlying security at a certain price before a certain date.
        -  The most common forms of financial derivatives includes... :
            -   Options Contracts (Calls, Puts, etc.).
            -   Index Futures (US 30 (DOW), US 100 (SPY), US Tech 100 (NQ), etc.).
            -   Commodity Futures (Gold Futures, Soybean Futures, Crude Oil Futures, etc.).
            -   Swaps (Credit Swaps, Interest Rate Swaps, etc.).
            -   and many more...
        -   For the purposes of this course, we will focus on options and index futures.
-   The vast majority of financial derivatives are managed and issued by Cboe Global Markets.
-   Excluding options, the vast majority of financial dervatives are traded by institutions as a means to hedge equity positions or to profit via speculative trading.
-   Derivatives often carry more risk than traditional equities because they are *leveraged*.
       -    Leverage refers to the ability to control more securities than one paid for.
       -   **Note :** Many blame the lack of regulation in the derivatives market as the cause of the *2008 Financial Crisis* and following *Great Recession*. Derivatives should be used with extreme caution.

### What are Options Contract?
Commonly shortened to "options," options contracts give the holder the "option" to exercise the contract at anytime before the expiration date if the underlying security's price is above the "strike price."
-   There are two main types of options :
       -   **Calls :** gives the holder the option to buy 100 shares of a certain security from the issuer at a certain strike price.
       -   **Puts :** gives the holder the option to sell 100 shares of a certain security from the issuer at a certain strike price.
-   Both types of options are leveraged, because the holder has the rights to 100 shares of a security that they did not pay for. 
       -   Because of this, options are more volatile than the underlying security.
-   Options expire worthless if they aren't exercised before the expiration date.
       -   For this reason, options decrease in value exponentially as we get closer to expiration. This is also known as **theta decay**.
-   Options trading is a form of speculation--the buyer of an option is betting that the underlying security will either go up in value (for a call) or go down in value (for a put) by the expiration date.
       -   As the underlying security changes in value, the associated option will also change in value (often more dramatically).
       -   The *implied volatility*, or simply IV, is a value that measures the implied (anticipated) movement of the underlying security. As IV goes up, the option's price will also go up. Algos that trade based off of news sentiment takes advantage of IV for profit.
-   **Note :** These definitions *only* apply to US options managed by the Chicago Board Option Exchange. 
       -   Employers may issue employer compensation in the form of non-derivative options which are not leveraged.
       -   Options contracts work vastly differently in other parts of the world.

### What are Index Futures?
Index futures are also a type of contract that allows the holder to purchase a certain security for a certain price that will settle on a later date. In the case of index futures, the right to purchase Dow Jones Industrial Average (DJIA), S&P 500, Nasdaq 100, and many other indexes.
-   There are two types of positions you can take on any future :
       -   **Long :** the purchaser believes that the future will appreciate (go up) in value.
       -   **Short :** the purchaser believes that the future will depreciate (go down) in value.
-   Like options contracts, they are used as a means to hedge a position or to speculate on future price movements.
-   Unlike options contracts or commodity futures, index futures are *cash settled*. This means that the index future contract holder doesn't actually purchase the underlying security, but instead recieves an appropriate cash payment.
-   Index futures are complex financial instruments that mostly only institutions are involved in.
       - Examples of entitites involved in trading index futures include : investment banks, hedge funds, portfolio managers, HFT traders, etc.

### Final Remarks
Financial derivatives are complex financial instruments that are important for institutions and quantitative analysts.
-   Derivatives provide a method to speculate on the future of a security without actually owning the security.
-   Derivatives are associated with more risk because of *leverage*.
