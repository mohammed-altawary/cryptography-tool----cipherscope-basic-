"""Shared helpers and cipher primitives."""
HISTORY=[]
B58="123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
MORSE=dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.".split(),"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
def header():
 print("\033[2J\033[H",end="")
 print("\n========== CIPHERSCOPE ==========\nPERSONAL SECURITY TOOLKIT\nEncodings/classical ciphers are not encryption. JWT inspection does not verify signatures.\n")
def title(s): print("\n"+"="*45+"\n"+s.upper()+"\n"+"="*45)
def pause(): input("\nPress ENTER to return to menu...")
def ask(): return input("\nEnter input: ")
def save(op,src,out): HISTORY.append({"operation":op,"input_length":len(src),"output_length":len(str(out))})
def show(v): print("\n[+] RESULT:\n"+str(v))
def decode_binary(t):
 g=t.split()
 if not g or any(len(x)!=8 or set(x)-{"0","1"} for x in g): raise ValueError("Binary input must contain 8-bit groups.")
 return bytes(int(x,2) for x in g).decode()
def b58_encode(data):
 n=int.from_bytes(data,"big"); out=""
 while n: n,r=divmod(n,58); out=B58[r]+out
 return "1"*(len(data)-len(data.lstrip(b"\0")))+out
def b58_decode(t):
 n=0
 for c in t:
  if c not in B58: raise ValueError("Invalid Base58 character")
  n=n*58+B58.index(c)
 return b"\0"*(len(t)-len(t.lstrip("1")))+n.to_bytes((n.bit_length()+7)//8,"big")
def caesar(t,s):
 return "".join(chr((ord(c)-(65 if c.isupper() else 97)+s)%26+(65 if c.isupper() else 97)) if c.isascii() and c.isalpha() else c for c in t)
def atbash(t):
 return "".join(chr(155-ord(c)) if "a"<=c<="z" else chr(155-ord(c)) if "A"<=c<="Z" else c for c in t)
def english_score(t): return sum(t.lower().count(c) for c in " etaoinshrdlu")/max(len(t),1)
