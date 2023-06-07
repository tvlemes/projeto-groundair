from firebase_admin import credentials, initialize_app, storage
import os 

firebase_key    = os.environ['AIRFLOW__FIREBASE__KEY']
path_bucket     = os.environ['AIRFLOW__PATH__BUCKET']
path_storage    = os.environ['AIRFLOW__PATH__STORAGE']

# Init firebase with your credentials
cred = credentials.Certificate(firebase_key)
initialize_app(cred, {'storageBucket': 'groundair-96d08.appspot.com'})

file_name = "img.png"
file_path = path_storage + file_name
bucket = storage.bucket()
blob = bucket.blob(file_name)
blob.upload_from_filename(file_path)

# Opt : if you want to make public access from the URL
blob.make_public()

print("your file url: ", blob.public_url)