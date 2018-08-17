import zipfile
import pwd

DICTIONARY = "files/fasttrack.txt"
ZIPFILE = "files/secure.zip"

def extract_zip(zFile, password):
    try:
        zFile.extractall(pwd=password.encode())
        return password
    except Exception as e:
        return 
        
def main():
    zFile = zipfile.ZipFile(ZIPFILE)
    dict = open(DICTIONARY)
    for line in dict.readlines():
        pwd = line.strip('\n')
        guess = extract_zip(zFile, pwd)
        if guess:
            print("[+] found password: {}".format(pwd))
            return

    print("[-] password not found")
    
if __name__ == '__main__':
    main()