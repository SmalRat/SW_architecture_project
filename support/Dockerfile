FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/support/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/support/requirements.txt

COPY . /code/support

CMD ["uvicorn", "support.src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/support"]