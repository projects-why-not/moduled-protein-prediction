# moduled-protein-prediction: Python module for predicting the spacial structure of a protein.

The module is intended to work as a pipeline. Different methods can be implemented in respective submodules of moduled-protein-prediction/module. Then, prediction for a single protein is a sequence of names of applied methods.

Dictionary with several kinds of data of the protein is shared between prediction steps. This process is unified and cannot be modified.

Users may add new prediction methods using the utility moduled-protein-prediction/utils/add_module.py.
