from ...general.processing import ModuleProcessorProtocol
from ...general.io import ModuleIOWrapper


class NCReconstructionModule(ModuleProcessorProtocol):
    __in_keys = ["coord"]

    def __init__(self, param_dict=None):
        super().__init__(param_dict)
        self._io_manager = ModuleIOWrapper(self.__in_keys)

    def process(self, input_dict):
        in_data = self._io_manager.read_input(input_dict)

        # TODO: process in_data
        # TODO: return self._io_manager.return_output()

    @classmethod
    def get_required_parameters(cls):
        return cls.__in_keys
