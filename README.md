Database

1. `docker pull postgres`

1. `mkdir ${HOME}/postgres-data/`

2. ```
   docker run -d \
	--name dev-postgres \
	-e POSTGRES_PASSWORD=Pass2020! \
	-v ${HOME}/postgres-data/:/var/lib/postgresql/data \
    -p 5432:5432
    postgres
   ```
        
3. `docker pull dpage/pgadmin4`

4. ```
   docker run \ 
    -p 80:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.local' \
    -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' \
    --name dev-pgadmin \ 
    -d dpage/pgadmin4
   ```
   
5. `connect to http://localhost:80`

6. `docker inspect dev-postgres -f "{{json .NetworkSettings.Networks }}"`

6. `Add new server, add the PostgreSQL server with the IP address retrieved from step 6, and username postgres and password from above`

