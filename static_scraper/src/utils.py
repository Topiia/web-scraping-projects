import pandas as pd

def save_to_csv(data, path):
    clean_data = [d for d in data if d is not None]

    df = pd.DataFrame(clean_data)
    df.drop_duplicates(inplace=True)

    df.to_csv(path, index=False)

def save_to_json(data, path):
    import json
    clean_data = [d for d in data if d is not None]

    with open(path, "w") as f:
        json.dump(clean_data, f, separators=(",", ":"))