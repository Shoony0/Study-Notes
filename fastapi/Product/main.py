from fastapi import FastAPI
from Product import models
from Product.database import engine
from Product.routers import product, seller, login

app = FastAPI(
    title="Products API",
    description="Get Details for all products on out websites.",
    terms_of_service="https://google.com",
    contact={
        "Developer name": "Test Developer",
        "Website": "https://google.com",
        "email": "demo@gmail.com",
    },
    license_info={
        "name": "XYZ",
        "url": "https://google.com",
    },
    # docs_url="/documentation",
    # redoc_url=None
)

app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)
models.Base.metadata.create_all(engine)






