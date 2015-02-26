import pickle

class Names:
    def __init__(self):
        self.name = None
        self.birth = None


new_record = Names()
new_record.name = input("Enter name: ")
new_record.birth =  input("Enter date of birth (dd/mm/yyyy): ")
    

name_list = []          

with open("names.dat",mode="wb") as name_file:
    pickle.dump(name_list,name_file)
