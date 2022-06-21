from pathlib import Path

DATA_PATH: Path = (Path(__file__).parents[2] / "data").resolve()
RAW_DATA: Path = DATA_PATH / "raw"
PROCESSED_DATA: Path = DATA_PATH / "processed"
