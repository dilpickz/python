from cryptography.hazmat.primitives import serialization
import sys

def writeKey(encryptedKey, key):
    file = encryptedKey.split(".")
    file.pop(4)
    pem_file = ".".join(file)
    print(pem_file)
    f = open(pem_file, "w")
    for line in key:
        f.write(line)
    f.close()
    return pem_file

def decryptKey(encryptedKey, password):
    password_user = password
    key_file = open(encryptedKey, 'rb')
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=password_user.encode()
        )
    decrypted_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
    ).decode()
    return decrypted_key

def main():
    while True:
        if len(sys.argv) < 3:
            print("Application needs file name and password")
            encryptedKey, password = input("Enter file name: "), input("Enter password: ")
        else:
            encryptedKey, password = sys.argv[1], sys.argv[2]
        try:
            key = decryptKey(encryptedKey, password)
            newFile = writeKey(key)
            print (f"New key created as {newFile}")
            break
        except:
            key = decryptKey(encryptedKey, password)
            newFile = writeKey(encryptedKey, key)
            print (f"New key created as {newFile}")
            break

if __name__=="__main__":
    main()
