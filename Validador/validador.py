import re


class Validador:
    @staticmethod
    def validar_cep(cep):
        if not isinstance(cep, str):
            raise ValueError("O CEP deve ser uma string")

        # Remove todos os caracteres não numéricos
        cep_limpo = re.sub(r'[^0-9]', '', cep)

        # Verifica se tem 8 dígitos
        if len(cep_limpo) != 8:
            return False

        return True

    @staticmethod
    def validar_cpf(cpf):
        if not isinstance(cpf, str):
            raise ValueError("O CPF deve ser uma string")

        # Remove todos os caracteres não numéricos
        cpf_limpo = re.sub(r'[^0-9]', '', cpf)

        # Verifica se tem 11 dígitos
        if len(cpf_limpo) != 11:
            return False

        return True

    @staticmethod
    def validar_cnpj(cnpj):
        if not isinstance(cnpj, str):
            raise ValueError("O CNPJ deve ser uma string")

        # Remove todos os caracteres não numéricos
        cnpj_limpo = re.sub(r'[^0-9]', '', cnpj)

        # Verifica se tem 14 dígitos
        if len(cnpj_limpo) != 14:
            return False

        return True