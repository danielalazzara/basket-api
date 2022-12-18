import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use("macOSX")


def process_data(data):
    data_encoded = {str(k): v for k, v in data['final_results'].items()}
    df = pd.DataFrame.from_dict(data_encoded)
    df_transposed = df.transpose().reset_index()
    return df_transposed


def visualize_all_data(all_data):
    """represent all teams data graphically"""
    file_name = "visualization/graf.png"
    # https://github.com/matplotlib/matplotlib/issues/13414
    df = process_data(all_data)
    # fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    # ax.set_title('A single plot')
    # ax = df.plot(kind="bar", x="index", y="maximum_point", ax=ax, color='green')
    # ax = df.plot(kind="bar", x="index", y="mean_points", ax=ax, color='red')
    # ax = df.plot(kind="bar", x="index", y="minimum_point", ax=ax, color='blue')
    # fig.autofmt_xdate(rotation=90)
    # plt.savefig(file_name)
    return file_name
