####################################################################################
#   __                            _
#  / _|__      ____      __  ___ | |__    ___ __  __
# | |_ \ \ /\ / /\ \ /\ / / / _ \| '_ \  / _ \\ \/ /
# |  _| \ V  V /  \ V  V / |  __/| |_) ||  __/ >  <
# | |_|    \_/\_/    \_/\_/   \___||_.__/  \___|/_/\_\
#
# html2fwwebex.py
#
# Released to Public Domain.
#####################################################################################
import argparse
import html
from bs4 import BeautifulSoup, Comment

def indent(level):
    return "    " * level

# Mapeamento de caracteres Unicode para entidades HTML
ENTITY_MAP = {
    '©': '&copy;',
    '·': '&middot;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&apos;'
}

def preserve_entities(text):
    """Converte caracteres Unicode para suas entidades HTML correspondentes."""
    # Primeiro, escapa caracteres especiais, exceto &
    text = html.escape(text, quote=True)
    # Aplica mapeamento específico para entidades como &copy; e &middot;
    for char, entity in ENTITY_MAP.items():
        text = text.replace(html.escape(char), entity)
    # Preserva &amp; como &amp; sem dupla codificação
    text = text.replace('&amp;', '&amp;')
    return text

def process_element(el, level=0, count=[0]):
    lines = []

    # Se for um comentário
    if isinstance(el, Comment):
        count[0] += 1
        var = f"oComment{count[0]}"
        lines.append(f"{indent(level)}{var} := WebExControl():New( \"!--\" )")
        content = str(el).strip().replace('"', '\\"')
        if content:
            content = preserve_entities(content)
            lines.append(f"{indent(level)}{var}:SetContent( \"{content}\" )")
        return lines, var

    # Se não for uma tag válida, retorna vazio
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
        elif attr == "href" and value == ":back":
            # Tratamento especial para href=":back" (navegação de retorno)
            lines.append(f"{indent(level)}{var}:SetAttr( \"href\", \"javascript:history.back()\" )")
        else:
            # Demais atributos são tratados diretamente
            attr_value = str(value).replace('"', '\\"')
            lines.append(f"{indent(level)}{var}:SetAttr( \"{attr}\", \"{attr_value}\" )")

    # Acumula linhas de conteúdo e filhos na ordem do DOM
    content_lines = []
    last_child_var = None
    for content in el.contents:
        if isinstance(content, str) and not isinstance(content, Comment) and content.strip():
            content = content.strip().replace('"', '\\"')
            content = preserve_entities(content)
            if last_child_var:
                content_lines.append(f"{indent(level)}{var}:SetContent( \"{content}\", {last_child_var}:GetID() )")
            else:
                content_lines.append(f"{indent(level)}{var}:SetContent( \"{content}\" )")
        else:
            # Processa comentários ou elementos como filhos
            child_lines, child_var = process_element(content, level + 1, count)
            content_lines.extend(child_lines)
            if child_var:
                content_lines.append(f"{indent(level)}{var}:AddChild( {child_var} )")
                last_child_var = child_var

    # Adiciona as linhas acumuladas após processar todos os conteúdos
    lines.extend(content_lines)

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
    if not body:
        raise ValueError("O arquivo HTML não contém uma tag <body> válida.")

    lines, top_var = process_element(body)

    # Finalização
    lines.append(f"Self:AddChild( {top_var} )")

    # Salvar como arquivo TLPP
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Arquivo TLPP gerado com sucesso em {args.output_file}!")

if __name__ == "__main__":
    main()
