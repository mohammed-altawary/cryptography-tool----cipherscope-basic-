"""CipherScope command-line entry point."""
import binascii,codecs,zlib
from .core import header,pause,show,ask,atbash
from .encodings_tools import encoding_menu,auto_detect
from .classical import caesar_tool,brute_force,recovery,vigenere_tool,morse_tool
from .analysis_tools import frequency,entropy,hash_identifier,text_tools
from .security_tools import hash_tool,jwt_tool,random_tool,hmac_tool,password_hash_tool
from .file_tools import file_inspector,json_tool,gzip_tool,history_tool
def main():
 tools={"01":auto_detect,"02":lambda:encoding_menu("Base64"),"03":lambda:encoding_menu("Base32"),"04":lambda:encoding_menu("Base58"),"05":lambda:encoding_menu("Base85"),"06":lambda:encoding_menu("Hexadecimal"),"07":lambda:encoding_menu("Binary"),"08":lambda:show("ASCII: "+" ".join(str(ord(c)) for c in ask())),"09":lambda:show(codecs.decode(ask(),"rot_13")),"10":caesar_tool,"11":lambda:show(atbash(ask())),"12":vigenere_tool,"13":morse_tool,"14":brute_force,"15":recovery,"16":frequency,"17":entropy,"18":hash_tool,"19":hash_identifier,"20":jwt_tool,"21":text_tools,"22":file_inspector,"23":json_tool,"24":gzip_tool,"25":history_tool,"26":random_tool,"27":hmac_tool,"28":password_hash_tool}
 while True:
  header()
  print("\n".join(["[01] Automatic Detection","[02] Base64","[03] Base32","[04] Base58","[05] Base85","[06] Hex","[07] Binary","[08] ASCII","[09] ROT13","[10] Caesar","[11] Atbash","[12] Vigenere","[13] Morse","[14] Brute Force","[15] Missing Character Recovery","[16] Frequency","[17] Entropy","[18] Hash Generator","[19] Hash Identifier","[20] JWT Inspector","[21] Text Analysis","[22] File Inspector","[23] JSON Formatter","[24] GZIP","[25] History","[26] Secure Random","[27] HMAC-SHA256","[28] PBKDF2","[00] EXIT"]))
  c=input("CIPHERSCOPE >> ").strip()
  if c=="00": print("CipherScope closed."); break
  try:
   if c in tools: tools[c]()
   else: print("Invalid selection.")
  except (ValueError,UnicodeError,OSError,zlib.error,binascii.Error) as e: print("[!] Error:",e)
  pause()
if __name__=="__main__":
 try: main()
 except (KeyboardInterrupt,EOFError): print("\nCipherScope closed.")
