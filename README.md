# CipherScope

i made this as a script / tool for an upcoming hackathon, i was trying to learn cryptography and got stuck on a couple of problems so what i was stuck on i made a tool to help me learn and better myself.

A Python command-line toolkit for learning about encodings, classical ciphers, text analysis, hashes, JWT structure, file metadata, and related utilities.

> Educational use only. Encodings and classical ciphers are not encryption. JWT inspection does not verify signatures. Never enter real passwords, private keys, API tokens, or confidential data into demonstrations.

## Requirements
- Python 3.10+ (standard library only).

## Run
From the repository root:

```bash
python -m cipherscope.main
```

## Project layout
- `cipherscope/main.py` — menu and entry point
- `cipherscope/core.py` — shared helpers and cipher primitives
- `cipherscope/encodings_tools.py` — Base encodings and detection
- `cipherscope/classical.py` — Caesar, Atbash, Vigenere, Morse and brute force
- `cipherscope/analysis_tools.py` — frequency, entropy, hash and text analysis
- `cipherscope/security_tools.py` — hashing, JWT inspection, random values, HMAC, PBKDF2
- `cipherscope/file_tools.py` — file inspection, JSON, GZIP and session history

Use only on files and data you own or are authorized to inspect. JWT signature validation is not implemented.
