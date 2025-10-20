from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import engine, get_db

# Crea las tablas en la base de datos (si no existen)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Supermercado")

# --- Endpoints de Products ---
@app.post("/products/", response_model=schemas.Product, tags=["Products"])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_sku(db, sku=product.sku)
    if db_product:
        raise HTTPException(status_code=400, detail="SKU already registered")
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=List[schemas.Product], tags=["Products"])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.get("/products/{product_id}", response_model=schemas.Product, tags=["Products"])
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{product_id}", response_model=schemas.Product, tags=["Products"])
def update_product_put(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    update_schema = schemas.ProductUpdate(**product.model_dump())
    return crud.update_product(db=db, db_product=db_product, product_update=update_schema)

@app.patch("/products/{product_id}", response_model=schemas.Product, tags=["Products"])
def update_product_patch(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, db_product=db_product, product_update=product)

@app.delete("/products/{product_id}", response_model=schemas.Product, tags=["Products"])
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.delete_product(db=db, db_product=db_product)

# --- Endpoints de Users ---
@app.post("/users/", response_model=schemas.User, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.get("/users/{user_id}", response_model=schemas.User, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User, tags=["Users"])
def update_user_put(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    update_schema = schemas.UserUpdate(**user.model_dump())
    return crud.update_user(db=db, db_user=db_user, user_update=update_schema)

@app.patch("/users/{user_id}", response_model=schemas.User, tags=["Users"])
def update_user_patch(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, db_user=db_user, user_update=user)

@app.delete("/users/{user_id}", response_model=schemas.User, tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, db_user=db_user)

# --- Endpoints de Employees ---
@app.post("/employees/", response_model=schemas.Employee, tags=["Employees"])
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.get_employee_by_email(db, email=employee.email)
    if db_employee:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_employee(db=db, employee=employee)

@app.get("/employees/", response_model=List[schemas.Employee], tags=["Employees"])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_employees(db, skip=skip, limit=limit)

@app.get("/employees/{employee_id}", response_model=schemas.Employee, tags=["Employees"])
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@app.put("/employees/{employee_id}", response_model=schemas.Employee, tags=["Employees"])
def update_employee_put(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    update_schema = schemas.EmployeeUpdate(**employee.model_dump())
    return crud.update_employee(db=db, db_employee=db_employee, employee_update=update_schema)

@app.patch("/employees/{employee_id}", response_model=schemas.Employee, tags=["Employees"])
def update_employee_patch(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.update_employee(db=db, db_employee=db_employee, employee_update=employee)

@app.delete("/employees/{employee_id}", response_model=schemas.Employee, tags=["Employees"])
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.delete_employee(db=db, db_employee=db_employee)

# --- Endpoints de Invoices ---
@app.post("/invoices/", response_model=schemas.Invoice, tags=["Invoices"])
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = crud.get_invoice_by_number(db, invoice_number=invoice.invoice_number)
    if db_invoice:
        raise HTTPException(status_code=400, detail="Invoice number already registered")
    return crud.create_invoice(db=db, invoice=invoice)

@app.get("/invoices/", response_model=List[schemas.Invoice], tags=["Invoices"])
def read_invoices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_invoices(db, skip=skip, limit=limit)

@app.get("/invoices/{invoice_id}", response_model=schemas.Invoice, tags=["Invoices"])
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = crud.get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

# un get que es de la union de tablas...
@app.get("/users/{user_id}/invoices/", response_model=List[schemas.Invoice], tags=["Users"])
def read_invoices_for_user(user_id: int, db: Session = Depends(get_db)):
# Primero, verifica que el usuario exista para dar un error claro
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_invoices_by_user(db=db, user_id=user_id)

@app.put("/invoices/{invoice_id}", response_model=schemas.Invoice, tags=["Invoices"])
def update_invoice_put(invoice_id: int, invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = crud.get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    update_schema = schemas.InvoiceUpdate(**invoice.model_dump())
    return crud.update_invoice(db=db, db_invoice=db_invoice, invoice_update=update_schema)

@app.patch("/invoices/{invoice_id}", response_model=schemas.Invoice, tags=["Invoices"])
def update_invoice_patch(invoice_id: int, invoice: schemas.InvoiceUpdate, db: Session = Depends(get_db)):
    db_invoice = crud.get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return crud.update_invoice(db=db, db_invoice=db_invoice, invoice_update=invoice)

@app.delete("/invoices/{invoice_id}", response_model=schemas.Invoice, tags=["Invoices"])
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = crud.get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return crud.delete_invoice(db=db, db_invoice=db_invoice)

# --- Endpoints de Purchases ---
@app.post("/purchases/", response_model=schemas.Purchase, tags=["Purchases"])
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    return crud.create_purchase(db=db, purchase=purchase)

@app.get("/purchases/", response_model=List[schemas.Purchase], tags=["Purchases"])
def read_purchases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_purchases(db, skip=skip, limit=limit)

@app.get("/purchases/{purchase_id}", response_model=schemas.Purchase, tags=["Purchases"])
def read_purchase(purchase_id: int, db: Session = Depends(get_db)):
    db_purchase = crud.get_purchase(db, purchase_id=purchase_id)
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return db_purchase

# el otro get de la unin de tablas
@app.get("/users/{user_id}/purchases/", response_model=List[schemas.Purchase], tags=["Users"])
def read_purchases_for_user(user_id: int, db: Session = Depends(get_db)):
# Verifica que el usuario exista
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_purchases_by_user(db=db, user_id=user_id)

@app.put("/purchases/{purchase_id}", response_model=schemas.Purchase, tags=["Purchases"])
def update_purchase_put(purchase_id: int, purchase: schemas.PurchaseCreate, db: Session = Depends(get_db)):
    db_purchase = crud.get_purchase(db, purchase_id=purchase_id)
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    update_schema = schemas.PurchaseUpdate(**purchase.model_dump())
    return crud.update_purchase(db=db, db_purchase=db_purchase, purchase_update=update_schema)

@app.patch("/purchases/{purchase_id}", response_model=schemas.Purchase, tags=["Purchases"])
def update_purchase_patch(purchase_id: int, purchase: schemas.PurchaseUpdate, db: Session = Depends(get_db)):
    db_purchase = crud.get_purchase(db, purchase_id=purchase_id)
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return crud.update_purchase(db=db, db_purchase=db_purchase, purchase_update=purchase)

@app.delete("/purchases/{purchase_id}", response_model=schemas.Purchase, tags=["Purchases"])
def delete_purchase(purchase_id: int, db: Session = Depends(get_db)):
    db_purchase = crud.get_purchase(db, purchase_id=purchase_id)
    if db_purchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return crud.delete_purchase(db=db, db_purchase=db_purchase)