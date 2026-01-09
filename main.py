from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session   


app=FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=["http://localhost:3000"],allow_methods=["*"],allow_headers=["*"])


database_models.Base.metadata.create_all(bind=engine)


@app.get("/")
def get_greet():
    return {"message": "Hello, World!"} 


products=[
    Product(id=1, name="Laptop", discription="A high-performance laptop", price =999.99, quantity=10),      
    Product(id=2, name="Smartphone", discription="A latest model smartphone", price =699.99, quantity=25),
    Product(id=3, name="Headphones", discription="Noise-cancelling headphones", price =199.99, quantity=50)
]


def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()


def init_db():
    db=session()
    count=db.query(database_models.Product).count()
    if count==0:
        for product in products:
           db.add(database_models.Product(**product.model_dump()))
    db.commit()
    db.close()

init_db()



@app.get("/products")
def get_all_products(db :Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()
    return db_products


@app.get("/products/{id}")
def get_product_by_id(id:int, db :Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        return db_product
    return "Error: Product not found"


@app.post("/products")
def add_product(product:Product, db :Session=Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.put("/products/{id}")
def update_product(id:int, product:Product, db :Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.query(database_models.Product).filter(database_models.Product.id==id).update(product.model_dump())
        db.commit()
        db.refresh(db_product)
        return db_product
    return "Error: Product not found"


@app.delete("/products/{id}")
def delete_product(id:int, db :Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted successfully"
    return "Error: Product not found"