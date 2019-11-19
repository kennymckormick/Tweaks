import hmac, base64, struct, hashlib, time, os

ovpn_cfg = ''
dual_factor = ''
password = ''
user_name = ''

def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(h[19]) & 15
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
    return h

def get_totp_token(secret):
    return get_hotp_token(secret, intervals_no=int(time.time())//30)

with open('auth.txt' ,'w') as fout:
    fout.write(user_name + '\n')
    pw = password + str(get_totp_token(dual_factor))
    fout.write(pw)

os.system('openvpn --config {} --auth-user-pass auth.txt'.format(ovpn_cfg))
    
