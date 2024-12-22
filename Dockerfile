FROM python:3.10
SHELL ["/bin/bash", "-l", "-c"]

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", './main']