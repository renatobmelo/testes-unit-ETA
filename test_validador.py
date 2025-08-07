import pytest
from validador import Validador

@pytest.fixture
def validador():
    return Validador()

# Testes para validar_cep
@pytest.mark.parametrize("cep, esperado", [
    ("12345678", True),         # Válido sem máscara
    ("12.345-678", True),       # Válido com máscara
    ("01001000", True),         # Válido (CEP real)
    ("1234567", False),         # Inválido (tamanho menor)
    ("123456789", False),       # Inválido (tamanho maior)
    ("12a34567", False),        # Inválido (contém letra)
])
def test_validar_cep_casos_validos_e_invalidos(validador, cep, esperado):
    assert validador.validar_cep(cep) == esperado

@pytest.mark.parametrize("cep", [
    12345678,                   # Número inteiro
    None,                       # None
    ["12345678"],               # Lista
    {"cep": "12345678"},        # Dicionário
])
def test_validar_cep_levanta_value_error_para_nao_string(validador, cep):
    with pytest.raises(ValueError):
        validador.validar_cep(cep)

# Testes para validar_cpf
@pytest.mark.parametrize("cpf, esperado", [
    ("12345678901", True),      # Válido (qualquer combinação com 11 dígitos)
    ("123.456.789-01", True),   # Válido com máscara
    ("1234567890", False),      # Inválido (tamanho menor)
    ("123456789012", False),    # Inválido (tamanho maior)
    ("123a5678901", False),     # Inválido (contém letra)
])
def test_validar_cpf_casos_validos_e_invalidos(validador, cpf, esperado):
    assert validador.validar_cpf(cpf) == esperado

@pytest.mark.parametrize("cpf", [
    12345678901,                # Número inteiro
    None,                       # None
    ["12345678901"],            # Lista
    {"cpf": "12345678901"},     # Dicionário
])
def test_validar_cpf_levanta_value_error_para_nao_string(validador, cpf):
    with pytest.raises(ValueError):
        validador.validar_cpf(cpf)

# Testes para validar_cnpj
@pytest.mark.parametrize("cnpj, esperado", [
    ("11222333000181", True),           # Válido (qualquer combinação com 14 dígitos)
    ("11.222.333/0001-81", True),       # Válido com máscara
    ("1122233300018", False),           # Inválido (tamanho menor)
    ("112223330001811", False),         # Inválido (tamanho maior)
    ("1122233300a181", False),          # Inválido (contém letra)
])
def test_validar_cnpj_casos_validos_e_invalidos(validador, cnpj, esperado):
    assert validador.validar_cnpj(cnpj) == esperado

@pytest.mark.parametrize("cnpj", [
    11222333000181,             # Número inteiro
    None,                       # None
    ["11222333000181"],         # Lista
    {"cnpj": "11222333000181"}, # Dicionário
])
def test_validar_cnpj_levanta_value_error_para_nao_string(validador, cnpj):
    with pytest.raises(ValueError):
        validador.validar_cnpj(cnpj)