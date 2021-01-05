# Indicator Basics
> Bruin Quants, Winter Quarter 2020
>Presenter -- Hunter Crosland

### Motivation -- Why Indicators?

- Standard metrics -- think open, high, low, close -- are like the speedometer of a car. They tell you exactly what you need to know at a baseline.
- If we want to look deeper, we need more information. This is where, in a car, something like miles per gallon comes in. For stocks, the number of indicators available is almost absurd.
- To start, let’s look at three of the most basic, and most powerful ones -- the Relative Strength Index, Simple Moving Averages, and Volatility.

### Relative Strength Index
> Measuring "Speed"
- Continuing with our car analogy -- if you are drag racing, only the acceleration of the car matters. The top speed won’t matter a bit. If your race is five hundred miles in a straight line, however, the top speed will ultimately beat out the acceleration.
- In this way, the relative strength index gives us an idea of how a stock will perform in the long run.
- I'd love to give you same LaTeX here, but since markdown doesn't natively support it, I'll just tell you -- the RSI is calculated via measuring the average gain against the average loss of a ticker over a period of time of your choosing.
- The most common RSI is the RSI14, which measures the strength of a stock over the last two weeks. That said, the RSI over, say, ten years, might give you an indication of how a long position will do in a stock, but it is incredibly important to weigh this against shorter RSIs so as to ensure that the strength of a long position is being bolstered.

### The Simple Moving Average
> Measuring "Acceleration"
- The simple moving average allows us a simple way to analyze the momentum of change in a stock price. 
- When we are trading in the short term, we don't care about the price of a stock, we only care about its movement in a given direction. 
- A crossover event happens when the simple moving average over, say, 20 days, takes on a lower value than the simple moving average over, say, 50 days. When this happens, there is no immediate guaranteed reaction of the price of the stock, but when the SMA20 begins to trend upward again, we may be seeing an indication of upward momentum.
- You may hear terms like DMAC -- double moving average crossover -- in reference to this. An example of the DMAC is above -- the SMA20 "crossing over" the SMA50. That said, we can analyze a much more significant number of SMAs -- even fractionally -- to measure momentum. Yay research team!
![AAPL_SMAs_legend.png](https://github.com/HunterCrosland/md_dump/blob/master/AAPL_SMAs_legend.png)
![AAPL_SMAs.png](https://github.com/HunterCrosland/md_dump/blob/master/AAPL_SMAs.png)

### Volatility
> Measuring "The Turning Radius"
- Volatility gives us an idea of how much a stock moves around its average in a given period of time.
- Higher volatility implies large discrepancy between the peaks and valleys of a stock, and a lower volatility implies a small discrepancy. 
- When we are trading in the short term, high volatility can be a great thing if we can nail when the peaks and valleys will appear, because we will have higher gains.
- When we are trading in the long term, however, a lower volatility is better due to a weird echochamber effect of volatility.
- Traders see a stock with high volatility and see an opportunity to get rich quick -- this leads to high volumes of buys and sells over the lifetime of the stock. This can artificially inflate its value. Once the stock settles, holders may realize the lack of substance behind the price of the stock, and close their positions. This would lead to a crash, and that's obviously bad for someone who bought at a high and wanted to hold a long position.

### Beyond the Basics
- What we have above is enough to create a naive algorithm that can make money.
- To extend into new territory requires creativity. Not much is published in the way of how to combine other metrics. 
- This is where the research sector of BQuants comes in -- we will need a comprehensive approach to finding combinations of metrics without overfitting. 
- We don't want to throw every metric we can find into a smorgasbord and hope that profitable stocks come out. Instead, we need to find the right batch for particular situations. 
