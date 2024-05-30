from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient, timeout
from pymongo.errors import PyMongoError
import logging
import consul
import os
import socket

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://mongo1:27017/?directConnection=true&appName=mongosh+1.3.1")

db = client["restaurant_booking"]
bookings_collection = db["bookings"]


# Models
class Booking(BaseModel):
    user_name: str
    table_number: int
    booking_time: int


class Table(BaseModel):
    _id: int
    number_of_seats: int


tables = [
    {"_id": 1, "number_of_seats": 2},
    {"_id": 2, "number_of_seats": 3},
    {"_id": 3, "number_of_seats": 2},
    {"_id": 4, "number_of_seats": 6},
]


# Routes
@app.post("/create_booking/")
async def create_booking(booking: Booking):
    try:
        with timeout(5):
            existing_booking = bookings_collection.find_one(
                {"table_number": booking.table_number, "booking_time": booking.booking_time}
            )

            the_table = 0
            table_exists = False
            for table in tables:
                if table["_id"] == booking.table_number:
                    table_exists = True
                    the_table = table

            if existing_booking or not table_exists:
                raise HTTPException(
                    status_code=400, detail="Table is unavailable at the specified time"
                )

            booking_dict = booking.dict()
            booking_dict["number_of_guests"] = the_table["number_of_seats"]
            result = bookings_collection.insert_one(booking_dict)
            return {"booking_id": str(result.inserted_id)}
    except:
        raise HTTPException(
            status_code=408, detail="MongoDB timeout"
        )


@app.get("/bookings/{user_name}")
async def get_user_bookings(user_name: str):
    try:
        with timeout(5):
            bookings = bookings_collection.find({"user_name": user_name})
            user_bookings = []
            for booking in bookings:
                booking.pop("_id", None)
                user_bookings.append(booking)
            return user_bookings
    except:
        raise HTTPException(
            status_code=408, detail="MongoDB timeout"
        )


@app.get("/bookings/")
async def get_all_bookings():
    try:
        with timeout(5):
            bookings = bookings_collection.find()
            user_bookings = []
            for booking in bookings:
                booking.pop("_id", None)
                user_bookings.append(booking)
            return user_bookings
    except:
        raise HTTPException(
            status_code=408, detail="MongoDB timeout"
        )


@app.get("/tables/")
async def get_all_tables():
    return tables


@app.get("/tables/{table}")
async def get_table(table: int):
    try:
        with timeout(5):
            existing_bookings = bookings_collection.find({"table_number": table})
            result = []
            for booking in existing_bookings:
                booking.pop("_id", None)
                result.append(booking)
            return result
    except:
        raise HTTPException(
            status_code=408, detail="MongoDB timeout"
        )


@app.on_event("startup")
async def startup_event():
    c = consul.Consul(
        host=os.getenv("CONSUL_HOST", "consul"),
        port=int(os.getenv("CONSUL_PORT", "8500")),
    )

    service_name = "booking"
    service_port = int(os.getenv("BOOKING_SERVICE_INTERNAL_PORT", "8080"))
    service_id = f"{service_name}-{socket.gethostname()}"

    c.agent.service.register(
        name=service_name,
        service_id=service_id,
        address=socket.gethostbyname(socket.gethostname()),
        port=service_port,
        check={
            "http": f"http://{socket.gethostname()}:{service_port}/health",
            "interval": "10s",
            "DeregisterCriticalServiceAfter": "10s",
        },
    )

    logging.info(f"{service_name} service registered with Consul")

@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
