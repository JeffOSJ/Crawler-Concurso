def filtrar_concurso(concurso, conteudo_paragrafo):
    palavras_chave_ti = [
        "TI", "Tecnologia da Informação", "Informatica", "Informática",
        "Analista de Sistemas", "Desenvolvedor", "Programador",
        "Banco de Dados", "DBA", "Redes", "Infraestrutura"
    ]
    
    palavras_chave_direito = [
        "Direito", "Procurador", "Advogado", "Jurídico",
        "Juridico", "Legislativo", "Judiciário", "Auditor","Judiciario"
    ]
    
    palavra_chave_estado = [
        "Maranhão", "MA", "São Luís"
    ]

    if any(palavra in conteudo_paragrafo for palavra in palavra_chave_estado):
        concurso.estado = "Maranhão"

    if any(palavra in conteudo_paragrafo for palavra in palavras_chave_ti):
        concurso.area  = "TI"
        vagas_separadas = conteudo_paragrafo.split(";")
        
        for palavra_chave in palavras_chave_ti:
            for vaga in vagas_separadas:
                if palavra_chave in vaga:
                    concurso.vagas += vaga.strip()
                    
    
    if any(palavra in conteudo_paragrafo for palavra in palavras_chave_direito):
        if concurso.area:
            concurso.area += " e Direito"
        else:
            concurso.area = "Direito"
            
        vagas_separadas = conteudo_paragrafo.split(";")
            
        for palavra_chave in palavras_chave_direito:
            for vaga in vagas_separadas:
                if palavra_chave in vaga:
                    concurso.vagas += vaga.strip()
    
    if concurso.area:
        return True

    return False