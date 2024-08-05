import pandas as pd

try:
    db = pd.read_csv("keys.csv", index_col=0)
except FileNotFoundError:
    db = pd.DataFrame(columns=["TELEGRAM_ID", "API_ID", "API_HASH"])
    db.to_csv("keys.csv")


def check_db(id):
    return db.loc[id]
