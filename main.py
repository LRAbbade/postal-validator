import re

def Validate(cep):
    """Valida o cep. 'cep' deve ser string, retorno booleano."""
    if (len(cep) != 6) or not (100000 < int(cep) < 999999):         # cep fora do padrão básico
        raise Exception(f'CEP "{cep}" inválido.')

    return True
