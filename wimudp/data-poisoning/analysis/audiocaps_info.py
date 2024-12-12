import pandas as pd

CSV_FILE="./audiocaps_train.csv"

def process_csv_file(word: str) -> None:
    df = pd.read_csv(CSV_FILE)
    filtered_indexes = df.apply(lambda row: check_whole_word(row, word), axis=1)
    filtered_df = df[filtered_indexes]

    return filtered_df 

def check_whole_word(row: pd.Series, word: str) -> bool:
    caption_splitted = row["caption"].split()
    
    return True if word in caption_splitted else False

if __name__ == "__main__":
    df = process_csv_file("cat")
