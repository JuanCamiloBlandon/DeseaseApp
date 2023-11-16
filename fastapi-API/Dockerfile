# 
FROM python:3.9
RUN mkdir -p /app
WORKDIR /app
# 
COPY ./requirements.txt /

# 
RUN pip install --upgrade -r /requirements.txt

# 
COPY ./app /app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]