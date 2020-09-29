print("""WriteText Shortcut made in Python by 4Bytes/Tangly/Luckytrang2010
==================================================================================

""")
location = input("[?] (DON'T PUT A SLASH AT THE END!) Enter the directory/location for the file to be in: ")
name = input("[?] Enter the file's name: ")
exten = input("[?] (DON'T PUT A DOT!) Enter the file's extension name: ")
print("Cool! Let's get to the editing part.\n")
filetime = open(f"{location}\\{name}.{exten}","a+")
inside = input(f"[?] Content inside {name}.{exten}: ")
filetime.write(inside)
print("Done! Thanks for using.")