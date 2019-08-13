import re

# Compilando as regex pra melhorar o desempenho
check_alternate_pairs = re.compile(r'(\d)\d\1')
check_size = re.compile(r'^\d{6}$')

def Validate(cep):
    """Valida o cep. 'cep' deve ser string, retorno booleano."""
    if (len(check_size.findall(cep)) == 0) or not (100000 < int(cep) < 999999):
        # cep fora do padrão básico
        raise Exception(f'CEP "{cep}" fora do padrão.')

    r = check_alternate_pairs.findall(cep)
    return len(r) == 0
