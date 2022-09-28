

class DictProcessor:
    @classmethod
    def update_dictionary(cls, gen_dict, app_dict):
        for k, v in app_dict.items():
            cls.__update_key(gen_dict, k, v)

    @classmethod
    def get_available_keys(cls):
        return ["dihedral",
                "coord",
                "contact_map",
                "third_party",
                "sequence",
                "pdb_struct",
                "pdb_path",
                "stats"]

    @classmethod
    def __update_key(cls, gen_dict, key, app_values):
        if key in ["coord", "dihedral", "third_party", "stats"]:
            cls.__update_countable(gen_dict, key, app_values)
        elif key == "contact_map":
            gen_dict["contact_map"] = app_values
        elif key == ["sequence", "pdb_struct", "pdb_path"]:
            raise ValueError("Sequence and PDB structure must be immutable!")
        else:
            raise ValueError("No such data type!")

    @classmethod
    def __update_countable(cls, gen_dict, key, app_values):
        for k, v in app_values.items():
            gen_dict[key][k] = v
