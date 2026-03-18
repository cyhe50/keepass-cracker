from pykeepass import PyKeePass
import sys

if len(sys.argv) < 3:
    print("Usage: python3 crack.py database.kdbx password")
    sys.exit(1)

kp = PyKeePass(sys.argv[1], password=sys.argv[2])

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
