# 💡 Exemplo de uso (3)

```advpl
#include "fw.webex.th"

#include "shell.ch"
#include "totvs.ch"

using namespace FWWebEx

procedure u_FWWebExExample_003()

    local lMainWnd:=(Type("oMainWnd")=="O") as logical

    private lRedefineBottom as logical

    if (!lMainWnd)
        private oMainWnd as object
        lRedefineBottom:=.T.
        DEFINE WINDOW oMainWnd FROM 00,00 TO 1024,768 TITLE ProcName()
        ACTIVATE WINDOW oMainWnd MAXIMIZED ON INIT (FWWebExExample_003(),oMainWnd:End())
        FreeObj(@oMainWnd)
    else
        lRedefineBottom:=.F.
        FWWebExExample_003()
    endif

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
            .:AddButton(WebExButton():New("Buscar CEP"))
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
                                <strong>CEP:</strong> ${data.cep}<br>
                                <strong>Logradouro:</strong> ${data.logradouro} -
                                <strong>Complemento:</strong> ${data.complemento} -
                                <strong>Unidade:</strong> ${data.unidade}<br>
                                <strong>Bairro:</strong> ${data.bairro} -
                                <strong>Localidade:</strong> ${data.localidade}<br>
                                <strong>UF:</strong> ${data.uf} -
                                <strong>Estado:</strong> ${data.estado}<br>
                                <strong>Regi&atilde;o:</strong> ${data.regiao} -
                                <strong>IBGE:</strong> ${data.ibge}<br>
                                <strong>GIA:</strong> ${data.gia} -
                                <strong>DDD:</strong> ${data.ddd}<br>
                                <strong>SIAFI:</strong> ${data.siafi}<br>
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

    WEBEXOBJECT CLEAN

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

![image](https://github.com/user-attachments/assets/20f6358a-b92e-4a97-9b65-6c5621c744ee)
