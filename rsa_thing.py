from cryptography.hazmat.primitives import serialization
import sys

file = sys.argv[1].split(".")
file.pop(4)
pem_file = ".".join(file)
print(pem_file)

password_user =sys.argv[2]

key_file = open(sys.argv[1], 'rb')
private_key = serialization.load_pem_private_key(
    key_file.read(),
    password=password_user.encode()
    )

print(private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
    ).decode())

decrypted_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
    ).decode()

f = open(pem_file, "w")
for line in decrypted_key:
    f.write(line)
f.close()


