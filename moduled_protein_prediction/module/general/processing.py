

class ModuleProcessorProtocol:
    def __init__(self, param_dict):
        self._param_dict = param_dict

    def process(self, input_dict):
        raise NotImplementedError("This method must be overridden!")

    @classmethod
    def get_required_parameters(cls):
        raise NotImplementedError("This method must be overridden!")
