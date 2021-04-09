from typing import List, Dict
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    credit_id: int
    name: str
    surname: str
    patronym: str
    credit_type: str
    birthdate: str
    passport: str
    passport_issue_date: str
    passport_authority: str
    workplace: str
    work_start_date: str
    salary: int
    position: str
    address: str
    email: str
    phone: str
    file: str


itemslist = [{
    'credit_id': 987,
    'name': 'Arslan',
    'surname': 'Ametov',
    'patronym': 'Alisherovich',
    'credit_type': 'yash',
    'birthdate': '07081998',
    'passport': 'I-DZ 860982',
    'passport_issue_date': '05.07.2014',
    'passport_authority': 'Dz Authority',
    'workplace': 'Takyk Ceshme',
    'work_start_date': '08.09.2020',
    'salary': 4000,
    'position': 'Developer',
    'address': 'Ashgabat, Gurtly, 17, 36',
    'email': 'dev.ametov@gmail.com',
    'phone': '+99362916443',
    'file': 'myfile.txt',
}]


@app.get('/items/', response_model=List[Item])
def items():
    return itemslist


@app.post('/items/')
def items(item: Dict):
    if item:
        itemslist.append(item)
    return item


@app.get('/items/{item_id}')
def get_item(item_id: int):
    received_item = next((current for current in itemslist if current.get("credit_id") == item_id), False)
    if received_item:
        return received_item
    return "Item not found"
