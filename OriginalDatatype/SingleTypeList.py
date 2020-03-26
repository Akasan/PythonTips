from copy import deepcopy


class InvalidTypeError(Exception):
    """ Error for specifying invalid data-type"""
    def __init__(self, mes="Invalid Type"):
        super(InvalidTypeError, self).__init__(mes)


def _is_single_type(data):
    """ check whether elements in data has same data-type or not
    Arguments:
        data {list} -- data you want to check elements' data-type
    Returns:
        {data-type or bool} -- if all elements has same data-type, return the data-type
                               if not, return False
    """
    _type = {}
    for d in data:
        _type[type(d)] = None
    is_single_type = True if len(_type) == 1 else False

    if is_single_type:
        return list(_type.keys())[0]
    else:
        False


class SingleTypeList(list):
    def __init__(self, _type):
        """
        Arguments:
            _type {any} -- type you want to store
        """
        super(SingleTypeList, self).__init__()
        self.TYPE = _type

    def append(self, data):
        """Append one value
        
        Arguments:
            data {list or any} -- data you want to append 
        """
        if not type(data) == list:
            data_type = type(data)
            assert data_type == self.TYPE, InvalidTypeError(f"Please add elements as {self.TYPE}")
            self += [data]
            
        else:
            is_single_type = _is_single_type(data)
            if not is_single_type:
                raise InvalidTypeError
            else:
                self += data

    def _to_empty(self):
        """ delete all elements"""
        for i in range(len(self)-1, -1, -1):
            del self[i]

    def to_unique(self):
        """ get unique list.
            This function can't overwrite this list as inplace.
        """
        unique_data = list(set(self))
        self._to_empty()
        self.append(unique_data)

    def delete_value(self, value, inplace=False):
        """ delete specific value from list
        Arguments:
            value {any} -- value you want to delete
            inplace {bool} -- if you want to change values as inplace, set this as True
        """
        if inplace:
            for i in range(len(self) -1 , -1, -1):
                if self[i] == value:
                    del self[i]
        else:
            result = deepcopy(self)
            for i in range(len(self) -1 , -1, -1):
                if result[i] == value:
                    del result[i]
            return result

    def _change_type(self):
        """ change 
        """
        for i in range(len(self)):
            self[i] = self.TYPE(self[i])

    def change_type(self, new_type):
        """ change type to new one.
        Arguments:
            new_type {any} -- type you want to set as new data-type
        """
        try:
            _ = new_type(self[0])
        except:
            raise InvalidTypeError(f"can't convert from {self.TYPE} to {new_type}")

        self.TYPE = new_type
        self._change_type()
 

if __name__ == "__main__":
    l = SingleTypeList(int)
    l.append([1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7, 10])
    l.to_unique()
    l += [1, 2, 3]
    l.to_unique()
    print(l)
