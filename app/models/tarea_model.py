from database import db



class Tarea(db.Model):
    __tablename__ = "tareas"

    # Define las columnas de la tabla `animals`
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(100), nullable=False)
    assigned_to = db.Column(db.String(100), nullable=False)
    # Inicializa la clase `Animal`
    def __init__(self,title,description,status,created,assigned_to):
        self.title = title
        self.description = description
        self.status = status
        self.created_at = created
        self.assigned_to = assigned_to

    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Tarea.query.all()

    @staticmethod
    def get_by_id(id):
        return Tarea.query.get(id)

    def update(self, title=None,description=None,status=None,created_at=None,assigned_to=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if assigned_to is not None:
            self.assigned_to = assigned_to
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
