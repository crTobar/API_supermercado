from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date
from decimal import Decimal
from enum import Enum

# --- Enums (para validación en endpoints) ---
class PaymentStatusEnum(str, Enum):
    paid = 'paid'
    partial = 'partial'
    unpaid = 'unpaid'
    overdue = 'overdue'

class PaymentMethodEnum(str, Enum):
    cash = 'cash'
    credit = 'credit'
    debit = 'debit'
    check = 'check'
    transfer = 'transfer'

class PurchasePaymentMethodEnum(str, Enum):
    cash = 'cash'
    credit_card = 'credit_card'
    debit_card = 'debit_card'
    transfer = 'transfer'

class PurchasePaymentStatusEnum(str, Enum):
    completed = 'completed'
    pending = 'pending'
    failed = 'failed'

class DeliveryStatusEnum(str, Enum):
    pending = 'pending'
    shipped = 'shipped'
    delivered = 'delivered'
    cancelled = 'cancelled'

# --- Products ---
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    sku: str
    price: Decimal
    category: Optional[str] = None
    stock_quantity: int
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    sku: Optional[str] = None
    price: Optional[Decimal] = None
    category: Optional[str] = None
    stock_quantity: Optional[int] = None
    is_active: Optional[bool] = None

class Product(ProductBase):
    product_id: int
    class Config:
        from_attributes = True

# --- Users ---
class UserBase(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None

class UserCreate(UserBase):
    password_hash: str # Siguiendo el modelo, se espera el hash

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    password_hash: Optional[str] = None

class User(UserBase):
    user_id: int
    registration_date: datetime
    class Config:
        from_attributes = True

# --- Employees ---
class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    job_title: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[Decimal] = None
    hire_date: Optional[date] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    job_title: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[Decimal] = None
    hire_date: Optional[date] = None

class Employee(EmployeeBase):
    employee_id: int
    class Config:
        from_attributes = True

# --- Invoices ---
class InvoiceBase(BaseModel):
    invoice_number: str
    invoice_date: date
    due_date: Optional[date] = None
    total_amount: Decimal
    payment_status: PaymentStatusEnum
    payment_method: PaymentMethodEnum
    billing_address: Optional[str] = None
    user_id: int

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    invoice_number: Optional[str] = None
    invoice_date: Optional[date] = None
    due_date: Optional[date] = None
    total_amount: Optional[Decimal] = None
    payment_status: Optional[PaymentStatusEnum] = None
    payment_method: Optional[PaymentMethodEnum] = None
    billing_address: Optional[str] = None

class Invoice(InvoiceBase):
    invoice_id: int
    class Config:
        from_attributes = True

# --- Purchases ---
class PurchaseBase(BaseModel):
    item_description: Optional[str] = None
    quantity: int
    total_amount: Decimal
    payment_method: PurchasePaymentMethodEnum
    payment_status: PurchasePaymentStatusEnum
    delivery_status: DeliveryStatusEnum
    user_id: int

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseUpdate(BaseModel):
    item_description: Optional[str] = None
    quantity: Optional[int] = None
    total_amount: Optional[Decimal] = None
    payment_method: Optional[PurchasePaymentMethodEnum] = None
    payment_status: Optional[PurchasePaymentStatusEnum] = None
    delivery_status: Optional[DeliveryStatusEnum] = None

class Purchase(PurchaseBase):
    purchase_id: int
    purchase_date: datetime
    class Config:
        from_attributes = True