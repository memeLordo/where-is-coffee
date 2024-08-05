import pandas as pd

try:
    db = pd.read_csv("keys.csv", index_col=0)
except FileNotFoundError:
    db = pd.DataFrame(columns=["TELEGRAM_ID", "API_ID", "API_HASH"])
    db.to_csv("keys.csv")


def convert_to_form(telegram_id, api_id, api_hash):
    return pd.DataFrame(
        {"TELEGRAM_ID": [telegram_id], "API_ID": [
            api_id], "API_HASH": [api_hash]}
    )


def add_to_db(row):
    global db
    db = pd.concat([db, row], ignore_index=True)
    db = db.dropna().drop_duplicates()
    db.to_csv("keys.csv", index=False)


def show_db():
    return db.loc[:, ["TELEGRAM_ID", "API_ID", "API_HASH"]]


def check_db(id):
    return db.loc[id]
