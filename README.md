# Group4_Project1


PROJECT PROPOSAL

1. Create a user interface / financial tool that allows us to loop through the SP 500 historical data that will allow us to generate a list of 10 stocks that have outperformed the index over a selected time frame ( 6months , 1yr, YTD, 5yr, 10 yr) and display the information on a graph with their individual performance compared to the benchmark (SP500) and the other 9 stocks. 

2. Pull the financial metrics from the list (i.e. beta, eps, volume, etc)  to create a data base that we can use to enter a combination of any other 10 stocks from the SP500 to run a comparison

3.  Back test the model (generate financial metrics that led them to outperform the market)

4. If successful, implement the model using real time data for use during market hrs

Working Options:

1. Using Montecarlo simulations - Historical info on selected 10 stocks. Return performance simulations over 5 - 10 years.

2. Create Loops to create an intuitive list of 10 stocks that are good opportunity to buy
    Make it interactive. 
    -Use Alpaca 
    Filters: earnings per share, deviation from 52 week high/low, relative strength to market
        use filters to determine good opportunity to buy specific stocks depending on pre-set parameters
        


MAJOR FINDINGS

Can we pull a list of the top performing stocks that have outperformed the SP 500?

Yes. By combining data files from all stocks in the S&P 500 for selected time frames (1 month, 6 months, 1 year, 5 years) we can extract lists of the top growing stocks for each time period and use this list to get more details on the metrics that make them perform at a better rate than the market.


![Top Growing Stocks in the Past 1 Month](https://github.com/laguilar359/Group4_Project1/blob/master/Images/1Month_TopStocks.png)
![Top Growing Stocks in the Past 6 Months](https://github.com/laguilar359/Group4_Project1/blob/master/Images/6Month_TopStocks.png)
![Top Growing Stocks in the Past 1 Year](https://github.com/laguilar359/Group4_Project1/blob/master/Images/1Year_TopStocks.png)
![Top Growing Stocks in the Past 5 Years](https://github.com/laguilar359/Group4_Project1/blob/master/Images/5Year_TopStocks.png)



What sectors are performing best across set time periods?

Technology and Healthcare are the best performing sectors across 6 months, 1 year, and 5 years. Materials and Consumer Discretion are performing best over the 1 Month and 6 Month periods.



![Market Performance by Russell 3000 Sector over the Past 1 Month](https://github.com/laguilar359/Group4_Project1/blob/master/Images/001Month_Sectors.png)
![Market Performance by Russell 3000 Sector over the Past 6 Months](https://github.com/laguilar359/Group4_Project1/blob/master/Images/006Month_Sectors.png)
![Market Performance by Russell 3000 Sector over the Past 1 Year](https://github.com/laguilar359/Group4_Project1/blob/master/Images/01Year_Sectors.png)
![Market Performance by Russell 3000 Sector over the Past 5 Years](https://github.com/laguilar359/Group4_Project1/blob/master/Images/05Year_Sectors.png)



Are we able to extrapolate any common characteristics from the list?

Yes the application enables the user to select a particular sector and find out performing stocks along with a graphical visualization , allowing the user to make an informed decision.


Can we use this data to illustrate a graphical representation of our results?

By extrapolating our data set based on our search inquiry, we are able to create a graphical representation of our results that incorporates several technical financial indicators like the Simple Moving Average (SMA) and Exponential Moving Average (EMA) represented with Open, High, Low and Close candlestick charts.




