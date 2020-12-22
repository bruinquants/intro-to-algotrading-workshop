# Algo Trading and Data Analysis

### How to get started

Make an account with Alpaca.  It's the free API we'll be using that allows us to fetch historical data, 
place orders into a paper trading account, and test our algorithm using live market data.  

You'll need to generate your API keys, which tells the server that we're allowed to use it.  Place the key and the 
secret key in their respective places in the ```config.py``` file.

### API interface 

The ```setup_requests.py``` file provides the basic interface to interact with our API.  We can get the information
about our account, see our portfolio, and place orders to our paper trading account.  See the
[documentation](https://alpaca.markets/docs/api-documentation/api-v2/) for extensive details about the response schema.  

If you have everything setup and running correctly you should be able to run the ```setup_requests.py``` file and see
1 share of Apple now in your portfolio.  The order might not fill immediately if you place the order outside of market
hours.

This should be everything we

### Websocket streaming for live data

### Getting historical data

### Pairs Trading and Time Series Analysis