import requests
from bs4 import BeautifulSoup
from domain.concurso import Concurso
import asyncio
from application.filtros import filtrar_concurso

class PCICrawler:
    BASE_URL = "https://www.pciconcursos.com.br/concursos"

    async def buscar_concursos(self):
        print("[Crawler] Acessando site:", self.BASE_URL)

        
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, requests.get, self.BASE_URL)

        if response.status_code != 200:
            print(f"[Crawler] Erro ao acessar PCI ({response.status_code})")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        concursos_html = soup.select("div.da")
        print(f"[Crawler] Encontrados {len(concursos_html)} concursos na página")

        concursos = []
        for c in concursos_html:
            links = c.find_all("a")
            orgao = links[0]
            apostila = links[1]
            estado = c.select("div.cc")[0]
            
            if("MA" not in estado):
                continue
            # data = c.find("div", class_="ca_data")
            link_edital = orgao.get("href") if orgao and orgao.get("href") else "Não informado"

            if not orgao:
                continue
            
            # navigate to link_edital
            edital_response = await loop.run_in_executor(None, requests.get, orgao.get("href"))

            if edital_response.status_code == 200:
                edital_soup = BeautifulSoup(edital_response.text, "html.parser")
                
                paragrafos_edital = edital_soup.select("p")
                
                concurso = Concurso(
                    orgao=orgao.text.strip() if orgao else "Não informado",
                    # data=data.text.strip() if data else "Não informado",
                    vagas="",
                    area="",
                    link_edital=link_edital,
                )

                for p in paragrafos_edital:
                    if filtrar_concurso(concurso, p.text):
                        concursos.append(concurso)
                        break

            else:
                print(f"[Crawler] Erro ao acessar edital ({edital_response.status_code})")

        return concursos