class Validator():

    def cnpj_alfanumerico(self, CNPJ: str) -> bool:
        if(not CNPJ):
            raise TypeError('CNPJ is empty or None.')
        
        if(self.todos_digitos_iguais(CNPJ)):
            raise Exception("CNPJ has all characters equals")
        
        cnpj_sem_mascara: str = self.remove_mask_cnpj(CNPJ)

        if len(cnpj_sem_mascara) != 14:
            raise IndexError("CNPJ has more or less than 14 characters.")
        
        cnpj_parcializado: str = cnpj_sem_mascara[:-2]

        for _ in range(2):
            cnpj_parcializado += str(self.total_cnpj(cnpj_parcializado))

        if cnpj_parcializado == cnpj_sem_mascara:
            return True

        return False


    def total_cnpj(self, cnpj_sliced: str) -> int:
        peso: str = ''
        count: int = 0
        result: int = 0
        total: int = 0

        if len(cnpj_sliced) == 12:
            peso = "543298765432"
        else:
            peso = "6543298765432"

        for i in range(len(peso)):
            count = ord(cnpj_sliced[i]) - 48
            count = count * int(peso[i])
            total += count
            count = 0 

        result = total % 11

        if (result == 0) or (result == 1):
            result = 0
        else:
            result = 11 - result

        return result
    
    
    def remove_mask_cnpj(self, cnpj_mascarado: str) -> str: 
        simbolos_mascara: list[str] = ['-', '/', '.']
        cnpj_limpo: str = cnpj_mascarado

        for simbolo in simbolos_mascara:
            if simbolo in cnpj_mascarado:
                cnpj_limpo = cnpj_limpo.replace(simbolo, '')

        return cnpj_limpo

    
    def todos_digitos_iguais(self, cnpj: str) -> bool:
        primeiro_digito: str = cnpj[0]

        if primeiro_digito * 14 == cnpj:
            return True

        return False