import sys
import json
from rc4 import encrypt

class Manager:

    __slots__ = ('master_key')

    def __init__(self, master_key:str):
        self.master_key = master_key
    
    def handleOption(self, option:str, **kwargs):
        
        if not self.validateArgs(option):
            return None 
        
        match option:
            case '-add':
                self.add(kwargs['domain'], kwargs['password'], kwargs['username'])
            case '-get':
                self.get(kwargs['domain'])
            case '-remove':
                self.remove(kwargs['domain'])
            case '-update':
                self.update(kwargs['domain'])
            case '-list':
                self.list()
    
    def validateArgs(self, option:str):
        match option:
            case '-add':
                return len(sys.argv) == 5
            case '-update':
                return len(sys.argv) == 7 and ('-username' in sys.argv or '-password' in sys.argv)
            case '-remove':
                return len(sys.argv) == 3
            case '-get':
                return len(sys.argv) == 3
            case '-list':
                return len(sys.argv) == 2

    def add(self, domain:str, password:str, username:str):
        with open('passwords.json', 'r') as f:
            try:
                js = json.load(f)
            except:
                js = []

            count = len([obj for obj in js if obj['domain'] == domain])
            if count != 0:
                return None       
            id = 0 if len([obj['id'] for obj in js if type(obj) is dict]) == 0 else max([obj['id'] for obj in js if type(obj) is dict])

            encrypted_password = encrypt(self.master_key, [ord(c) for c in password], 'encrypt')
            encrypted_password = '$'.join([str(x) for x in encrypted_password])

            encrypted_username = encrypt(self.master_key, [ord(c) for c in username], 'encrypt')
            encrypted_username = '$'.join([str(x) for x in encrypted_username])
            
            js.append({
                    'id':id + 1,
                    'domain':domain, 
                    'password':encrypted_password,
                    'username':encrypted_username,
            })

        with open('passwords.json', 'w') as f:
            json.dump(js, f, indent = 6)

    def get(self, domain:str):
        with open('passwords.json', 'r') as f:
            js = json.load(f)
            credentials = []
            for obj in js:
                if obj['domain'] == domain:
                    for attribute in ['username', 'password']:
                        credentials.append(''.join([chr(x)for x in encrypt(self.master_key, [int(x) for x in obj[f'{attribute}'].split('$')], 'decrypt')]))
            if len(credentials) != 0:
                print('Domain %s: The username is %s and the password is %s'%(domain, credentials[0], credentials[1]))
            else:
                print('The specified domain was not found!')
    
    def remove(self, domain:str):
        js = None
        with open('passwords.json', 'r') as f:
            js = list(filter(lambda x: x['domain'] != domain, json.load(f)))
        with open('passwords.json', 'w') as f2:
            json.dump(js, f2, indent = 6)

    def update(self, domain:str):
        with open('passwords.json', 'r') as f:
            js = json.load(f)
            dictIndex = next(index for (index, x) in enumerate(js) if x['domain'] == domain)
            if dictIndex != None:
                if '-username' in sys.argv:
                    userIndex = next(index for (index, x) in enumerate(sys.argv) if x == '-username') + 1
                    js[dictIndex].update({'username':'$'.join(str(x) for x in encrypt(self.master_key, [ord(x) for x in sys.argv[userIndex]], 'encrypt'))})
                
                if '-password' in sys.argv:
                    pswIndex = next(index for (index, x) in enumerate(sys.argv) if x == '-password') + 1
                    js[dictIndex].update({'password':'$'.join(str(x) for x in encrypt(self.master_key, [ord(x) for x in sys.argv[pswIndex]], 'encrypt'))})
        
        with open('passwords.json', 'w') as f:
            json.dump(js, f)

    def list(self):
        with open('passwords.json', 'r') as f:
            js = json.load(f)
            for obj in js:
                self.get(obj['domain'])
    

            

def main():
    args = sys.argv;args.pop(0)
    master_key, option = args[0:2]
    dict = {key:args[index+2] for index, key in enumerate(['domain', 'username', 'password']) if index + 2 < len(sys.argv)}
    m = Manager(master_key)
    m.handleOption(option, **dict)


if __name__ == '__main__':
    main()