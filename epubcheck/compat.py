has_scandir = True


try:
    from scandir import scandir, walk
except ImportError:
    from os import walk  # NOQA
    from os import listdir as scandir  # NOQA
    from os.path import isdir  # NOQA

    has_scandir = False
