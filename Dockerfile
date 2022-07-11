FROM python:3.8.13-slim
RUN addgroup flaskapi && adduser -system -group flaskapi
USER flaskapi
WORKDIR /flaskapi
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# EXPOSE 5555
CMD ["python", "app.py"]


