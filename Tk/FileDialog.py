import os
import tkinter
import tkinter.filedialog as fd


def get_filepath(extension):
    """ get file path with file dialog
    Arguments:
        extension {str} -- extension you want to get 
    Returns:
        {str or NoneType} -- when file is properly selected, return the absolute path 
    """
    root = tkinter.Tk()
    root.withdraw()

    ftype = [(f"{extension.upper()}", f".{extension}")]
    cwd = os.path.abspath(os.getcwd())

    _file = fd.askopenfilename(filetypes=ftype, initialdir=cwd)
    return None if _file == "" else _file
