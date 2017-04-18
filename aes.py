import sys
import os.path
import base64

def read_file(filename):
	file = open(filename, "rb")
	fileBytes = [];
	while True:
		block = base64.b16encode(file.read(1))
		if block == b"":
			break
		fileBytes.append(block)
	return fileBytes


def main(filename): 
	byteArray = read_file(filename)
	for byte in byteArray:
		print(byte)


if __name__ == "__main__":
	if (len(sys.argv) != 2):
		print("Usage aes.py <file>")
	else:
		if os.path.isfile(sys.argv[1]):
			main(sys.argv[1])
		else:
			print("File does not exist")