FROM python:3.14-slip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python app.py --download-model

EXPOSE 8080
CMD ["python", "app.py"]