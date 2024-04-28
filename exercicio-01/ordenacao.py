

class Ordenacao():

    def __init__(self, array_para_ordenar: list):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array_para_ordenar = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        # Using booble sort method
        array_size = len(self.array_para_ordenar)
        for i in range(array_size - 1):
            for j in range(array_size-i):
                if (j+1 < array_size and self.array_para_ordenar[j] > self.array_para_ordenar[j + 1]):
                    bigger_value = self.array_para_ordenar[j]
                    lower_value = self.array_para_ordenar[j + 1]
                    self.array_para_ordenar[j + 1] = bigger_value
                    self.array_para_ordenar[j] = lower_value

        return self.array_para_ordenar

    def to_string(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        string = str()
        for index in range(len(self.array_para_ordenar)):
            number_string = str(self.array_para_ordenar[index])
            if (index == (len(self.array_para_ordenar) - 1)):
                string += number_string
            else:
                string += number_string + ','

        return string
