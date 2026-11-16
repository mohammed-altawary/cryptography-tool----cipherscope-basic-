"""Frequency, entropy, hash and text analysis."""
import hashlib,math,re
from collections import Counter
from .core import title,ask
def frequency():
 title("FREQUENCY"); c=Counter(x.lower() for x in ask() if x.isalpha()); n=sum(c.values()) or 1
 for x,k in c.most_common(): print(f"{x}: {k} ({k/n*100:.2f}%)")
def entropy():
 title("ENTROPY"); t=ask()
 if not t: print("Empty input."); return
 c=Counter(t); n=len(t); print("Characters:",n,"Unique:",len(c),"Entropy:",-sum((v/n)*math.log2(v/n) for v in c.values()))
 print("Sample estimate only; not a password-strength guarantee.")
def hash_identifier():
 title("HASH IDENTIFIER"); t=ask().strip()
 if not re.fullmatch("[0-9a-fA-F]+",t): print("Not a hexadecimal digest."); return
 print({32:"Possible MD5",40:"Possible SHA-1",56:"Possible SHA-224",64:"Possible SHA-256",96:"Possible SHA-384",128:"Possible SHA-512"}.get(len(t),"Unknown hash format"))
 print("Length does not prove algorithm identity.")
def text_tools():
 title("TEXT ANALYSIS"); t=ask()
 for k,v in [("Characters",len(t)),("Words",len(t.split())),("Reversed",t[::-1]),("Letters",sum(x.isalpha() for x in t)),("Digits",sum(x.isdigit() for x in t)),("Spaces",sum(x.isspace() for x in t)),("Uppercase",t.upper()),("Lowercase",t.lower())]: print(k+":",v)
