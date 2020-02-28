import collect_phone_no
import collect_name
#import create_contact

#create_contact.new_contact()
contacts = {}

def new_contact():
    print('\nNew Contact')
    while True:
        name = collect_name.collect_name()
        if name == 'quit' or name == 'q':
            break
        phone_no = collect_phone_no.collect_phone_no()
        contacts[name] = phone_no
    print(contacts)

def search_contact():
    print('\nSearch Contact')
    while True:
        name = collect_name.collect_name()
        if name == 'quit' or name == 'q':
            break
        try:
            print(name, contacts[name])
        except:
            print(name + ' does not exist')
