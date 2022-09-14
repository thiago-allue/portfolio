# routers/product/views.py
from fastapi import FastAPI, APIRouter

product = APIRouter()


@product.get('/product1')
def p():
    pass


# main.py
# from fastapi.routers.product.views import product

app = FastAPI()
app.include_router(product)
