
from .module import prediction, evaluation, reconstruction
from .utils.pdb_processing import PDBProcessor


class ModuledProteinPrediction:
    def __init__(self, pdb_path, config):
        self.__pdb_struct, self.__sequence = PDBProcessor.read_pdb(pdb_path)
        self.__config = config
        self.result = {"sequence": self.__sequence,
                       "pdb_struct": self.__pdb_struct,
                       "pdb_path": pdb_path,
                       "metrics": []}

    def predict(self):
        modules = {"prediction": prediction.available_modules,
                   "evaluation": evaluation.available_modules,
                   "reconstruction": reconstruction.available_modules}

        for module, module_params in self.__config:
            m_type, m_name = module.split(".")
            mod_obj = modules[m_type][m_name](module_params)
            self.result = mod_obj.process(self.result)
