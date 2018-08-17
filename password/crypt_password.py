import crypt

PASSWORD = "Welcome123"
SALT = "HX"

hash = crypt.crypt(PASSWORD,SALT)
print("hash: {}".format(hash))
