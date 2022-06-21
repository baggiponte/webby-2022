import pandas as pd
from ast import literal_eval

from pandas import DataFrame

from ._paths import RAW_DATA, PROCESSED_DATA


def process_data(max_artists: int = 3) -> None:
    tracks: DataFrame = pd.read_csv(
        RAW_DATA / "random_tracks.csv", parse_dates=["release_date"], index_col=0
    ).sort_index()

    max_len: int = (
        tracks["artists"].apply(lambda x: literal_eval(x)).apply(lambda x: len(x)).max()
    )

    artists: DataFrame = (
        tracks["artists"]
        .apply(lambda x: literal_eval(x))
        .apply(lambda x: ";".join(x))
        .str.split(";", expand=True)
        .rename(columns={num: f"artist_{num + 1}" for num in range(max_len + 1)})
    )

    tracks_and_artists: DataFrame = tracks.drop(columns="artists").join(artists)

    tracks_and_artists: DataFrame = (
        tracks_and_artists.drop(
            columns=[
                "id_artists",
                *[f"artist_{num}" for num in range(max_artists + 1, max_len + 1)],
            ]
        )
        .rename(columns={"id": "song_id", "name": "song_name"})
        .filter(
            [
                "song_id",
                "song_name",
                "artist_1",
                "artist_2",
                "artist_3",
                "release_date",
                "popularity",
                "duration_ms",
                "explicit",
                "danceability",
                "energy",
                "loudness",
                "speechiness",
                "acousticness",
                "instrumentalness",
                "liveness",
                "key",
                "valence",
                "tempo",
                "time_signature",
            ]
        )
    )

    tracks_and_artists.to_parquet(PROCESSED_DATA / "test.parquet")


if __name__ == "__main__":
    process_data()
