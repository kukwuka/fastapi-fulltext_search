FROM python:3.8.5



EXPOSE 8000

COPY ./ ./
RUN pip install -r req.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
