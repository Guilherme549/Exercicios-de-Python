def notas(* nota, sit=False):
    """
    :para nota: recebe as notas do aluno
    :para sit: com o sit igual a True (valor opcional) é possivel mostrar qual a situação das notas do aluno
    :para return: retorna um dicionário com com a maior e menor nota, media do aluno e quantidade de notas
    """
    boletim = dict()
    boletim["total"] = len(nota)
    boletim["maior"] = max(nota)
    boletim["menor"] = min(nota)
    boletim["média"] = sum(nota) / boletim['total']
    if sit == True:
        if boletim['média'] > 7:
            boletim["situacao"] = "BOA"
        if boletim['média'] > 6 and boletim['média'] < 7:
            boletim["situacao"] = "RAZOAVEL"
        if boletim['média'] < 6:
            boletim["situacao"] = "RUIM"

    return boletim


resp = notas(10, 10, 10, sit=True)
print(resp)
help(notas)
