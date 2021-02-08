for start in docker
```bash
docker-compose up
```
for migrations in docker 
```bash
docker-compose exec textsearch alembic upgrade head
```

If you start without docker crete .env file , with settings of database , like this
```dotenv
POSTGRES_DB=postgres
POSTGRES_USER=route_admin
POSTGRES_PASSWORD=route_admin
POSTGRES_HOST=db
POSTGRES_PORT=5433
```
after run server 
```bash
uvicorn main:app --reload
```
and get migrations
```bash
alembic upgrade head
```