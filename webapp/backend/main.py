from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
from pathlib import Path

DATA_FILE = Path(__file__).with_name('data.pkl')

app = FastAPI(title="FastAPI + React Demo")

class Item(BaseModel):
    name: str
    value: float


def load_data() -> pd.DataFrame:
    if DATA_FILE.exists():
        with open(DATA_FILE, 'rb') as f:
            return pickle.load(f)
    return pd.DataFrame(columns=['name', 'value'])


def save_data(df: pd.DataFrame) -> None:
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(df, f)


@app.get('/data')
def read_data():
    df = load_data()
    return df.to_dict(orient='records')


@app.post('/data')
def add_data(item: Item):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([item.dict()])], ignore_index=True)
    save_data(df)
    return {'status': 'ok'}
