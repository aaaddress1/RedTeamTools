import base64
import random
import string



split_str = base64_str.split('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
salt = ''.join(random.sample(string.ascii_letters + string.digits, 50))
new_base64_str=split_str[0]+salt
open('new_mimi.exe','wb').write(base64.b64decode(new_base64_str))
print ("\nCreate new_mimi.exe success.\n")