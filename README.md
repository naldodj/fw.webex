# FW.WebEX — Framework Web Extensível para Protheus (ADVPL/TLPP)
![dna_tech_logo_black_panter](https://github.com/user-attachments/assets/b3e14547-41e0-484f-9d42-533fc71c28b8)
--
**FW.WebEX** é um microframework escrito em ADVPL/TLPP que permite criar interfaces web responsivas, modernas e funcionais **diretamente do seu código no Protheus**, sem precisar de Angular, React ou qualquer outra parafernália.

> **Do Protheus para o browser. Simples. Direto. Web.**

---

## 🚀 Por que FW.WebEX?

A TOTVS está indo para o web. Mas o desenvolvedor ADVPL não precisa reaprender Angular ou TypeScript só pra fazer uma tela de cadastro ou uma tabela com ação.

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

#include "tbiconn.ch"

using namespace FWWebEx

procedure u_FWWebExExample_001()
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"
        FWWebExExample_001()
    RESET ENVIRONMENT
return

static procedure FWWebExExample_001()

    local cHTML as character
    local cHTMLFile as character
    local cProcName:=ProcName() as character

    local oFWWebExPage as object

    WITH WEBEXOBJECT oFWWebExPage CLASS WebExPage ARGS cProcName
        WITH WEBEXOBJECT CLASS WebExTemplateBulkActionTable ARGS cProcName
            .:FromSQL("SELECT TOP 10 * FROM SX5990")
        END WEBEXOBJECT
        cHTML:=oFWWebExPage:Render()
    END WEBEXOBJECT

    FreeObj(@oFWWebExPage)

    cHTML:=EncodeUTF8(cHTML)
    cHTMLFile:="c:\tmp\"+Lower(cProcName)+".html"

    MemoWrite(cHTMLFile,cHTML)

    ShellExecute("open",cHTMLFile,"","",1)

return
````
![image](https://github.com/user-attachments/assets/65c4706b-420e-40c4-a0dc-8b9412cd186f)
---
## 💡 Exemplo de uso (2)

```advpl
#include "fw.webex.th"

#include "shell.ch"
#include "totvs.ch"
#include "fileio.ch"
#include "tbiconn.ch"

using namespace FWWebEx

procedure u_FWWebExExample_003()
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"
        FWWebExExample_003()
    RESET ENVIRONMENT
return

static procedure FWWebExExample_003()

    local cHTML as character
    local cHTMLFile as character

    local cScript as character
    local cProcName:=ProcName() as character

    local oFWWebExPage as object

    WITH WEBEXOBJECT oFWWebExPage CLASS WebExPage ARGS cProcName
        WITH WEBEXOBJECT CLASS WebExForm ARGS "Consulta CEP"
            .:SetMethod("get")
            .:SetAction("javascript:buscarCEP()")
            .:AddField("CEP","cep","text","Digite o CEP")
        END WEBEXOBJECT
        WITH WEBEXOBJECT CLASS WebExControl TYPE script
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
                                <strong>Logradouro:</strong> ${data.logradouro}<br>
                                <strong>Bairro:</strong> ${data.bairro}<br>
                                <strong>Cidade:</strong> ${data.localidade} - ${data.uf}<br>
                                <strong>CEP:</strong> ${data.cep}
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
            .:SetAttr("id","resultadoCEP")
            .:SetAttr("class","mt-4")
        END WEBEXOBJECT
        cHTML:=oFWWebExPage:Render()
    END WEBEXOBJECT

    FreeObj(@oFWWebExPage)

    cHTML:=EncodeUTF8(cHTML)
    if (!lIsDir("\web\tmp\"))
        FWMakeDir("\web\tmp\",.F.)
    endif
    cHTMLFile:="\web\tmp\"+Lower(cProcName)+".html"
    MemoWrite(cHTMLFile,cHTML)

    htmlFileShow(cHTML,cProcName,cHTMLFile)

    fErase(cHTMLFile)

return
````
![WebExForm](https://github.com/user-attachments/assets/fcf7609f-a2be-43b4-b63e-af5aa2718d58)

---

## 🧩 Dependências

* Nenhuma no backend (ADVPL puro)
* Frontend usa:

  * [Bootstrap 5.3](https://getbootstrap.com)
  * (opcional) [PO UI CSS](https://po-ui.io)

---

## 📦 Como usar

1. Clone o repositório
2. Compile
3. Use

---

## 🤝 Quer contribuir?

Toda ajuda é bem-vinda! A ideia aqui é **evoluir juntos** como comunidade Protheus:

* Criar novos componentes (`fw.webex.form`, `fw.webex.chart`, etc.)
* Melhorar o renderizador
* Adicionar eventos dinâmicos
* Documentar com mais exemplos

---

## ✨ Visão

> Acreditamos que dá pra evoluir mantendo o que o Protheus tem de melhor: a produtividade.
> FW\.WebEX é o passo que faltava pra quem quer ir pro web **sem perder a alma ADVPL**.

---

## 📄 Licença

[MIT](LICENSE)

---
