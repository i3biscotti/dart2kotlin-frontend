FROM python:3.12-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app /app
WORKDIR /app

CMD ["streamlit", "run", "ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
