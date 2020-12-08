import q2
q2.generate_key()
key = q2.load_key()

# encrypt file
f = open("img.jpg", "rb")
q2.encrypt_message(f.read())
# print(f.read())
f.close()

#decrypt File
f = open('encoded.file', 'rb')
q2.decrypt_message(f.read())
f.close()
