import firebase_admin
from firebase_admin import firestore

def insert_email(collection_name, mail):
    try:
        doc_ref = db.collection(collection_name).document()
        doc_ref.set({
            u'email': mail
        })
        print("Document added with ID:", doc_ref.id)
    except Exception as e:
        print("Error adding document:", str(e))

def print_collection(collection_name):
    docs = db.collection(collection_name).stream()
    total_records = 0
    for doc in docs:
        total_records += 1
        print(f'{doc.id} => {doc.to_dict()}')
    print("*-*" * 10,)
    print(f'Total records: {total_records}')

def create_new_collection(collection_name, initial_data):
    try:
        db.collection(collection_name).add(
            initial_data
        )
        print(f'Collection {collection_name} created successfully')
    except Exception as e:
        print(f'Error creating collection {collection_name}:', str(e))

def insert_web_dev_agency(collection_name, website):
    try:
        doc_ref = db.collection(collection_name).document()
        doc_ref.set({
            u'website': website
        })
        print("Document added with ID:", doc_ref.id)
    except Exception as e:
        print("Error adding document:", str(e))    

if __name__ == "__main__":
    credentials = firebase_admin.credentials.Certificate("servcy-landing-firebase-adminsdk-84yk3-4cfb9454e1.json")
    app = firebase_admin.initialize_app(credentials)
    db = firestore.client()