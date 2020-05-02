import re


def is_cnpj_valid(cnpj):
    """ If cnpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

    # Check if type is str
    if not isinstance(cnpj, str):
        return False

    # Remove some unwanted characters
    cnpj = re.sub("[^0-9]", '', cnpj)

    # Checks if string has 11 characters
    if len(cnpj) != 14:
        return False

    sum = 0
    weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    """ Calculating the first cpf check digit. """
    for n in range(12):
        value = int(cnpj[n]) * weight[n]
        sum = sum + value

    verifying_digit = sum % 11

    if verifying_digit < 2:
        first_verifying_digit = 0
    else:
        first_verifying_digit = 11 - verifying_digit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for n in range(13):
        sum = sum + int(cnpj[n]) * weight[n]

    verifying_digit = sum % 11

    if verifying_digit < 2:
        second_verifying_digit = 0
    else:
        second_verifying_digit = 11 - verifying_digit

    if cnpj[-2:] == "%s%s" % (first_verifying_digit, second_verifying_digit):
        return True
    return False


def is_cpf_valid(cpf):
    """ If cpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

    # Check if type is str
    if not isinstance(cpf, str):
        return False

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]", '', cpf)

    # Checks if string has 11 characters
    if len(cpf) != 11:
        return False

    # Para validar cpfs com sequencia de valores repetidos, por exemplo:
    # 111.111.111-11, 222.222.222-22, .., 999.999.999-99
    if cpf == len(cpf) * cpf[0]:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifying_digit = 11 - sum % 11

    if verifying_digit > 9:
        first_verifying_digit = 0
    else:
        first_verifying_digit = verifying_digit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifying_digit = 11 - sum % 11

    if verifying_digit > 9:
        second_verifying_digit = 0
    else:
        second_verifying_digit = verifying_digit

    if cpf[-2:] == "%s%s" % (first_verifying_digit, second_verifying_digit):
        return True
    return False


def keep_only_numbers(value):
    return re.sub("[^0-9]", "", value)
