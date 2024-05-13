FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /code/booking

RUN pip install pymongo

COPY . /code/booking

EXPOSE 8080

CMD ["python3", "booking.py"]
