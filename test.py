
import rsa
import base64; base64.b64decode("MyA+IDE=").decode("utf-8")
 
# generate public and private keys with 
# rsa.newkeys method,this method accepts 
# key length as its parameter
# key length should be atleast 16
publicKey, privateKey = rsa.newkeys(2048)
print(privateKey)
print(privateKey.n)

 
# this is the string that we will be encrypting
message = """3 > 1"""
 
# rsa.encrypt method is used to encrypt 
# string with public key string should be 
# encode to byte string before encryption 
# with encode method
encMessage = rsa.encrypt(message.encode(), 
                         publicKey)
 
print("original string: ", message)
print("encrypted string: ", encMessage)

drazheska_n = privateKey.n
drazheska_e = privateKey.e
drazheska_d = privateKey.d
drazheska_p = privateKey.p
drazheska_q = privateKey.q
print(f"{drazheska_n}, {drazheska_e}, {drazheska_d}, {drazheska_p}, {drazheska_q}")
 
# the encrypted message can be decrypted 
# with ras.decrypt method and private key
# decrypt method returns encoded byte string,
# use decode method to convert it to string
# public key cannot be used for decryption

decMessage = rsa.decrypt(encMessage, rsa.PrivateKey(n=drazheska_n, e=drazheska_e, d=drazheska_d, p=drazheska_p, q=drazheska_q)).decode()
 
print("decrypted string: ", decMessage)

if eval(decMessage):
    print("e")
