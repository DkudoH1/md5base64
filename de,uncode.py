import hashlib
import base64

sellect = input(" 1-'MD5' , 2-'base64' ")

if sellect == "1" :

    Ad5 = input("Please Enter String To Hash? ").strip()
    hash1 = hashlib.md5(Ad5.encode())
    print(hash1.hexdigest())
if sellect == "2" :
    base = input("Please input your app (1==>encode) or (2==>decode)")
    if base == "1" :

        base = input("Please Enter Strng To Base64? ").strip()
        base_bytes = base.encode('ascii')
        base64_bytes = base64.b64encode(base_bytes)
        base64_bbytes = base64_bytes.decode('ascii')
        print(base64_bbytes)
        #for num in base64_bbytes :
           # print(f"{num.upper()}@#1Zxc")
    if base == "2" :
        base64_string = input("Please write your hash base decode??").strip()
        base64_bytes = base64_string.encode("ascii")

        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")

        print(f"Decoded string: {sample_string}")

