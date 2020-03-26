import pickle


def remove_duplicate_from_list(data):
    """ remove duplications from specific list
        any data can be contained in the data.
        if the data is hashable, you can implement this function easily like below.
            data = list(set(data))
        but if the data is unhashable, you have to implement in other ways.
        This function use pickle.dumps to convert any data to binary.
        Binary data is hashable, so after that, we can implement like with hashable data.
    Arguments:
        data {list(any)} -- list that contains any type of data
    Returns:
        {list(any)} -- list that contains any type of data without duplications
    """
    pickled_data = [pickle.dumps(d) for d in data]
    removed_pickled_data = list(set(pickled_data))
    result = [pickle.loads(d) for d in removed_pickled_data]
    return result


if __name__ == "__main__":
    data = [1, 2, 2, 3, 2, 2, 2, 6]
    print(remove_duplicate_from_list(data))

    data = ["hoge", 1, "hdf", 3.4, "hoge", 2, 2, 2]
    print(remove_duplicate_from_list(data))
