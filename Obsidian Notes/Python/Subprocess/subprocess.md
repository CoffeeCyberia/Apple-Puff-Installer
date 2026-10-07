# main.py

## subprocess
```
output = subprocess.check_output(               
	["lsblk", "-dn", "-o", "NAME,MODEL,SIZE"],
text=True
)
Disks = output.splitlines()
```
**subproces.check_output()**
	checks the output of the command in the brackets
**Brackets**
	-the Command is in brackets, because i want to have the Output also in Brakets. Normaly you can just type the command in the normal brackets
**text=True**
	Without that the text would be in bytes and not in a string
