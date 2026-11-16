"""Base encodings and automatic detection."""
import base64,binascii,re
from .core import title,ask,show,save,decode_binary,b58_encode,b58_decode,caesar
def encoding_menu(name):
 title(name); print("[1] Encode\n[2] Decode"); choice=input("Select: "); t=ask(); raw=t.encode()
 if choice=="1":
  out={"Base64":lambda:base64.b64encode(raw).decode(),"Base32":lambda:base64.b32encode(raw).decode(),"Base85":lambda:base64.b85encode(raw).decode(),"Base58":lambda:b58_encode(raw),"Hexadecimal":lambda:raw.hex(),"Binary":lambda:" ".join(f"{b:08b}" for b in raw)}[name]()
 elif choice=="2":
  out={"Base64":lambda:base64.b64decode(t,validate=True).decode(),"Base32":lambda:base64.b32decode(t,casefold=True).decode(),"Base85":lambda:base64.b85decode(t).decode(),"Base58":lambda:b58_decode(t).decode(),"Hexadecimal":lambda:bytes.fromhex(t).decode(),"Binary":lambda:decode_binary(t)}[name]()
 else: print("Invalid selection."); return
 show(out); save(name,t,out)
def auto_detect():
 title("AUTOMATIC DETECTION"); t=ask().strip()
 try:
  d=base64.b64decode(t,validate=True)
  if base64.b64encode(d).decode().rstrip("=")==t.rstrip("="): print("Possible Base64:",d.decode(errors="replace"))
 except (ValueError,binascii.Error): pass
 if t and len(t.replace(" ",""))%2==0 and re.fullmatch(r"[0-9a-fA-F ]+",t):
  try: print("Possible hex:",bytes.fromhex(t).decode(errors="replace"))
  except ValueError: pass
 print("Caesar candidates:")
 for s in range(26): print(f"Shift {s:02}: {caesar(t,-s)}")
 save("Automatic detection",t,"Analysis completed")
