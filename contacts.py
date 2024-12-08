import tkinter as tk #tkinter for the GUI
from tkinter import messagebox, simpledialog


class HashTable:
    

    def __init__(self, size=100):
        self.size = size  # the size for the hash table (is fixed)
        self.table = [[] for _ in range(self.size)]  # List of buckets

    def hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash(key)
        bucket = self.table[index]

        # this is to see if the key already exists
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        # If key doesn't exist, then add it to the bucket
        bucket.append([key, value])
    
    def get(self, key):
        index = self.hash(key)
        bucket = self.table[index]

        # Search the bucket for the key
        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return None  # Key not found

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        # search bucket for the key and remove it
        for pair in bucket:
            if pair[0] == key:
                bucket.remove(pair)
                return True

        return False  # the key isnt found

    def items(self):
        for bucket in self.table:
            for pair in bucket:
                yield pair[0], pair[1]


