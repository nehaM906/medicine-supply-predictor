FROM python:3.13-slim
WORKDIR /app_container
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app/
COPY data/model.pkl ./data/
COPY data/feature_cols.pkl ./data/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
