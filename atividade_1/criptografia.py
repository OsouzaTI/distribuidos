import rsa
import os
import signal

# gera as chaves publica e privada na pasta keys
def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(2048)
    with open('/home/osouza/distribuidos/atividade_1/keys/publicKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1())
    with open('/home/osouza/distribuidos/atividade_1/keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1())

# retorna o valor das chaves publica e privada em forma de tupla
def loadKeys():
    with open('/home/osouza/distribuidos/atividade_1/keys/publicKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('/home/osouza/distribuidos/atividade_1/keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey
