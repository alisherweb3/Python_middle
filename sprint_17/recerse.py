function find_file(folder, file_to_find):
  for path in __ folder
    if path :
        #
      file = find_file(path, file_to_find)
      if file != None: # dif file find, send it to continie
        return file # in cycle recerse calls
else: # path - simple file
  if name_file(path) == file_to_find:
      # if file find, return it
    return path
return None
