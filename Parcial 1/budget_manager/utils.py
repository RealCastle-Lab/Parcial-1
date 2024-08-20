# utils.py

def input_float(prompt, error_message="Invalid input, please enter a valid number"):
    """ Solicita al usuario un valor flotante, repite hasta que se ingrese un valor válido. """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(error_message)

def input_integer(prompt, error_message="Invalid input, please enter a valid integer"):
    """ Solicita al usuario un valor entero, repite hasta que se ingrese un valor válido. """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(error_message)

def confirm_action(prompt):
    """ Pide al usuario confirmación antes de realizar una acción. """
    while True:
        choice = input(prompt + " (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def format_article(article):
    """ Devuelve una cadena formateada de los detalles de un artículo. """
    if not article:
        return "Article not found."
    return f"ID: {article.id}, Name: {article.name}, Description: {article.description}, Price: ${article.price:.2f}"
