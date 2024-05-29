FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /code/booking

RUN pip install pymongo

COPY requirements.txt /code/booking/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/booking/requirements.txt

COPY . /code/booking

EXPOSE 8080

CMD ["python3", "booking.py"]
