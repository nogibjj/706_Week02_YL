import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def gen_stats():
    df = pd.read_csv("wine.csv")

    # calculate the median/mean/standard deviation for the log wine prices
    price_median = df["price"].dropna().median()
    price_mean = df["price"].dropna().mean()
    price_sd = df["price"].dropna().std()
    print("The median log price for wine is "+str(price_median))
    print("The mean log price for wine is "+str(price_mean))
    print("The standard deviation log price for wine is "+str(price_sd))

    # visualization 1: histogram for log wine price
    plt.hist(df, bins=5, edgecolor="k")
    plt.xlabel("Median log wine price")
    plt.ylabel("Frequency")
    plt.title("Frequency distribution of median log wine price")

    plt.show()

    return price_median, price_mean, price_sd

if __name__ == "__main__":
    gen_stats()