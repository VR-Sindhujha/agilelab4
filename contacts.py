contacts={}
def add_contact(name,phone):
    contacts[name]=phone
def search_contact(name):
    return contacts.get(name,"Not found")
if __name__=="__main__":
    add_contact("Arun","9843567897")
    add_contact("Priya","9080999719")
    print("Arun's number:",search_contact("Arun"))
    print("Search Kabir:", search_contact("Kabir"))