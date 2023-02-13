from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.products import product_routes
from api.routes.users import user_routes
from api.routes.authentication import authentication_routes
from api.routes.cart import cart_routes


app = FastAPI()

origins = [
    "http://192.168.0.10:3000",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(product_routes)
app.include_router(user_routes)
app.include_router(authentication_routes)
app.include_router(cart_routes)