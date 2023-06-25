# import pymongo
# from pymongo import MongoClient
# client=pymongo.MongoClient('mongodb://localhost:27017/')

# mydb=client['Bugbusters']

# information= mydb.child_imgs

# # post={"_id":0,"none":"tim"}
# # information.insert_one(post)
# # record={}

import pymongo
from cryptography.fernet import Fernet
from rsa import decrypt
from pymongo import MongoClient
import cv2
import numpy as np

# client=pymongo.MongoClient('mongodb://localhost:27017/')

# mydb=client['Bugbusters']

# #collection= mydb.child_imgs

# collection= mydb.Book1

# for i in mydb.Book1.find({'Username': 'ghn'}):
#     message = str((i['Username']))
#     key = Fernet.generate_key()
#     fernet = Fernet(key)
#     print(i)

#     encrypted_message = fernet.encrypt(message.encode())
#     print("Original Message:\n", message)
#     print("Encrypted Message:\n", encrypted_message)

#     decrypted_message = fernet.decrypt(encrypted_message).decode()
#     print("Decrypted Message:",decrypted_message)


demo = cv2.imread(r"C:\Users\Divya Nair\Downloads\BugBusters-main\Childhood_vs_present\2\B.jpeg", 0)
r, c = demo.shape
key = np.random.randint(0, 256, size=(r, c), dtype=np.uint8)  # Generate random key image
cv2.imwrite(r"C:\Users\Divya Nair\Downloads\BugBusters-main\Childhood_vs_present\2\B.jpeg", key)   # Save key image

cv2.imshow("demo", demo)  # Display original image
cv2.imshow("key", key)  # Display key image

encryption = cv2.bitwise_xor(demo, key)  # encryption
cv2.imwrite(r"C:\Users\Divya Nair\Downloads\BugBusters-main\Childhood_vs_present\2\encryption.jpg", encryption)     # Save the encrypted image
decryption = cv2.bitwise_xor(encryption, key)  # decrypt
cv2.imwrite(r"C:\Users\Divya Nair\Downloads\BugBusters-main\Childhood_vs_present\2\decryption.jpg", decryption) # Save the decrypted image

cv2.imshow("encryption", encryption)  # Display ciphertext image
cv2.imshow("decryption", decryption )  # Displays the decrypted image

cv2.waitKey(-1)
cv2.destroyAllWindows()