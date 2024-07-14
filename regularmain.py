import regulardz

if __name__ == '__main__':
    contacts_list, first_row = regulardz.input_file('phonebook_raw.csv')
    newlist = regulardz.creating_newlist(contacts_list)
    thirdlist = regulardz.merge_contact(newlist, first_row)
    regulardz.output_file(thirdlist)
