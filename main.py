import pyAesCrypt

password = input ('Enter your password ')

pyAesCrypt.encryptFile('data.txt', 'data.txt.aes',password)


'''дешифратор - decoder'''


pyAesCrypt.decryptFile('data.txt.aes', 'data.txt',password)