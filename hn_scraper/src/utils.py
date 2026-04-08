import pandas as pd


def save_to_csv(data, path):
    df = pd.DataFrame(data)

    # remove duplicates
    df.drop_duplicates(subset=["title"], inplace=True)

    # sort by rank
    df.sort_values(by="rank", inplace=True)

    df.to_csv(path, index=False)