import pickle

class Names:
    def __init__(self):
        self.name = None
        self.birth = None

name_list = [] 

thing = False
while thing == False:
    new_record = Names()
    print("\nEnter name and date of birth - press 'Enter' to end")
    new_record.name = input("Enter name: ")
    if new_record.name == "":
        thing = True
        print("\nEnd")
    else:
        new_record.birth =  input("Enter date of birth: ")
    for count in range(1):
        name_list.append(Names)
    
    
with open("names.dat",mode="wb") as name_file:
    pickle.dump(name_list,name_file)
