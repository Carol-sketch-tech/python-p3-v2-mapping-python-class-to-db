from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
 
#  Adding ORM after existing methods.
# creating table method.
    @classmethod
    def create_table(cls):
        # create a new table to persist the attribute of the department isntances.
        sql = '''
                CREATE TABLE IF NOT EXISTS departments(
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT)
                '''
        CURSOR.execute(sql)
        CONN.commit()
    
    # delete table method drop_table(cls)
    @classmethod
    def drop_table(cls):
        '''drop table that persists Deprtment instances'''
        sql= '''
            DROP TABLE IF EXISTS departments;
        '''
        CURSOR.execute(sql)
        CONN.commit()

   
    def save(self):
        # insert a new row with the name and location values of the current Department instance.
        # Update object id attribute using the primary key value of new row.
        sql = '''
                INSERT INTO departments (name, location)
                VALUES (?,?)
                '''
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
    
    @classmethod 
    def create(cls, name, location):
        # initializing a new department instance and save the object to the database.
        department = cls(name, location) # here we have created a class instance.
        department.save() # here we have called the save() method on the new instance creaetd.
        return department
    
    def update(self):
        # update the table row corresponding to the current department instance.
        sql = '''
                UPDATE departments
                SET name = ?, location = ?
                WHERE id = ?
                '''
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()
    
    def delete(self):
        #delete the table row corresponding to the current Depatment instance.
        sql = '''
                DELETE FROM departments
                WHERE id = ?
                '''
        CURSOR.execute(sql, (self.id,))# the comman in the tuple is crucial for creating a tupel with one item.
        CONN.commit()
# we use bound parameters with each questionmark  bound to a value within the CURSOR.execute method call.


    