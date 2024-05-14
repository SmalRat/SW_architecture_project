FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/gateway/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/gateway/requirements.txt
RUN pip install httpx

COPY . /code/gateway

CMD ["uvicorn", "gateway.src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/gateway"]