import sys
import os.path
import base64

BLOCK_SIZE = 16

# Reads key and returns bytes of that key
def read_key(keyname):
	file = open(keyname, "rb")
	key = base64.b16encode(file.read(BLOCK_SIZE))
	if not key or len(key) < 32:
		print("ERROR: Key is not large enough.")
		return -1
	return key


# Expands key and returns expanded key
def expand_key(key):
	print("expand key")


# Reads file and returns list with 16byte-blocks
def read_file(filename):
	file = open(filename, "rb")
	fileBytes = [];
	while True:
		block = base64.b16encode(file.read(BLOCK_SIZE))
		if not block:
			break
		# Adds 01 and 00's to complete block
		if len(block) < 32:
			block += b'01'
			while len(block) < 32:
				block += b'00'
		fileBytes.append(block)
	return fileBytes


# Main function that will call every stage of the encryption
def cypher(byte, expandedKey):
	print("BYTE -> " + byte.decode("utf-8"))

def main(filename, keyfile):
	name = filename
	
	key = read_key(keyfile)
	if key == -1:
		return

	byteArray = read_file(filename)
	for byte in byteArray:
		byte = cypher(byte, 1)


if __name__ == "__main__":
	if (len(sys.argv) != 3):
		print("Usage aes.py <file> <key>")
	else:
		if os.path.isfile(sys.argv[1]):
			main(sys.argv[1], sys.argv[2])
		else:
			print("File does not exist")