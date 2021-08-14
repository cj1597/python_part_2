import logging


logging.basicConfig(filename='func.log', level=logging.INFO, format="%(asctime)s %(funcName)s(%(message)s)",
                    datefmt="%d-%m-%Y %H:%M:%S")


def get_first_name(fname):
    logging.info(f'{fname}')
    return f'Welcome to Python {fname}'


def get_full_name(fname, lname):
    logging.info(f'{fname}, {lname}')
    return f'Welcome to Python {fname} {lname}'


def get_role(fname, lname, role):
    logging.info(f'{fname}, {lname}, {role}')
    return f'Welcome to Python {role} - {fname} {lname}'


if __name__ == '__main__':
    print(get_first_name('Zoro'))
    print(get_full_name('Sanji', 'Vinsmoke'))
    print(get_role('Luffy', 'Monkey D.', 'Pirate King'))