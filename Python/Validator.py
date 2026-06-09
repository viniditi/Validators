class Validator():

    def validate_cnpj(self, CNPJ: str) -> bool:
        """
        Checks if CNPJ is valid or not. It does valite alphanumeric CNPJ as well.

        Args:
            CNPJ (str) : CNPJ to validate. It can be numeric or alphanumeric.
        
        Returns:
            bool: Returns True if CNPJ is valid, and False if invalid.
        """
        if(not CNPJ):
            raise TypeError('CNPJ is empty or None.')
        
        if(self.equal_digits(CNPJ)):
            raise Exception("CNPJ has all equals characters.")
        
        cnpj_without_mask: str = self.remove_mask_cnpj(CNPJ)

        if len(cnpj_without_mask) != 14:
            raise IndexError("CNPJ has more or less than 14 characters.")
        
        sliced_cnpj: str = cnpj_without_mask[:-2]

        for _ in range(2):
            sliced_cnpj += str(self.total_cnpj(sliced_cnpj))

        if sliced_cnpj == cnpj_without_mask:
            return True

        return False


    def total_cnpj(self, sliced_cnpj: str) -> int:
        """
        Calculates the first and second check digit of CNPJ.

        Args:
            sliced_cnpj (str) : The first 12th or 13th first digits of a CNPJ. It can be numeric or alphanumeric.
        
        Returns:
            int: Returns the calculation of the first check digit of CNPJ if the size of sliced_cnpj is 12 characters; if sliced_cnpj has 13 characters, returns the second check digit of the CNPJ.
        """
        weight: str = ''
        count: int = 0
        result: int = 0
        total: int = 0

        if len(sliced_cnpj) == 12:
            weight = "543298765432"
        else:
            weight = "6543298765432"

        for i in range(len(weight)):
            count = ord(sliced_cnpj[i]) - 48
            count = count * int(weight[i])
            total += count
            count = 0 

        result = total % 11

        if (result == 0) or (result == 1):
            result = 0
        else:
            result = 11 - result

        return result
    
    
    def remove_mask_cnpj(self, masked_cnpj: str) -> str: 
        """
        Removes the mask of CNPJ.

        Args:
            masked_cnpj (str) : CNPJ with mask to remove it, e.g.: AB.CDE.FGH/IJKL-12. It can be numeric or alphanumeric.
        
        Returns:
            str: Returns the CNPJ with no mask.
        """
        cnpj_without_mask: list[str] = ['-', '/', '.']
        cnpj_limpo: str = masked_cnpj

        for symbol in cnpj_without_mask:
            if symbol in masked_cnpj:
                cnpj_limpo = cnpj_limpo.replace(symbol, '')

        return cnpj_limpo

    
    def equal_digits(self, cnpj: str) -> bool:
        """
        Verify if all digits are equal.

        Args:
            cnpj (str) : CNPJ to validate. It can be numeric or alphanumeric.
        
        Returns:
            bool: Returns True if all digits are equal and False if at least one of then is different.
        """
        first_digit: str = cnpj[0]

        if first_digit * 14 == cnpj:
            return True

        return False