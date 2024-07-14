import re
import csv


def input_file(filename):
    with open(f"{filename}", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        first_row = contacts_list[0]
    return contacts_list, first_row


def creating_newlist(contacts_list):
    i = 0
    newlist = []

    for resource in contacts_list:
        i += 1
        if i > 1:

            tel = resource[-2]
            pattern = r"(\+7|8)?(\s)*(\()?(\d{3})(\))?" \
                      r"(\s|-)*(\d{3})[\s-]*(\d{2})[\s-]*(\d+)\s?" \
                      r"(\()?(доб\.)?(\s)?(\d{4})?(\))?"
            substr = r"+7(\4)\7-\8-\9 \11\13"
            telefon = re.sub(pattern, substr, tel)
            fio = " ".join(resource[:3]).replace('  ', ' ').strip(" ")
            b = fio.split(' ')
            if len(b) <= 2:
                b.append('')
            c = resource[3:5]
            d = [resource[-1]]
            e = [telefon.strip(" ")]
            f = b + c + e + d
            newlist.append(f)
    return newlist


def merge_contact(newlist, first_row):
    altlist = newlist
    cleanlist = []
    thirdlist = [first_row]
    testlist = []
    for i in newlist:
        for j in altlist:
            if i not in thirdlist and i not in testlist:
                thirdlist.append(i)
            if i != j and i[0] == j[0] and i[1] == j[1]:
                testlist.append(i)
                thirdlist.remove(i)
                for numb in range(len(i)):
                    if i[numb] != '':
                        cleanlist.append(i[numb])
                    elif i[numb] == '':
                        cleanlist.append(j[numb])
            if cleanlist != [] and cleanlist not in thirdlist:
                thirdlist.append(cleanlist)
            cleanlist = []
    return thirdlist


def output_file(thirdlist):
    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(thirdlist)
