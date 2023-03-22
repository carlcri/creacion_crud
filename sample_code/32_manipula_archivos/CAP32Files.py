import csv

def print_all():

    with open('employee_birthday.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for idx, row in enumerate(csv_reader):
            while idx != 0:
            #    print(row)
                print(f'{row[0]} works at the {row[1]} deparment, and his/her birhday is on {row[2]}')
                break

        print(f'\n number of registers = {idx}')


def write_row():
    with open('employee_birthday.txt', mode = 'a', newline = '') as csv_file:
        csv_file_writer = csv.writer(csv_file, delimiter = ',')
        csv_file_writer.writerow(['Francia', 'Culture', 'October'])


def display_menu():
    print('*'*50)
    print('\nPrograma que ilustra R/W con cvs.reader and cvs.writer')
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
            write_row()
        else:
            break 
        






