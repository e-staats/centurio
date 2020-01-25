from centurio.data.users import User
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
import centurio.services.mongo_setup as mongo_setup
import centurio.services.attempt_services as attempt_service
import bson

# pylint: disable=no-member


def find_user_by_email(email: str) -> User:
    mongo_setup.global_init()
    return User.objects(email=email).first()

def find_user_by_id(user_id: bson.ObjectId) -> User:
    mongo_setup.global_init()
    return User.objects(id=user_id).first()

def create_user(name,email,password):
    
    #todo: validation
    if find_user_by_email(email):
        return None
    user = User()
    user.name = name
    user.email = email
    user.hashed_pw = hash_text(password)
    user.status = 1

    mongo_setup.global_init()
    user.save()
    return user

def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=171204)
    return hashed_text

def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)

def validate_user(email: str, password: str) -> User:
    mongo_setup.global_init()
    user = find_user_by_email(email)
    if not user:
        return False
    if not verify_hash(user.hashed_pw, password):
        return False
    return user

def construct_feed_user_list(user):
    #get the members of the cohort
    #todo
    active_attempts = attempt_service.get_active_attempt_list(user)
    user_list = []
    #get friends
    user_list.append(list(User.objects(id=user.id).friends_list))



