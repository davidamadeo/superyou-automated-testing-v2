import os
from decouple import config

variable = config("DRIVER_PATH", cast=str)

print(variable)