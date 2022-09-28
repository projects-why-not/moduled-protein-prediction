import os
import sys


def create_model_directory(module_name, module_type):
    m_types = ["evaluation", "prediction", "reconstruction"]
    if module_type not in m_types:
        raise ValueError("Module type must be one of: evaluation, prediction, reconstruction")
    path = "/".join(os.path.realpath(__file__).split("/")[:-2]) + "/module/"
    for t in m_types:
        if os.path.exists(path + f"{t}/{module_name}"):
            raise ValueError("Module with this name already exists!")
    path += f"{module_type}/{module_name}/"
    os.mkdir(path)
    # TODO: copy io.py and __processing.py
    # TODO: create wrapper.py


def print_help():
    print("\nEXECUTION:")
    print("python3 add_module.py <module_name> <module_type>\n")


def process_input(args):
    if (len(args) > 0 and args[0] == "--help") or len(args) < 2:
        print_help()
        return
    m_name, m_type = args
    create_model_directory(m_name, m_type)


if __name__ == "__main__":
    args = sys.argv[1:]
    process_input(args)