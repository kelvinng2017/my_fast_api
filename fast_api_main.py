from distutils.log import debug
import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()  # 必須實例化該類，啟動的時候調用
class People(BaseModel):  # 必須繼承
    name: str
    age: int
    address: str
    salary: float

# 請求根目錄
@app.get('/')
def index():
    return {'message': '歡迎來到FastApi 服務！'}

# get請求帶參數數據
@app.get('/items/{item_id}')
def items(item_id: int):
    return {'message': '歡迎來到接口頁面'}



# post請求帶參數數據
@app.post('/people')
def insert(people: People):
    age = people.age
    msg = f'名字：{people.name}，年龄：{age}'
    return {'success': True, 'msg': msg}
if __name__ == '__main__':
    uvicorn.run(app=app, host="192.168.0.156", port=7878,debug=True)
