docker run -it \
	-e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="test" \
  -v "/Users/tejaskale/Code/data-engineering-zoomcamp/database/test":/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13