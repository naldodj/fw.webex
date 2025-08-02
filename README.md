# FW.WebEX — Framework Web Extensível para Protheus (ADVPL/TLPP) 🌟

## ⭐Gostou do projeto? Deixa uma estrelinha(⭐) aí no topo! Isso ajuda muito!

[![Stars](https://img.shields.io/github/stars/DNATechByNaldoDJ/fw.webex?style=social)](https://github.com/DNATechByNaldoDJ/fw.webex)
![Clones](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/DNATechByNaldoDJ/fw.webex/main/clone-badge.json)

![fwwebex_banner](https://github.com/user-attachments/assets/64a542a9-97f3-47b0-81f9-1655374a1a90)

--
**FW.WebEX** é um microframework escrito em ADVPL/TLPP que permite criar interfaces web responsivas, modernas e funcionais **diretamente do seu código no Protheus**, sem precisar de Angular, React ou qualquer outra parafernália.

> **Do Protheus para o browser. Simples. Direto. Web.**

---

## 🚀 Por que FW.WebEX?

A TOTVS está indo para o web. Mas o desenvolvedor ADVPL n&atilde;o precisa (re)aprender Angular ou TypeScript só pra fazer uma tela de cadastro ou uma tabela com ação.

**FW.WebEX** nasceu da ideia de manter o espírito do desenvolvimento no Protheus:

- Rápido
- Sem burocracia
- Produtivo

Só que agora... **na web.**

---

## ⚙️ O que ele faz?

- Gera páginas HTML com sintaxe 100% TLPP
- Usa **Bootstrap** para comportamento (modais, tabelas, botões)
- Pode usar **PO UI (opcional)** para identidade visual padrão TOTVS
- Tem componentes já prontos como:
  - `fw.webex.page`
  - `fw.webex.control`
  - `fw.webex.table` (com checkbox, modal de exclusão, etc.)
- Permite encadeamento estilo `WITH OBJECT ... END`, via `WithObject()/EndWith()`

---

## 💡 Exemplo de uso (1)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_001()
    local bExecute as codeblock
    local cHTMLFile as character
    local cProcName:=ProcName() as character
    bExecute:={||FWMsgRun(nil,{||cHTMLFile:=FWWebExExample_001()},"Aguarde",cProcName)}
    FWExampleTools():Execute(bExecute,cProcName,.T.)
    if (!Empty(cHTMLFile).and.File(cHTMLFile))
        ShellExecute("open",cHTMLFile,"","",1)
    endif
return

static function FWWebExExample_001() as character

    local cHTML as character
    local cProcName:=ProcName() as character
    local cHTMLFile:=cProcName as character
    local cSX5TableName:=RetSQLName("SX5") as character

    local oFWWebExPage as object

    WITH WEBEXOBJECT oFWWebExPage CLASS WebExPage ARGS cProcName
        WITH WEBEXOBJECT CLASS WebExBody
            WITH WEBEXOBJECT CLASS WebExMain
                WITH WEBEXOBJECT CLASS WebExTemplateBulkActionTable ARGS cProcName+" (Tabela 32)"
                    .:FromSQL("SELECT * FROM "+cSX5TableName+" WHERE X5_TABELA='32' AND D_E_L_E_T_<>'*'")
                END WEBEXOBJECT
                WITH WEBEXOBJECT CLASS WebExHR
                END WEBEXOBJECT
                WITH WEBEXOBJECT CLASS WebExTemplateBulkActionTable ARGS cProcName+" (Tabela 35)"
                    .:FromSQL("SELECT * FROM "+cSX5TableName+" WHERE X5_TABELA='35' AND D_E_L_E_T_<>'*'")
                END WEBEXOBJECT
            END WEBEXOBJECT
        END WEBEXOBJECT
    END WEBEXOBJECT

    WebFileTools():HTMLFromControl(oFWWebExPage,GetTempPath(),@cHTMLFile,@cHTML,.T.)

    WEBEXOBJECT CLEAN

return(cHTMLFile)
````

![image](https://github.com/user-attachments/assets/65c4706b-420e-40c4-a0dc-8b9412cd186f)

---

## 💡 Exemplo de uso (3)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_003()
    local bExecute as codeblock
    local cHTML as character
    local cHTMLFile as character
    local cProcName:=ProcName() as character
    bExecute:={||FWMsgRun(nil,{||cHTMLFile:=FWWebExExample_003(@cHTML)},"Aguarde",cProcName)}
    FWExampleTools():Execute(bExecute,cProcName,.T.)
    if (!Empty(cHTMLFile).and.File(cHTMLFile))
        FWExampleTools():htmlFileShow(cHTML,cProcName,cHTMLFile)
        fErase(cHTMLFile)
    endif
return

static function FWWebExExample_003(cHTML as character) as character

    local cScript as character
    local cProcName:=ProcName() as character
    local cHTMLFile:=cProcName as character

    local oFWWebExPage as object

    WITH WEBEXOBJECT oFWWebExPage CLASS WebExPage ARGS cProcName
        WITH WEBEXOBJECT CLASS WebExBody
            WITH WEBEXOBJECT CLASS WebExMain
                WITH WEBEXOBJECT CLASS WebExForm ARGS "Consulta CEP"
                    .:SetFormMethod("get")
                    .:SetFormAction("javascript:buscarCEP()")
                    .:AddField("CEP","cep","text","Digite o CEP")
                    .:AddButton(WebExButton():New("Buscar CEP"))
                END WEBEXOBJECT
                WITH WEBEXOBJECT CLASS WebExScript
                    beginContent var cScript

                        function buscarCEP() {

                        const cep = document.querySelector("input[name='cep']").value.trim();
                        const url = `https://viacep.com.br/ws/${cep}/json/`;

                        fetch(url)
                            .then(response => response.json())
                            .then(data => {
                            if (data.erro) {
                                document.getElementById("resultadoCEP").innerHTML = "<div class='alert alert-danger'>CEP n&atilde;o encontrado.</div>";
                            } else {
                                document.getElementById("resultadoCEP").innerHTML = `
                                <div class='card'>
                                    <div class='card-body'>
                                    <h5 class='card-title'>Endere&ccedil;o</h5>
                                    <p class='card-text'>
                                        <strong>CEP:</strong> ${data.cep}<br/>
                                        <strong>Logradouro:</strong> ${data.logradouro} -
                                        <strong>Complemento:</strong> ${data.complemento} -
                                        <strong>Unidade:</strong> ${data.unidade}<br/>
                                        <strong>Bairro:</strong> ${data.bairro} -
                                        <strong>Localidade:</strong> ${data.localidade}<br/>
                                        <strong>UF:</strong> ${data.uf} -
                                        <strong>Estado:</strong> ${data.estado}<br/>
                                        <strong>Regi&atilde;o:</strong> ${data.regiao} -
                                        <strong>IBGE:</strong> ${data.ibge}<br/>
                                        <strong>GIA:</strong> ${data.gia} -
                                        <strong>DDD:</strong> ${data.ddd}<br/>
                                        <strong>SIAFI:</strong> ${data.siafi}<br/>
                                    </p>
                                    </div>
                                </div>
                                `;
                            }
                            })
                            .catch(() => {
                            document.getElementById("resultadoCEP").innerHTML = "<div class='alert alert-danger'>Erro ao consultar o CEP.</div>";
                            });
                        }

                    endContent
                    .:SetContent(cScript)
                END WEBEXOBJECT
                WITH WEBEXOBJECT CLASS WebExControl TYPE div
                    .:SetFixedID("resultadoCEP")
                    .:SetAttr("class","mt-4")
                END WEBEXOBJECT
            END WEBEXOBJECT
        END WEBEXOBJECT
    END WEBEXOBJECT

    WebFileTools():HTMLFromControl(oFWWebExPage,oFWWebExPage:GetFWWebExTmpPath(),@cHTMLFile,@cHTML,.T.)

    WEBEXOBJECT CLEAN

return(cHTMLFile)
````

![WebExForm](https://github.com/user-attachments/assets/fcf7609f-a2be-43b4-b63e-af5aa2718d58)

---

## 🧩 Dependências

- Nenhuma no backend (ADVPL puro)
- Frontend usa:

  - [Bootstrap 5.n](https://getbootstrap.com)
  - (opcional) [PO UI CSS](https://po-ui.io)

---

## 📦 Como usar

1. Clone o repositório
2. Compile
3. Use

---

## 🤝 Quer contribuir?

Toda ajuda é bem-vinda! A ideia aqui é **evoluir juntos** como comunidade Protheus:

- Criar novos componentes (`fw.webex.form`, `fw.webex.chart`, etc.)
- Melhorar o renderizador
- Adicionar eventos dinâmicos
- Documentar com mais exemplos

---

## 🛠️ Como Participar

Contribuições são bem-vindas! Siga estas diretrizes para garantir a consistência do código:

🧾 Estilo de Codificação

- Indentação: use 4 espaços por nível de indentação.
- Parênteses, chaves, colchetes: sempre com espaçamento correto e estilo claro.
- return: deve sempre iniciar na mesma coluna do nível atual (sem recuo adicional).
- Nomes de métodos e variáveis: utilize nomes descritivos em inglês, com camelCase para métodos e snake_case para variáveis locais se necessário.
- Classes: o nome deve ser prefixado por WebEx e descrever a função do componente (ex: WebExForm, WebExTable, WebExCardKPI).
- Arquivos: devem estar organizados por tipo (ex: forms/, tables/, components/) dentro de src/fw.webex.

🧪 Contribuindo com Novos Exemplos

- Crie uma nova função com nome u_FWWebExExample_XXX() onde XXX é o próximo número disponível.
- Armazene o exemplo em src/fw.webex.examples/.
- Mantenha a mesma estrutura dos exemplos existentes:

Página HTML gerada via TL++.

Uso de objetos WebEx*.

Interface limpa e responsiva.

📎 Convenções de Commit

Utilizamos padrão Harbour: [How to Participate](https://github.com/naldodj/naldodj-harbour-core#how-to-participate)

```text
2025-07-01 HH:MM UTC seu_nome (contexto)
  + src/...      ; Adição
  - src/...      ; Remoção
  * src/...      ; Alteração
  ! src/...      ; Correção
  % src/...      ; Otimização
```

---

## ✨ Visão

> Acreditamos que dá pra evoluir mantendo o que o Protheus tem de melhor: a produtividade.
> FW\.WebEX é o passo que faltava pra quem quer ir pro web **sem perder a alma ADVPL**.

---

## ⭐ Gostou do projeto? Deixa uma estrelinha(⭐) aí no topo! Isso ajuda muito!

[![Stars](https://img.shields.io/github/stars/DNATechByNaldoDJ/fw.webex?style=social)](https://github.com/DNATechByNaldoDJ/fw.webex)
![Clones](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/DNATechByNaldoDJ/fw.webex/main/clone-badge.json)

---

### ✅ Configuration: `[FWWEBEX]` Section in `appserver.ini`

To enable integration with the FWWebEx REST services, make sure to include the following configuration in your `appserver.ini` file:

```ini
[FWWEBEX]
RestURL=<e.g.:https://localhost:8091/app-root/>
OAuth2URL=<e.g.:https://localhost:8091/rest/tlpp/oauth2/token>
AppRootURI=<e.g.:https://localhost:8091/app-root/>
ClientID=<e.g.:000000>
ClientSecret=<e.g.:admin>
UserName=<e.g.:admin>
Password=<e.g.:admin>
```

⚠️ **Note:** The `AppRootURI` value is currently required as a manual setting. Ideally, this value should be automatically retrieved from the system. A future improvement may address this limitation.

---

## 📄 Licença

[MIT](LICENSE)

---

<img width="1024" height="1024" alt="dna_tech_logo_black_panter" src="https://github.com/user-attachments/assets/9b39a407-31ca-4a86-a1df-f76790e2036a" />
