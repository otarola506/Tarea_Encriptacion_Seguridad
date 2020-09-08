from hashGrupo1 import FKS_Hash
import sys

def hash_attack(dictionary_path):
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

def dictionary_attack(dictionary_path):
    dictionary_file = open(dictionary_path, 'r')
    given_hash_value = 'c77420476c0930b5b5c77420476c0930b5c77420476c0930b5c77420476c0931'
    for password in dictionary_file:
        password = password.rstrip('\n')
        hash_grupo_4 = FKS_Hash(password, 256)
        hash_grupo_4.checkSize()
        hash_value = hash_grupo_4.hashAlgorithm()
        if given_hash_value == hash_value:
            print(password)

dictionary_attack(sys.argv[1])