from copy import deepcopy
from ...utils.dict_processing import DictProcessor


class ModuleIOWrapper:
    def __init__(self, in_keys):
        self.__dict = None
        self.__input = None
        self._in_keys = in_keys

    def _process_input(self):
        return {k: v for k, v in self.__dict.items() if k in self._in_keys}

    def _process_output(self, module_out):
        dict_out = deepcopy(self.__dict)
        DictProcessor.update_dictionary(dict_out, module_out)
        return dict_out

    def __check_input_conforms(self):
        for k in self._in_keys:
            if k not in self.__dict:
                raise Exception("Module " + type(self).__name__ + ": " + k + " data missing")

    def read_input(self, input_dict):
        if self._in_keys is None:
            raise ValueError("Module " + type(self).__name__ + " has no in_keys!")

        self.__dict = input_dict
        self.__check_input_conforms()
        self.__input = self._process_input()
        return self.__input

    def return_output(self, module_output):
        return self._process_output(module_output)

    def get_in_keys(self):
        return self._in_keys
