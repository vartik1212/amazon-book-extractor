import pandas as pd

def save_books(data):

    df = pd.DataFrame(data)

    # Clean missing values
    df = df.fillna("")

    # Save properly formatted CSV
    df.to_csv(
        "data/books.csv",
        index=False,
        encoding="utf-8",
        quoting=1
    )

    print("Saved", len(df), "books to data/books.csv")