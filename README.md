Path Normalization
===================
Author: Michelle Nguyen

This is a method written in Python that takes a string that represents a file path as an argument and returns
a string which represents the normalized path. The path is normalized by removing all single dot components 
and double dot components, along with their parent directory (if any), but does no further normalization. That 
is, the method will return 'foo/bar' if 'foo/./bar' is passed in as an argument, 'foo/baz/../bar' will return 'foo/bar',
but '../foo/bar' will return 'foo/bar', and 'foo//bar' will still return 'foo//bar'.

To run the code, load the Python file into an interpreter and call the function "normalize" with your string that 
represents a file path as an argument.

For example: normalize('foo/./bar')

