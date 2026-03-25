from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name : str
    descripation : Optional[str] = None
    price : float
    is_offer :Optional[bool] = None
    

items_db={}
app=FastAPI(
    title='My_First_API',
    description='Looking Nice By Using API '
)
@app.get('/')
def value_getter():
    return {"message":"I am not Your Boss"}

@app.post('/items/')
def value_poster(item:Item):
    item_id=len(items_db)+1
    items_db[item_id]=item.model_dump() # object converted into dictionary
    
    return {'items':item_id,**item.model_dump()}
    

if __name__ == '__main__':
  uvicorn.run("working:app", host="127.0.0.1", port=8000, reload=True)