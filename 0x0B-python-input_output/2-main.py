#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

text_to_append = "This School is so cool!\n"
nb_characters_added = append_write("file_append.txt", text_to_append)
print(nb_characters_added)
