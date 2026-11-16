"""File metadata, JSON formatting, GZIP decompression, history."""
import hashlib,json,zlib
from pathlib import Path
from .core import title,ask,show,HISTORY
def file_inspector():
 title("FILE INSPECTOR"); p=Path(input("File path: ").strip().strip('"'))
 if not p.is_file(): print("File not found."); return
 h=hashlib.sha256()
 with p.open("rb") as f:
  first=f.read(32); h.update(first)
  for chunk in iter(lambda:f.read(1048576),b""): h.update(chunk)
 print("Name:",p.name,"Size:",p.stat().st_size,"bytes","First bytes:",first.hex(" "),"SHA256:",h.hexdigest())
 sig={b"\x89PNG\r\n\x1a\n":"PNG",b"\xff\xd8\xff":"JPEG",b"PK\x03\x04":"ZIP",b"%PDF":"PDF",b"\x1f\x8b":"GZIP"}
 print("Format:",next((v for k,v in sig.items() if first.startswith(k)),"Unknown"))
def json_tool():
 title("JSON FORMATTER")
 try: show(json.dumps(json.loads(ask()),indent=4))
 except json.JSONDecodeError as e: print("Invalid JSON:",e)
def gzip_tool():
 title("GZIP DECOMPRESSOR"); raw=bytes.fromhex(ask().replace(" ","")); limit=10*1024*1024; d=zlib.decompressobj(16+zlib.MAX_WBITS); out=d.decompress(raw,limit+1)
 if len(out)>limit or d.unconsumed_tail: raise ValueError("Decompressed output exceeds 10 MiB.")
 out+=d.flush(limit+1-len(out))
 if len(out)>limit or not d.eof: raise ValueError("Oversized, incomplete, or invalid GZIP data.")
 show(out.decode(errors="replace"))
def history_tool():
 title("SESSION HISTORY"); print("Memory-only activity log; contents are not retained.")
 if not HISTORY: print("No operations yet.")
 for x in HISTORY: print(x["operation"],"input:",x["input_length"],"output:",x["output_length"])
