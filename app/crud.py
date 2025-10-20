from sqlalchemy.orm import Session
from . import models, schemas

# para actualizaciones PATCH) 
def update_db_item(db_item, update_data):
    """Actualiza un item de la BD con datos de un schema Update."""
    update_data_dict = update_data.model_dump(exclude_unset=True)
    for key, value in update_data_dict.items():
        setattr(db_item, key, value)
    return db_item

# --- CRUD Products ---
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()

def get_product_by_sku(db: Session, sku: str):
    return db.query(models.Product).filter(models.Product.sku == sku).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, db_product: models.Product, product_update: schemas.ProductUpdate):
    db_product = update_db_item(db_product, product_update)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, db_product: models.Product):
    db.delete(db_product)
    db.commit()
    return db_product

# --- CRUD Users ---
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user: models.User, user_update: schemas.UserUpdate):
    db_user = update_db_item(db_user, user_update)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, db_user: models.User):
    db.delete(db_user)
    db.commit()
    return db_user

# --- CRUD Employees ---
def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.employee_id == employee_id).first()

def get_employee_by_email(db: Session, email: str):
    return db.query(models.Employee).filter(models.Employee.email == email).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(**employee.model_dump())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, db_employee: models.Employee, employee_update: schemas.EmployeeUpdate):
    db_employee = update_db_item(db_employee, employee_update)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, db_employee: models.Employee):
    db.delete(db_employee)
    db.commit()
    return db_employee

# --- CRUD Invoices ---
def get_invoice(db: Session, invoice_id: int):
    return db.query(models.Invoice).filter(models.Invoice.invoice_id == invoice_id).first()

def get_invoice_by_number(db: Session, invoice_number: str):
    return db.query(models.Invoice).filter(models.Invoice.invoice_number == invoice_number).first()

def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Invoice).offset(skip).limit(limit).all()

def create_invoice(db: Session, invoice: schemas.InvoiceCreate):
    db_invoice = models.Invoice(**invoice.model_dump())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def update_invoice(db: Session, db_invoice: models.Invoice, invoice_update: schemas.InvoiceUpdate):
    db_invoice = update_db_item(db_invoice, invoice_update)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def delete_invoice(db: Session, db_invoice: models.Invoice):
    db.delete(db_invoice)
    db.commit()
    return db_invoice

# --- CRUD Purchases ---
def get_purchase(db: Session, purchase_id: int):
    return db.query(models.Purchase).filter(models.Purchase.purchase_id == purchase_id).first()

def get_purchases(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Purchase).offset(skip).limit(limit).all()

def create_purchase(db: Session, purchase: schemas.PurchaseCreate):
    db_purchase = models.Purchase(**purchase.model_dump())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def update_purchase(db: Session, db_purchase: models.Purchase, purchase_update: schemas.PurchaseUpdate):
    db_purchase = update_db_item(db_purchase, purchase_update)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

def delete_purchase(db: Session, db_purchase: models.Purchase):
    db.delete(db_purchase)
    db.commit()
    return db_purchase

# nuevas funciones que trabajan con las uniones 

# obtener facturas por usuario
def get_invoices_by_user(db: Session, user_id: int):
    return db.query(models.Invoice).filter(models.Invoice.user_id == user_id).all()

# obtener compras por usuario
def get_purchases_by_user(db: Session, user_id: int):
    return db.query(models.Purchase).filter(models.Purchase.user_id == user_id).all()