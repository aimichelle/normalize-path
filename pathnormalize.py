
def normalize(path):
    """Takes a string which represents a file path and returns the normalized file 
    path by removing all single dot components of the path and all double dots
    components of the path, but does not perform any other kind of
    normalization.

    >>> normalize('foo/./bar')
    'foo/bar'

    >>> normalize('foo/bar/../baz')
    'foo/baz'

    >>> normalize('foo/bar/.././baz/./../bar')
    'foo/bar'

    """
    directories = path.split('/')
    kept_directories = []
    normalized= ''
    for directory in directories:
        if directory != '.' and directory != '..':
            kept_directories.append(directory)           
        elif directory == '..':
            if len(kept_directories) != 0:
                kept_directories.pop()           
    for directory in kept_directories:
        if directory is kept_directories[0]:
            normalized = directory
        else:
            normalized = normalized + "/" + directory
    
    return normalized
