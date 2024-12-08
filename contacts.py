import tkinter as tk
from tkinter import messagebox, simpledialog


class HashTable:
    

    def __init__(self, size=100):
        self.size = size  # the size for the hash table (is fixed)
        self.table = [[] for _ in range(self.size)]  # List of buckets

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        # this is to see if the key already exists
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        # If key doesn't exist, then add it to the bucket
        bucket.append([key, value])
