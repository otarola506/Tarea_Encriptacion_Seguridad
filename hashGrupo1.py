# encoding: utf-8
from bitarray import bitarray
from bitarray.util import *
import struct
import sys

'''
Algoritmo Hash para la primera tarea práctica del curso.
Estudiantes:
            - Filip Sobejko
            - Kevin Barrantes
            - Steff Fernanfez
'''

class FKS_Hash:
  
    def __init__(self, word, block):

        self.wordToHash = word
        self.arr = bitarray()
        self.outputHash = bitarray()
        self.block = block
        self.checkSize()

    def checkSize(self):
        
        # Se crea el bitarray para almacenar la hilera de entrada y se hace append de un 1
        bitArray = bitarray()
        bitArray.frombytes(self.wordToHash.encode("utf-8"))
        bitArray.append(1)

        stringLen = len(bitArray)
        lenBitArray = int2ba(stringLen)
        sizeLen = len(lenBitArray)

        # Se realizan appends de ceros hasta que llegue a un punto donde podamos insertar lo que vale la hilera y completar el módulo
        while len(bitArray) % self.block != self.block - sizeLen: 
                bitArray.append(0)

        bitArray.extend(lenBitArray)
        self.arr = bitArray

    def rightRotate(self, subBloque, movement):

        return (subBloque >> movement) | (subBloque << (64 - movement)) & 0xFFFFFFFFFFFFFFFF

    def hashAlgorithm(self):

        index = 0
        startingVariable = hex2ba('88FEEF103CCDF8B5')
        blockArray = []

        while(index != len(self.arr)):

            # Se particiona el bloque de datos en 4 sub-bloques
            sub1 = self.arr[index:index+64]
            sub2 = self.arr[index+64:index+128]
            sub3 = self.arr[index+128:index+192]
            sub4 = self.arr[index+192:index+256]

            # Se realizan las operaciones para digerir el estado inicial con los sub-bloques
            startingVariable = sub1 ^ (startingVariable & hex2ba('912161483B58B3FF'))
            blockArray.append(startingVariable)

            startingVariable = sub2 ^ int2ba((self.rightRotate(ba2int(startingVariable), 8)), length=64)
            blockArray.append(startingVariable)

            startingVariable = int2ba(ba2int((sub3 | startingVariable), signed=False), length=64)
            blockArray.append(startingVariable)

            startingVariable = sub4 | startingVariable
            blockArray.append(startingVariable)

            index += 256

        result = bitarray()
        result.extend(blockArray[0])
        result.extend(blockArray[1])
        result.extend(blockArray[2])
        result.extend(blockArray[3])

        return ba2hex(result)

def main():

    hashKey = ""
    if len(sys.argv) > 1:
        hashKey = sys.argv[1]

    claseHash = FKS_Hash(hashKey, 256)
    hashKey = claseHash.checkSize()
    hashValue = claseHash.hashAlgorithm()

    print (hashValue)
