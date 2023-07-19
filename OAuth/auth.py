from typing import Dict, Set
from uuid import uuid4

import pyotp
from flask import Flask, redirect, request

app = Flask(__name__)


# bu yeri hali yana to'ldiriladi
totp_sync_template = '''



# imitatsiya qilamiz
users_secrets: Dict[str, str] = dict()

# TOTP ilovasi orqali kirilganda
verifier_users: Set[str] = set()

@app.route('/')

def sync():
  # oddiylik uchun user ni generic qilamiz
  user_id = str(uuid4())
  # secret key ni generic qilamiz, shu asosida kod yozamiz
  secret = pyotp.random_base32()
  users_secrets[user_id] = secret
  # secret ga asoslanib, instance generator yaratamiz
  totp = pyotp.TOTP(secret)
  # TOTP ilova uchun havola + havolada, ism familiya va ilova nomini yuborish mumkin
  provisioning_url = totp.provisioning_uri(name=user_id + '@futurism.uz', issuer_name='Awesome Futurism app')
  tmpl = totp_sync_template % (provisioning_url, user_id)
  return tmpl
  
