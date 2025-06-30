# Caminho do arquivo original
$arquivoJson = "turnovergeralfuncionarios.json"

# Le o conteudo do arquivo JSON
$json = Get-Content $arquivoJson -Raw | ConvertFrom-Json

# Acessa os itens da tabela
$items = $json.table.items

foreach ($item in $items) {
    $codMatricula = $item.detail.items.codMatricula
    $item.detail.items.nomeFuncionario = "FUNCIONARIO $codMatricula"
}

# Converte de volta para JSON
$jsonFinal = $json | ConvertTo-Json -Depth 10

# Salva em novo arquivo (pode sobrescrever se quiser)
$jsonFinal | Set-Content "turnovergeralfuncionarios.json" -Encoding UTF8
