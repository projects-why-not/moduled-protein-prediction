import Bio.PDB as pdb


class PDBProcessor:
    @classmethod
    def read_pdb(cls, pdb_path):
        struct = pdb.PDBParser().get_structure("s", pdb_path)[0]
        sequence = [res.resname for res in struct.child_list[0].child_list]
        return struct, sequence
