from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///university.db")
engine.connect()

Base = declarative_base()


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    course_list = relationship(
        "Course",
        back_populates="student_info",
        cascade="all, delete"
    )


class Course(Base):

    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    unit = Column(Integer)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE")
    )

    student_info = relationship(
        "Student",
        back_populates="course_list"
    )


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sessionlocal = Session()


# # Add student:
# student1 = Student(name="Ali Ahmadi")
# student2 = Student(name="Sara Mohammadi")

# sessionlocal.add_all([student1, student2])
# sessionlocal.commit()


# # Add course:
# course1 = Course(
#     title="Python Programming",
#     unit=3,
#     student_id=1
# )

# course2 = Course(
#     title="Database",
#     unit=4,
#     student_id=1
# )

# course3 = Course(
#     title="Network",
#     unit=3,
#     student_id=2
# )

# sessionlocal.add_all([course1, course2, course3])
# sessionlocal.commit()


# # Read:

# student = sessionlocal.query(Student).filter_by(id=1).first()

# if student:
#     print("Student Name:", student.name)
#     print("-" * 30)

#     for course in student.course_list:
#         print("Course:", course.title)
#         print("Units:", course.unit)
#         print("*" * 20)


# # Update:

# course = sessionlocal.query(Course).filter_by(id=1).first()
# if course:
#     course.unit = 5
#     sessionlocal.commit()


# # Delete:

# student = sessionlocal.query(Student).filter_by(id=2).first()
# if student:
#     sessionlocal.delete(student)
#     sessionlocal.commit()