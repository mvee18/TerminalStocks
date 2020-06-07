import yfinance as yf
from datetime import datetime
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

date = str(datetime.today().strftime('%Y-%m-%d'))

ticker = input("Enter a ticker:")
period = input("Enter a custom period, or type 'week', 'month', 'year' or 'max'")

def calculate_time(delta):
    today = datetime.today()
    start = today - delta
    start = start.strftime('%Y-%m-%d')
    return start, today


def get_stonks(period_choice):
    if period_choice == "week":
        delta = timedelta(days=7)
        start, end = calculate_time(delta)
        plot_data(ticker, start, end)

    elif period_choice == "month":
        delta = timedelta(weeks=4)
        start, end = calculate_time(delta)
        plot_data(ticker, start, end)

    elif period_choice == "year":
        delta = timedelta(days=365)
        start, end = calculate_time(delta)
        plot_data(ticker, start, end)

    elif period_choice == "max":
        start = "max"
        end = "N/A"
        plot_data(ticker, start, end)


def plot_data(ticker_name, starting_time, ending_time):
    ticker_data = yf.Ticker(ticker_name)

    # Df means Pd Dataframe.
    if starting_time == "max":
        ticker_df = ticker_data.history(period="max")
    else:
        ticker_df = ticker_data.history(start=starting_time, end=ending_time)

    ticker_df['Close'].plot(title="{} Stock Price".format(ticker))

    plt.show()


get_stonks(period)
