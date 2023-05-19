import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
import os
import DB.firebaseconfig
import pyrebase

# Fetch the service account key JSON file contents
cred = credentials.Certificate("DB/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
bucket_name = DB.firebaseconfig.get_bucket_name()

firebaseConfig = DB.firebaseconfig.get_firebase_config()
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

class FirebaseMutator:
    def __init__(self, collection_name):
        self.db = firestore.client()
        self.collection_ref = self.db.collection(collection_name)

    def create(self, data, memberID):
        doc_ref = self.collection_ref.document(memberID)
        doc_ref.set(data)
        return doc_ref.id

    def update(self, doc_id, data):
        doc_ref = self.collection_ref.document(doc_id)
        doc_ref.update(data)

    def delete(self, doc_id):
        doc_ref = self.collection_ref.document(doc_id)
        doc_ref.delete()

class FirebaseAccessor:
    def __init__(self, collection_name):
        self.db = firestore.client()
        self.collection_ref = self.db.collection(collection_name)

    def read_all(self):
        docs = self.collection_ref.get()
        return [doc.to_dict() for doc in docs]

    def read(self, doc_id):
        doc_ref = self.collection_ref.document(doc_id)
        doc = doc_ref.get()
        return doc.to_dict() if doc.exists else None

class FirebaseStorage:
    def __init__(self):
        self.bucket = storage.bucket(bucket_name)

    def upload_folder(self, local_folder_path, remote_folder_path):
        for root, dirs, files in os.walk(local_folder_path):
            for filename in files:
                local_file_path = os.path.join(root, filename)
                remote_file_path = os.path.join(
                    remote_folder_path, os.path.relpath(local_file_path, local_folder_path)
                ).replace("\\", "/")
                blob = self.bucket.blob(remote_file_path)
                blob.upload_from_filename(local_file_path)
        print("File uploaded!")
    
    def upload_file(self, local_file_path, remote_folder_path, new_file_name):
        remote_file_path = os.path.join(remote_folder_path, new_file_name).replace("\\", "/")
        blob = self.bucket.blob(remote_file_path)
        blob.upload_from_filename(local_file_path)
        print("File uploaded!")

    def download_folder(self, remote_folder_path, local_folder_path):
        if not os.path.exists("ImagesMembers"):
            os.mkdir("ImagesMembers")
            print("Folder created successfully")
        else:
            print("Folder already exists")
        blobs = self.bucket.list_blobs(prefix=remote_folder_path)
        for blob in blobs:
            remote_file_path = blob.name
            local_file_path = os.path.join(
                local_folder_path, os.path.relpath(remote_file_path, remote_folder_path)
            )
            os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
            blob.download_to_filename(local_file_path)
        print("File downloaded!")

class FirebaseAuthentication:
    # def __init__(self):

    def login(email, password):
        try:
            auth.sign_in_with_email_and_password(email, password)
            return "Pass"
        except:
            return "Invalid email or password"
    
    def register(email, password):
        try:
            auth.create_user_with_email_and_password(email, password)
            return "Pass"
        except:
            return "Email already exist"
    
    def getAuthEmail():
        return auth.current_user['email']

# firebase_storage = FirebaseStorage()
#  > Upload folder to firebase storage
# firebase_storage.upload_folder("ImagesMembers", "img")

# > Download folder from firebase storage
# firebase_storage.download_folder("img", "ImagesMembers")

# > Create new member
# mutator = FirebaseMutator('members')
# accessor = FirebaseAccessor('members')
# new_member_data = {'name': 'testing', 'points': 0}
# new_member_id = mutator.create(new_member_data, "testing")
# print('New user created with ID:', new_member_id)

# > Update the member's point
# updated_user_data = {'points': 100}
# mutator.update("testing", updated_user_data)
# print('Member's points updated')

# > Retrieve all users
# all_members = accessor.read_all()
# print('All members:', all_members)

# > Retrieve the updated user
# updated_user = accessor.read("testing")
# print('Updated user:', updated_user)

# > Delete the user
# mutator.delete("i5pytua00CCI1cIy0yUM")
# print('User deleted')