FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/worker/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/worker/requirements.txt

COPY . /code/worker

CMD ["uvicorn", "worker.src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/worker"]