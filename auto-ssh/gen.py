import hmac, base64, struct, hashlib, time, os
password = ''
dual_factor = ''

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(h[19]) & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time())//30)

with open('password.txt', 'w') as fout:
	fout.write(password + '\r')

with open('dyn_code.txt', 'w') as fout:
	fout.write(str(get_totp_token('dual_factor')) + '\r')

