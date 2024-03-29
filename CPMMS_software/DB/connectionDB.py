import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
import sys, os
import DB.firebaseconfig
import pyrebase

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Fetch the service account key JSON file contents
cred = credentials.Certificate(resource_path("DB/serviceAccountKey.json"))
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

    def create_autoID(self, data):
        self.collection_ref.add(data)

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

    def read_all_with_id(self):
        docs = self.collection_ref.get()
        return [{"id": doc.id, "data": doc.to_dict()} for doc in docs]

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
    
    def delete_file(self, remote_folder_path, file_name):
        remote_file_path = os.path.join(remote_folder_path, file_name).replace("\\", "/")
        blob = self.bucket.blob(remote_file_path)
        blob.delete()
        print("File deleted!")

    def delete_file_has_string(self, memID):
        blobs = self.bucket.list_blobs(prefix="img")
        for blob in blobs:
            if memID in blob.name:
                blob.delete()
                print("File deleted!")


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
        
    def delete_user_auth(email):
        try:
            user = firebase_admin.auth.get_user_by_email(email)
            firebase_admin.auth.delete_user(user.uid)
            return "User deleted successfully"
        except:
            return "Failed to delete user"
    
    def getAuthEmail():
        return auth.current_user['email']
    
    def send_password_reset_email(email):
        try:
            auth.send_password_reset_email(email)
            return "Success! Please check your email to reset your password"
        except:
            return "Failed to send email due to invalid email or email is not registered"
