from hash import hash_function
import sys

def attack(dictionary_path):
    dictionary_file = open(dictionary_path, 'r')
    colissions_file = open('collisions.txt', 'w+')
    dic = dict() 
    for password in dictionary_file:
        password = password.rstrip('\n')
        hash_value = hash_function(password)
        if dic.get(hash_value) is None:
            dic[hash_value] = password
            print(hash_value + '     ->     ' + password)
        else:
            print("--------------------------------------------------------------")
            print(hash_value + '     ->     ' + password + '               ' + hash_value)
            colissions_file.write(dic[hash_value]+ '      ' + password + '     ->     ' + hash_value + '\n')

attack(sys.argv[1])