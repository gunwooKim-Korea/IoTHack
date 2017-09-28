import pyasn1.codec.der.encoder
import pyasn1.type.univ
import base64

def egcd(a, b) :
        if a == 0:
                return (b,0,1)
        else:
                g,y,x = egcd(b % a, a)
                return (g, x - ( b // a ) *y, y)


def modinv(a, m):
        gcd, x, y = egcd(a, m)
        if gcd != 1:
                return None
        else:
                return x % m

def pempriv(n,e,d,p,q, dP, dQ, qInv):
        template = '-----BEGIN RSA PRIVATE KEY-----\n{}-----END RSA PRIVATE KEY-----\n'
        seq = pyasn1.type.univ.Sequence()
        for x in [0,n,e,d,p,q,dP,dQ,qInv] :
                seq.setComponentByPosition(len(seq), pyasn1.type.univ.Integer(x))
        der = pyasn1.codec.der.encoder.encode(seq)
        return template.format(base64.encodestring(der).decode('ascii'))


p=
q=
n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = modinv(e,phi)
dp = d % p
dq = d % q
qi = pow(q, p - 2, p)


key = pempriv(n,e,d,p,q,dp,dq,qi)
print key
