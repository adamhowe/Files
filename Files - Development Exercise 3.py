import pickle

class Names:
    def __init__(self):
        self.name = None
        self.birth = None

with open("names.dat",mode="rb") as name_file:
    Names = pickle.load(name_file)


for name in Names:
    print(new_record.name)
