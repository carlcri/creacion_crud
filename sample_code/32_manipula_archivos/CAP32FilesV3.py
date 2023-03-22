import csv, os


def print_all():

    with open('.people.csv', mode='r') as f:
        reader = csv.DictReader(f)

        for idx, row in enumerate(reader):
            print(row)  
        
        print(f'\n number of registers = {idx}')





def write_row(new_person):

    fields = ['SN', 'Name', 'City']
    new_row = {fields: new_person for fields, new_person in zip(fields, new_person)}
    print(new_row)

    with open('.people.csv', mode = 'a', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerow(new_row)



def get_new_person():

    user_id = input('id: ')
    name = input('Nombre: ')
    city = input('city: ')

    *new_employee, = user_id, name, city

    return new_employee


def display_menu():
    print('*'*50)
    os.system('echo Programa que ilustra R/W con cvs.Dictreader and cvs.Dictwriter | lolcat')
#    print('\nPrograma que ilustra R/W con cvs.Dictreader and cvs.Dictwriter')
    print('Que quieres hacer?')
    print('(M)ostrar todo')
    print('(E)scribir una nueva entrada')
    print('(S)alir')

    return input('Cual es tu opcion: ').upper()

if __name__ == '__main__':

    while(True):
        opcion = display_menu()
        
        if opcion == 'M':
            print_all()
        elif opcion == 'E':
            new_person = get_new_person()
            write_row(new_person)
        else:
            break 
        






