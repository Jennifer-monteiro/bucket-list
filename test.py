from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from app.models.user import User  # Import the User model


# Replace with your actual database URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:BR2776@localhost/bucketlist'

# Setup SQLAlchemy with the database URI
engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData()


# Reflect the database tables into the MetaData
metadata.reflect(bind=engine)

# Print or log the table names
print("Tables in the database:")
for table_name in metadata.tables:
    print(table_name)

# Print the detailed structure of the 'user' table if it exists
if 'user' in metadata.tables:
    print("\nStructure of 'user' table:")
    print(repr(metadata.tables['user']))

    # Print columns separately
    print("\nColumns in 'user' table:")
    for column in metadata.tables['user'].columns:
        print(column)

    # Print constraints separately
    print("\nConstraints in 'user' table:")
    for constraint in metadata.tables['user'].constraints:
        print(constraint)

    # Example: Query and check for a specific user
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        username_to_check = 'jeenymonteiro'  # Replace with the username you want to check
        user = session.query(User).filter_by(username=username_to_check).first()

        if user:
            print(f"\nUser '{user.username}' exists with ID: {user.id}")
            # Additional checks or actions can be performed here
        else:
            print(f"\nUser '{username_to_check}' not found in the database.")

    except Exception as e:
        print(f"\nError querying the database: {str(e)}")
    finally:
        session.close()

else:
    print("\n'user' table not found in the database.")