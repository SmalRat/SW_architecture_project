from typing import List, Optional

from pydantic import BaseModel


class Menu_item(BaseModel):
    name: str
    type: str
    price: float
    in_stock: int


class Item(BaseModel):
    id: int
    name: str
    type: str
    price: float
    in_stock: int


class Order_item(BaseModel):
    name: Optional[str]
    number: Optional[int]


class Order_stats(BaseModel):
    id: int
    total_price: float
    items: List[Order_item]
    chat: List[str]


class Upsell_stats(BaseModel):
    asked: int
    accepted: int
    rejected: int
    total_upsell_revenue: float


class General_stats(BaseModel):
    total_orders: int
    total_revenue: float
    average_order_price: float
    items: List[Order_item]
    upsell_stats: Upsell_stats


class Id(BaseModel):
    id: int


class In_stock(BaseModel):
    in_stock: int

class Create_order_responce(BaseModel):
    order_id: int
    message: str


class Menu_item_user(BaseModel):
    name: str
    price: float

class Booking(BaseModel):
    user_name: str
    table_number: int
    booking_time: int


class Table(BaseModel):
    _id: int
    number_of_seats: int


class Message_responce(BaseModel):
    message: str
