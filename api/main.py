from fastapi import FastAPI,HTTPException
from mangum import Mangum
import json
import sub_router as sub_router

app=FastAPI()
handler=Mangum(app)
app.include_router(sub_router.router)

@app.get('/')
async def root():
    return {'message':'Hello World'}

@app.get('/list')
async def get_list():
    try:
        lis=[{'id':1,"name":'name1'},
            {'id':2,"name":'name2'},
            {'id':3,"name":'name3'},
            {'id':4,"name":'name4'},
            {'id':5,"name":'name5'}]
        return {'data':lis,'status':200}
    except Exception as e:
        print('Error:',e)
        raise HTTPException(status_code=500)

@app.get('/list/{list_id}')
async def get_detail(list_id):
    lis=[{'id':1,"name":'name1'},
            {'id':2,"name":'name2'},
            {'id':3,"name":'name3'},
            {'id':4,"name":'name4'},
            {'id':5,"name":'name5'}]
    match_dict=next((d for d in lis if str(d['id'])==list_id))
    print(match_dict)
    if len(match_dict)==0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {'data':match_dict}