def upper(func):
    def wrapper(*args, **kwargs):
        
        lista = []

        for item in args:
            lista.append(item.upper())

        args = tuple(lista)  
        result = func(*args, **kwargs)

        return result
    
    return wrapper


@upper
def say_my_name(name, last_name):
    return 'hello {name} es {last_name}'.format(name = name, last_name=last_name)


if __name__ == '__main__':
	print(say_my_name('Gustavo', 'Petro'))
