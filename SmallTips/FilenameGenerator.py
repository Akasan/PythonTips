def apply_and_save(base_file, out_filename, apply_function, save_function, *args):
    """ apply_and_save does following process.
        1. apply function to base_file
        2. the 1's result will be saved as out_filename with base_file's directory
        
    Arguments:
        base_file {str} -- file name
        out_filename {str} -- file name for save
        apply_function {function} -- open base_file and do something
        save_function {function} -- receive the results of apply_function and save results 
                                    as out_filename                               
    """
    result = function(base_file, *args)
    splitted_name = base_file.replace("\\", "/").split("/")
    out_filepath = "/".join(splitted_name[:-1]) + "/" + out_filename
    save_function(result, out_filepath)
