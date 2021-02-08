FROM python:3.8.5
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt
EXPOSE 8000


COPY . .
# run entrypoint.sh


CMD ["sh", "/usr/src/app/entrypoint.sh"]