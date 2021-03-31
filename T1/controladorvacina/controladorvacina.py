from vacina import Vacina

class ControladorVacina:

    def __init__(self):
        self.__lista_vacinas: []
    
    def incluir_vacinas(self, nome: str, fabricante: str, qtd_doses: int) -> Vacina:

        nova_vacina = None
        if isinstance(nome, str) and isinstance(fabricante, str) and isinstance(qtd_doses, int):
            
            nova_vacina =  Vacina(nome, fabricante , qtd_doses)

            for vacina in self.__lista_vacinas:
                if vacina.nome == nome:
                    nova_vacina = None
            if nova_vacina is not None:
                self.__lista_vacinas.append(nova_vacina)
            return nova_vacina
    
    def excluir_vacina(self, vacina: Vacina):

        if isinstance(vacina, Vacina) and vacina is not None:
            if vacina in self.__lista_vacinas:
                self.__lista_vacinas.remove(vacina)
            else:
                print ("está vacina não está cadastrada")
    
    def doses_disponiveis(self, vacina: Vacina):
    
        if isinstance(vacina, Vacina) and vacina is not None:
            for vacina in self.__lista_vacinas:
                return vacina.qtd_doses