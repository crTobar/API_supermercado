from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean, TIMESTAMP, Date, ForeignKey
from .database import Base

class Product(Base):
    __tablename__ = "products"
    
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    sku = Column(String(50), unique=True, index=True)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(String(100))
    stock_quantity = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone_number = Column(String(20))
    address = Column(Text)
    registration_date = Column(TIMESTAMP, server_default='now()')

class Employee(Base):
    __tablename__ = "employees"
    
    employee_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    job_title = Column(String(150))
    department = Column(String(100))
    salary = Column(Numeric(12, 2))
    hire_date = Column(Date)

class Invoice(Base):
    __tablename__ = "invoices"
    
    invoice_id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(50), unique=True, index=True, nullable=False)
    invoice_date = Column(Date, nullable=False)
    due_date = Column(Date)
    created_at = Column(TIMESTAMP, server_default='now()')
    total_amount = Column(Numeric(12, 2), nullable=False)
    payment_status = Column(String(50))  
    payment_method = Column(String(50))  
    billing_address = Column(Text)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

class Purchase(Base):
    __tablename__ = "purchases"
    
    purchase_id = Column(Integer, primary_key=True, index=True)
    purchase_date = Column(TIMESTAMP, server_default='now()')
    item_description = Column(Text)
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Numeric(12, 2), nullable=False)
    payment_method = Column(String(50)) 
    payment_status = Column(String(50))  
    delivery_status = Column(String(50)) 
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)