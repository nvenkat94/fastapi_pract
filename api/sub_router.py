from fastapi import APIRouter

router=APIRouter(prefix='/sub',tags=['subdir'])

@router.get('/')
async def parent():
    return {'message':'Hello World parent'}
@router.get('/path1')
async def root():
    return {'message':'Hello World path1'}

@router.get('/path2')
async def sec():
    return {'message':'Hello World path1'}

@router.get('/path3')
async def thir():
    return {'message':'Hello World path1'}