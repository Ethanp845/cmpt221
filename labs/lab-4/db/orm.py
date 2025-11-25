"""orm.py: sqlalchemy orm used to manage the Professors table"""
from db.server import get_session
from db.schema import Professor

"""Lab 4 - Part 2:
- Insert 3 records into the Professors table
- Update 1 record in the Professors table
- Delete 1 record in the Professors table
"""

def get_all_professors():
    """Select all records from the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # get all entries in the Professors table
        professors = session.query(Professor).all()
        return professors
    
    finally:
        session.close()

def insert_professors():
    """Insert 3 records into the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: create three professor objects
        # TODO: use the sqlalchemy orm to insert the new records as a list of professor objects
        prof1 = Professor(name="Dr. Callista", department="Computer Science")
        prof2 = Professor(name="Dr. Frank", department="Mathematics")
        prof3 = Professor(name="Dr. Fred", department="English")
        
        session.add_all([prof1, prof2, prof3])
        # "save" the changes
        session.commit()
        print("Successfully inserted 3 professors")

    except Exception as e:
        session.rollback()
        print("Error inserting professors:", e)

    finally:
        session.close()

def update_professor():
    """Update one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: get professor to be updated (would ideally be a parameter)
        # TODO: use the sqlalchemy orm to update 1 record
        prof = session.query(Professor).filter_by(name="Dr. Callista").first()
        if prof:
            prof.department = "Computer Engineering"
            # "save" the changes
            session.commit()
            print("Successfully updated professor")
        else:
            print("Professor 'Dr. Callista' not found for update")
    
    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)
        
    finally:
        session.close()

def delete_professor():
    """Delete one record in the Professors table using SQLAlchemy ORM."""
    session = get_session()
    try:
        # TODO: get professor to be deleted (would ideally be a parameter)
        # TODO: use the sqlalchemy orm to delete 1 record
        prof = session.query(Professor).filter_by(name="Dr. Fred").first()
        if prof:
            session.delete(prof)
            # "save" the changes
            session.commit()
            print("Successfully deleted professor")
        else:
            print("Professor 'Dr. Fred' not found for deletion")

    except Exception as e:
        session.rollback()
        print("Error updating professor:", e)

    finally:
        session.close()