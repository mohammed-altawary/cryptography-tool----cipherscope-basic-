"""Classical ciphers and educational brute-force helpers."""
import itertools,string
from .core import title,ask,show,caesar,english_score,MORSE,save
def caesar_tool():
 title("CAESAR CIPHER"); c=input("[1] Encode [2] Decode: "); t=ask(); s=int(input("Shift 0-25: "))
 if c not in {"1","2"} or not 0<=s<=25: raise ValueError("Invalid choice or shift.")
 out=caesar(t,s if c=="1" else -s); show(out); save("Caesar",t,out)
def brute_force():
 title("BRUTE FORCE LAB"); c=input("[1] Caesar [2] Single-byte XOR: "); t=ask()
 if c=="1":
  for score,s,x in sorted((english_score(caesar(t,-s)),s,caesar(t,-s)) for s in range(26))[::-1]: print(f"{s:02} | {score:.3f} | {x}")
 elif c=="2":
  raw=bytes.fromhex(t.replace(" ","")); rows=[]
  for k in range(256):
   x=bytes(b^k for b in raw).decode(errors="replace"); rows.append((sum(c.isprintable() for c in x)/max(len(x),1),k,x))
  for score,k,x in sorted(rows,reverse=True)[:10]: print(f"Key {k:02X} | {score:.2f} | {x}")
def recovery():
 title("MISSING CHARACTER RECOVERY"); t=ask(); pos=[i for i,c in enumerate(t) if c=="?"]
 if not pos: print("No missing characters."); return
 if len(pos)>2: print("Maximum supported unknowns: 2"); return
 rows=[]
 for letters in itertools.product(string.ascii_lowercase,repeat=len(pos)):
  a=list(t)
  for i,c in zip(pos,letters): a[i]=c
  x="".join(a); rows.append((english_score(x),x))
 for s,x in sorted(rows,reverse=True)[:20]: print(f"{s:.3f} | {x}")
def vigenere_tool():
 title("VIGENERE"); c=input("[1] Encode [2] Decode: "); t=ask(); k="".join(x for x in input("Key: ").lower() if x in string.ascii_lowercase)
 if c not in {"1","2"} or not k: print("Invalid choice/key."); return
 out=[]; j=0
 for x in t:
  if x.isascii() and x.isalpha():
   s=ord(k[j%len(k)])-97; s=s if c=="1" else -s; b=65 if x.isupper() else 97; out.append(chr((ord(x)-b+s)%26+b)); j+=1
  else: out.append(x)
 show("".join(out))
def morse_tool():
 title("MORSE"); c=input("[1] Encode [2] Decode: "); t=ask().upper(); rev={v:k for k,v in MORSE.items()}
 if c=="1": show(" ".join(MORSE.get(x,"/") for x in t))
 elif c=="2": show("".join(rev.get(x," ") for x in t.split()))
 else: print("Invalid choice.")
