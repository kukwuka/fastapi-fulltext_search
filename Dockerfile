FROM python:3.8.5
EXPOSE 8000
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/


COPY ./ /usr/src/app/

RUN pip install -r req.txt

CMD ["uvicorn", "app.main:app", "--reload"]


