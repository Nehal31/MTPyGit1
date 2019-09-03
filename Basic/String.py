# ”DBES” mnemonic. ”Decode Bytes, Encode Strings”

FILE = 'language.txt'
MODE = 'r'
ENCODING = 'utf-8'

def main():
    with open(FILE, mode=MODE, encoding=ENCODING) as infile:
        data = infile.readlines()
        for line in data:
            line = line.strip()
            print(line, end=" ")
            row_data = line.encode(ENCODING, errors='strict')
            cooked_data = row_data.decode(ENCODING, errors='strict')

            print(row_data , '====' , cooked_data)

if __name__ == '__main__':
    main()
