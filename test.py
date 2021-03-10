import os
from decouple import config

password = config("ADDRESS", cast=str)

print(password)