import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    def find_files_helper(dir_path):
        subpaths = os.listdir(dir_path)
        for subpath in subpaths:
            fullpath = os.path.join(dir_path,subpath)
            if os.path.isfile(fullpath):
                if subpath.endswith("." + suffix):
                    suffix_paths.append(fullpath)
            elif os.path.isdir(fullpath):
                find_files_helper(fullpath)

    if os.path.isfile(path):
        if path.endswith("." + suffix):
            return [path]
        else:
            return []
    suffix_paths = []
    find_files_helper(path)
    return suffix_paths

#Test Case 1
##print(find_files("c", "testdir"))
#expected ---> ['testdir/subdir3/subsubdir1/b.c', 'testdir/t1.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c']

#Test Case 2
#print(find_files("java", "testdir"))
#expected ---> []

#Test Case 3
#print(find_files("", "testdir"))
#expected ---> []

#Test Case 4
#print(find_files("txt", "testdir2"))
#expected ---> ['testdir2/testdir2file.txt']

#Test Case 4
#print(find_files("md", "testdir2"))
#expected ---> ['testdir2/testdir2file.md', 'testdir2/testdir2file2.md']

#Test Case 5
#print(find_files("js", "testdir3"))
#expected ---> []

#Test Case 6
#print(find_files("js", "testfile.js"))
#expected ---> ["testfile.js"]