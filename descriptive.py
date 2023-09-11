import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def gen_stats():
    df = pd.read_csv("wine.csv")
    print(df.describe())

    # calculate the median/mean/standard deviation for the log wine prices
    price_median = df["Price"].dropna().median()
    price_mean = df["Price"].dropna().mean()
    price_sd = df["Price"].dropna().std()
    print("The median log wine price is " + str(price_median))
    print("The mean log wine price is " + str(price_mean))
    print("The standard deviation for log wine price is " + str(price_sd))

    # visualization: histogram for log wine price
    plt.hist(df["Price"], bins=5, edgecolor="k")
    plt.xlabel("Log wine price")
    plt.ylabel("Frequency")
    plt.title("Frequency distribution of log wine price")
    plt.show()

    # visualization: correlation plot between columns
    sns.pairplot(df)


if __name__ == "__main__":
    gen_stats()
