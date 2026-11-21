import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def analysis_data(df,chart="Chart_figure.png"):
    total_revenal = np.sum(df["Total_Sales"])
    total_average = np.mean(df["Total_Sales"])
    summary = df.groupby("Product")["Total_Sales"].sum().reset_index()
    sb.set_theme(style="whitegrid")
    plt.figure(figsize=(6,4))
    sb.barplot(data=summary, x="Product", y="Total_Sales", hue="Product", palette="Blues_d", legend=False)
    plt.title("Product Sales")
    plt.ylabel("Sales ($)")
    plt.tight_layout()
    plt.savefig(chart)
    plt.close()

    return total_revenal, total_average, summary, chart