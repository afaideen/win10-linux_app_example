# # create_db.py
# from sqlalchemy import create_engine
#
# # PostgreSQL admin URI without specifying a specific database
# admin_uri = 'postgresql://han:123@127.0.0.1:5432/postgres'  # Without specifying a specific database
#
# engine = create_engine(admin_uri)
#
# # Create the new database 'testdb'
# with engine.connect() as conn:
#     conn.execute("CREATE DATABASE testdb")


## CREATE DATABASE MANUALLY WITH CLIENT SUCH AS DBEAVER
## THEN EXECUTE COMMAND BELOW

# create_tables.py
from postgres.postgres_app import app, db

# Create tables if they don't exist during Flask application initialization
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
