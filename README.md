# keepass-cracker

A Python tool to decrypt and dump all entries from a KeePass `.kdbx` vault.

## Requirements

```bash
pip install pykeepass
```

## Usage

```bash
# Decrypt with a known password
python3 keepass-cracker.py vault.kdbx -p MyPassword

# Crack with a wordlist
python3 keepass-cracker.py vault.kdbx -w /usr/share/wordlists/rockyou.txt
```

## Output

Dumps all vault entries including username, password, URL, notes, group, tags, timestamps, and custom fields.

## Password Cracking

The `-w` flag provides a basic wordlist attack by attempting to open the database with each password. **This is for reference only — it is single-threaded Python and significantly slower than dedicated tools.**

For practical use, prefer `keepass2john` + `john` or `hashcat`:

```bash
# Extract hash
keepass2john vault.kdbx > vault.hash

# Crack with John
john vault.hash --wordlist=/usr/share/wordlists/rockyou.txt

# Crack with hashcat (mode 13400 = KeePass)
hashcat -m 13400 vault.hash /usr/share/wordlists/rockyou.txt
```

These are multi-threaded and GPU-capable, making them far more practical for real engagements.
