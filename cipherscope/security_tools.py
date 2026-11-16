"""Hashing, JWT inspection, random values, HMAC and PBKDF2."""
import base64,binascii,hashlib,hmac,json,re,secrets,string
from getpass import getpass
from .core import title,ask
def hash_tool():
 title("HASH GENERATOR"); b=ask().encode(); print("MD5/SHA1 are legacy only.")
 for n in ["md5","sha1","sha256","sha512","sha3_256","blake2b"]: print(n.upper(),hashlib.new(n,b).hexdigest())
def jwt_tool():
 title("JWT INSPECTOR"); p=ask().strip().split(".")
 if len(p)!=3: print("Invalid three-part JWT."); return
 def dec(x):
  if not re.fullmatch("[A-Za-z0-9_-]*",x): raise ValueError("Invalid base64url characters.")
  return base64.b64decode(x+"="*(-len(x)%4),altchars=b"-_",validate=True)
 try:
  for name,x in [("HEADER",p[0]),("PAYLOAD",p[1])]:
   d=json.loads(dec(x))
   if not isinstance(d,dict): raise ValueError("JWT part must be a JSON object.")
   print(name+":\n"+json.dumps(d,indent=4))
  print("WARNING: Signature NOT verified; claims are untrusted.")
 except (ValueError,binascii.Error,json.JSONDecodeError) as e: print("Error:",e)
def random_tool():
 title("SECURE RANDOM"); c=input("[1] URL-safe token [2] Password: "); n=int(input("Length: "))
 if c=="1":
  if not 1<=n<=1024: raise ValueError("Token length 1-1024.")
  out=secrets.token_urlsafe(n)
 elif c=="2":
  if not 8<=n<=256: raise ValueError("Password length 8-256.")
  groups=(string.ascii_lowercase,string.ascii_uppercase,string.digits,"!@#$%^&*()-_=+[]{}:,.?")
  a=[secrets.choice(g) for g in groups]+[secrets.choice("".join(groups)) for _ in range(n-4)]; secrets.SystemRandom().shuffle(a); out="".join(a)
 else: print("Invalid choice."); return
 print("Generated value (not stored):",out)
def hmac_tool():
 title("HMAC-SHA256"); c=input("[1] Create [2] Verify: "); key=getpass("Secret key (hidden): ").encode()
 if not key: raise ValueError("Empty key.")
 tag=hmac.new(key,ask().encode(),hashlib.sha256).hexdigest()
 if c=="1": print(tag)
 elif c=="2":
  supplied=input("Expected 64-char hex tag: ").strip()
  if not re.fullmatch("[0-9a-fA-F]{64}",supplied): raise ValueError("Invalid tag format.")
  print("Valid" if hmac.compare_digest(tag,supplied.lower()) else "INVALID")
 else: print("Invalid choice.")
def password_hash_tool():
 title("PBKDF2 PASSWORD"); c=input("[1] Create [2] Verify: "); pw=getpass("Password (hidden): ").encode()
 if not pw: raise ValueError("Empty password.")
 if c=="1":
  n=600000; salt=secrets.token_bytes(16); d=hashlib.pbkdf2_hmac("sha256",pw,salt,n); print(f"pbkdf2_sha256${n}${salt.hex()}${d.hex()}"); return
 if c!="2": print("Invalid choice."); return
 p=input("Stored hash: ").split("$")
 if len(p)!=4 or p[0]!="pbkdf2_sha256": raise ValueError("Unrecognized hash format.")
 n=int(p[1]); salt=bytes.fromhex(p[2]); expected=bytes.fromhex(p[3])
 if not 100000<=n<=2000000 or len(salt)!=16 or len(expected)!=32: raise ValueError("Malformed PBKDF2 hash.")
 print("Valid" if hmac.compare_digest(hashlib.pbkdf2_hmac("sha256",pw,salt,n),expected) else "INVALID")
