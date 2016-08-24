from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def add_course(self, course):
        query="INSERT INTO courses (title, description, created_at, updated_at) VALUES (:title, :description, NOW(), NOW())"
        return self.db.query_db(query, course)

    def get_course(self,id):
        query = "SELECT * FROM courses WHERE id=:id LIMIT 1"
        data = {'id':id}
        return self.db.query_db(query,data)[0]

    def get_courses(self):
        query="SELECT * FROM courses"
        return self.db.query_db(query)

    def destroy(self,id):
        query = "DELETE FROM courses WHERE id=:id"
        data={'id':id}
        self.db.query_db(query,data)
