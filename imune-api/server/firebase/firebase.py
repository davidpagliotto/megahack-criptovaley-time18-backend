from pyrebase import pyrebase

_conf = {
    'apiKey': 'AIzaSyDNSQYZTdMgpZn1OZnW_52FEwVHYiGrHKs',
    'authDomain': 'imune-4be76.firebaseapp.com',
    'databaseURL': 'https://imune-4be76.firebaseio.com',
    'projectId': 'imune-4be76',
    'storageBucket': 'imune-4be76.appspot.com',
    'messagingSenderId': '868812606233',
    'appId': '1:868812606233:web:c20a3aec86ffd86fd09388',
    'measurementId': 'G-KD03L22RDR'
}


def init_firebase_app():
    return pyrebase.initialize_app(_conf)
