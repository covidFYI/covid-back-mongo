from app.data import data_bp
from app.data.models import Entries
import csv
import os

""" Flask CLI Commands (DATA) """
@data_bp.cli.command('add-data')
def add_data():

    # Why add if already added? :D
    if Entries.objects.count() > 0:
        print("MongoDB already populated!")
        return

    with open(os.path.join('test_data_csv', 'Doctors.csv')) as f:
        print('Adding doctors...')
        reader = csv.reader(f)
        l = tuple(reader)
        for s in l[1:]:
            Entries(id=s[0],category=s[1], state=s[2], area=s[3], name=s[4], subCategory=s[5], email_1=s[6], phone_1=s[7],  phone_2=s[8], sourceURL=s[9], source=s[10],description=s[11]).save()
        print('Doctors added!')
    
    with open(os.path.join('test_data_csv', 'Fever_Clinics.csv')) as f:
        print('Adding fever clinics...')
        reader = csv.reader(f)
        l = tuple(reader)
        for s in l[1:]:
            
            Entries(id=s[0],category=s[1], state=s[2], area=s[3], subCategory=s[4],name=s[5], pointOfContact=s[6], email_1=s[7], email_2=s[8], phone_1=s[9],  phone_2=s[10], address=s[11],sourceURL=s[12], source=s[13]).save()
        print('Fever clinics added!')
    
    with open(os.path.join('test_data_csv', 'Government_Contacts.csv')) as f:
        print('Adding govt contacts...')
        reader = csv.reader(f)
        l = tuple(reader)
        for s in l[1:]:
            Entries(id=s[0],category=s[1], state=s[2], area=s[3], subCategory=s[4], pointOfContact=s[5], email_1=s[6], email_2=s[7], phone_1=s[8],  phone_2=s[9], sourceURL=s[10], source=s[11], description=s[12]).save()
        print('Govt contacts added!')

    with open(os.path.join('test_data_csv', 'Helpline.csv')) as f:
        print('Adding helplines...')
        reader = csv.reader(f)
        l = tuple(reader)
        for s in l[1:]:
            
            Entries(id=s[0],category=s[1], state=s[2], area=s[3], subCategory=s[4], phone_1=s[5],  phone_2=s[6], sourceURL=s[7], source=s[8]).save()
        print('Helplines added!')
    with open(os.path.join('test_data_csv', 'Hospitals.csv')) as f:
        print('Adding hospitals...')
        reader = csv.reader(f)
        l = tuple(reader)
        for s in l[1:]:
            
            Entries(id=s[0], category=s[1], state=s[2], area=s[3], name=s[4], pointOfContact=s[5], email_1=s[6],email_2=s[7], phone_1=s[8],  phone_2=s[9], address=s[10],sourceURL=s[11], source=s[12], description=s[13]).save()
        print('Hospitals added!')
    
    with open(os.path.join('test_data_csv', 'Labs.csv')) as f:
        print('Adding labs...')
        reader = csv.reader(f)
        l = tuple(reader)
        for s in l[1:]:
            #Unique ID,Category,State,Area,Sub -Category,Name,Point Of Contact,Email 1,Email 2,Phone 1,Phone 2,Address,Source Url,Source
            Entries(id=s[0],category=s[1], state=s[2], area=s[3], subCategory=s[4],name=s[5], pointOfContact=s[6], email_1=s[7],email_2=s[8], phone_1=s[9],  phone_2=s[10], address=s[11],sourceURL=s[12], source=s[13]).save()
        print('Labs added!')

@data_bp.cli.command('delete-all')
def delete_all():

    Entries.objects().delete()