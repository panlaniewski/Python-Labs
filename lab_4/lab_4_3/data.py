from faker import Faker
import numpy as np
import pandas as pd
import json

fake = Faker('ru_RU')

def generate_entrance_campaign_data(count=100):
    students = []
    
    with open('specialties.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    specialties_data = data['specialties']
    
    for _ in range(count):
        admission_year = fake.random_int(min=2020, max=2024)
        exams_score = fake.random_int(min=180, max=300)
        certificate_grade = round(np.random.uniform(7.0, 10.0), 1)
        admission_score = round(exams_score + (certificate_grade * 10))
        random_faculty = np.random.choice(specialties_data)
        faculty_info = random_faculty["faculty"]
        random_specialty = np.random.choice(random_faculty["specialties"])
        
        student = {
            'name': fake.name(),  
            'admission_year': admission_year, 
            'form_of_study': random_specialty["form"], 
            'exams_score': exams_score,  
            'certificate_score': certificate_grade, 
            'admission_score': admission_score, 
            'faculty_name': faculty_info["name"],
            'faculty_short_name': faculty_info["short_name"],
            'specialty': random_specialty["name"], 
            'address': fake.address().replace('\n', ', '), 
            'phone': fake.phone_number()  
        }
        students.append(student)
    return students

dataset = generate_entrance_campaign_data(1000)
df = pd.DataFrame(dataset)
df.to_csv('entrance_campaign.csv', index=False)
