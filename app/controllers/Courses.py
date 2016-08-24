"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

   
    def index(self):
        courses=self.models['Course'].get_courses()
        return self.load_view('index.html', courses=courses)

    def add_course(self):
        course={
                    'title': request.form['name'],
                    'description': request.form['description']
                }
        self.models['Course'].add_course(course)
        return redirect('/')

    def destroy_course(self,id):
        course=self.models['Course'].get_course(id)
        return self.load_view('destroy.html', course=course)

    def destroy(self,id):
        self.models['Course'].destroy(id)
        return redirect('/')
