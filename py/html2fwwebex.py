####################################################################################
#   __                            _
#  / _|__      ____      __  ___ | |__    ___ __  __
# | |_ \ \ /\ / /\ \ /\ / / / _ \| '_ \  / _ \\ \/ /
# |  _| \ V  V /  \ V  V / |  __/| |_) ||  __/ >  <
# |_|    \_/\_/    \_/\_/   \___||_.__/  \___|/_/\_\
#
# html2fwwebex.py
#
#Released to Public Domain.
#####################################################################################
import argparse
from bs4 import BeautifulSoup

def indent(level):
    return "    " * level

def process_element(el, level=0, count=[0]):
    lines = []
    tag = el.name
    if not tag:
        return [], None

    count[0] += 1
    var = f"o{tag.capitalize()}{count[0]}"
    lines.append(f"{indent(level)}{var} := WebExControl():New( \"{tag}\" )")

    # Processa todos os atributos de forma genérica
    for attr, value in el.attrs.items():
        if attr == "class":
            # Tratamento especial para classes (lista de strings)
            class_str = " ".join(value)
            lines.append(f"{indent(level)}{var}:SetAttr( \"class\", \"{class_str}\" )")
        elif attr == "id":
            # Tratamento especial para id (usando SetFixedID)
            lines.append(f"{indent(level)}{var}:SetFixedID( \"{value}\" )")
        else:
            # Demais atributos são tratados diretamente
            attr_value = str(value).replace('"', '\\"')
            lines.append(f"{indent(level)}{var}:SetAttr( \"{attr}\", \"{attr_value}\" )")

    # Se tiver conteúdo textual direto
    if el.string and el.string.strip():
        content = el.string.strip().replace('"', '\\"')
        lines.append(f"{indent(level)}{var}:SetContent( \"{content}\" )")

    # Processa filhos diretos (sem recursividade total)
    for child in el.find_all(recursive=False):
        child_lines, child_var = process_element(child, level + 1, count)
        lines.extend(child_lines)
        if child_var:
            lines.append(f"{indent(level)}{var}:AddChild( {child_var} )")

    return lines, var

def main():
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(description="Converte arquivo HTML para TLPP.")
    parser.add_argument("input_file", help="Caminho para o arquivo HTML de entrada")
    parser.add_argument("output_file", help="Caminho para o arquivo TLPP de saída")
    args = parser.parse_args()

    # Carregar o HTML
    with open(args.input_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    body = soup.body
    lines, top_var = process_element(body)

    # Finalização
    lines.append(f"Self:AddChild( {top_var} )")

    # Salvar como arquivo TLPP
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Arquivo TLPP gerado com sucesso em {args.output_file}!")

if __name__ == "__main__":
    main()
