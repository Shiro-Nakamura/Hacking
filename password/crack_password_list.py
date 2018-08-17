import crypt


DICTIONARY = "files/fasttrack.txt"
PASSFILELIST = "files/passwords.txt"
SEPERATOR = ":"

def test_password(crypt_pass):
    salt = crypt_pass[0:2]
    dir = open(DICTIONARY, 'r')
    for word in dir.readlines():
        word = word.strip('\n')
        crypt_word = crypt.crypt(word, salt)
        
        if(crypt_word == crypt_pass):
            print("[+] found password: {}".format(word))
            return
    print("[-] not found")
        
def main():
    passfile = open(PASSFILELIST)
    for line in passfile.readlines():
        if SEPERATOR in line:
            user = line.split(SEPERATOR)[0].strip(' ')
            print("[+] try crack password for user: {}".format(user))
            crypt_pass = line.split(SEPERATOR)[1].strip(' ')
            test_password(crypt_pass)
    
        
if __name__=="__main__":
    main()