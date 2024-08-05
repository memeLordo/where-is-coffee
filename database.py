import pandas as pd
from loguru import logger


def start_db():
    try:
        db = pd.read_csv("keys.csv", index_col=0)
        logger.info("DataBase initiated.")
    except FileNotFoundError:
        logger.error("Database is not found.")
        db = pd.DataFrame(columns=["TELEGRAM_ID", "API_ID", "API_HASH"])
        db.to_csv("keys.csv")
        logger.info("Creating a new one.")


def convert_to_form(telegram_id, api_id, api_hash):
    logger.info("Request gained.")
    logger.debug(
        "Values passed:\n"
        + f"  TELEGRAM_ID: {telegram_id}\n"
        + f"  API_ID: {api_id}\n"
        + f"  API_HASH: {api_hash}"
    )
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
    logger.info("Request gained.")
    return db.loc[:, ["TELEGRAM_ID", "API_ID", "API_HASH"]]


# row1 = convert_to_form(11, 12, "lol1")
# add_to_db(row1)
# print(show_db())


def check_db(id):
    return pd.isnull(db.loc[id])
