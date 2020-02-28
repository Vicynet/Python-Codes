import json
import contacts_book

def main():
    file_object = open('backup_file.json', 'r')
    contacts_book.contacts = json.load(file_object)
    file_object.close()
    print(contacts_book.contacts)
    
    contacts_book.new_contact()
  
    contacts_book.search_contact()

    file_object = open('backup_file.json', 'w')
    json.dump(contacts_book.contacts, file_object)
    file_object.close()
    
if __name__ == '__main__':
    main()

