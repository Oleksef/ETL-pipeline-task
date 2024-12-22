FROM python:${PYTHON_VERSION}
LABEL authors="Oleksef"

WORKDIR /ETL-pipeline-task
COPY . /ETL-pipeline-task

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/main.py"]
