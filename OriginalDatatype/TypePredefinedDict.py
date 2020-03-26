class InvalidKeyError(Exception):
    def __init__(self, mes):
        super(InvalidKeyError, self).__init__(mes)

class InvalidValueError(Exception):
    def __init__(self, mes):
        super(InvalidValueError, self).__init__(mes)


class PredefinedDict(dict):
    def __init__(self, key_type, value_type):
        super(PredefinedDict, self).__init__()
        self.KEY_TYPE = key_type
        self.VALUE_TYPE = value_type
        self.item = dict()

    def __setitem__(self, key, val):
        assert type(key) == self.KEY_TYPE, InvalidKeyError(f"Please set key as type {self.KEY_TYPE} (you specified {key})")
        assert type(val) == self.VALUE_TYPE, InvalidValueError(f"Please set value as type {self.VALUE_TYPE} (you specified {type(val)})")

        self.item[key] = val

    def __getitem__(self, key):
        return self.item[key]

    def __repr__(self):
        result = ""
        for k, v in self.item.items():
            result += f"key: {k}\tvalue: {v}\n"
        return result
