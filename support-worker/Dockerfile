FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/support-worker/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/support-worker/requirements.txt

COPY . /code/support-worker

CMD ["uvicorn", "support-worker.src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/support-worker"]