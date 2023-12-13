from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HastaneVerileri(Base):
    __tablename__ = 'example_table'

    case_id = Column(Integer, primary_key=True)
    hospital_type_code = Column(String(1))
    city_code_hospital = Column(Integer)
    hospital_region_code = Column(String(1))
    available_extra_rooms_in_hospital = Column(Integer)
    department = Column(String(50))
    ward_type = Column(String(10))
    ward_facility_code = Column(String(1))
    bed_grade = Column(Float)
    patientid = Column(Integer)
    city_code_patient = Column(Float)
    type_of_admission = Column(String(20))
    severity_of_illness = Column(String(20))
    visitors_with_patient = Column(Integer)
    age = Column(String(20))
    admission_deposit = Column(Float)
    stay = Column(String(20))
    hospital_name = Column(String(100))
    def __repr__(self):
        return f"Case {self.case_id}"