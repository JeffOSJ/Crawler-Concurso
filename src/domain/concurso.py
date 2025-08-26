class Concurso:
    def __init__(self, orgao, vagas, area, link_edital):
        self.orgao = orgao
        self.vagas = vagas
        self.area = area
        self.link_edital = link_edital

        
    def __str__(self):
        # return f"{self.orgao} - {self.area} - {self.vagas} - Edital: {self.link_edital}"
        return f"{self.vagas}-{self.link_edital}"