# 💡 Exemplo de uso (6)

```advpl
#include "fw.webex.th"

#include "shell.ch"
#include "totvs.ch"

using namespace FWWebEx

procedure u_FWWebExExample_006()

    local lMainWnd:=(Type("oMainWnd")=="O") as logical

    private lRedefineBottom as logical

    if (!lMainWnd)
        private oMainWnd as object
        lRedefineBottom:=.T.
        DEFINE WINDOW oMainWnd FROM 00,00 TO 1024,768 TITLE ProcName()
        ACTIVATE WINDOW oMainWnd MAXIMIZED ON INIT (FWWebExExample_006(),oMainWnd:End())
        FreeObj(@oMainWnd)
    else
        lRedefineBottom:=.F.
        FWWebExExample_006()
    endif

return

static procedure FWWebExExample_006()

    local cHTML as character
    local cHTMLFile as character

    local cScript as character
    local cProcName:=ProcName() as character

    local oPage:=WebExPage():New("Exemplo 006 - ViaCEP em DataTable")
    local oForm:=WebExForm():New("Buscar CEP")
    local oButton:=WebExButton():New("Buscar")
    local oScript:=WebExControl():New("script")
    local oDivTable:=WebExControl():New("div")

    //Campo para a Pesquisa do CEP
    oForm:AddField("CEP","cep","text","Digite o CEP")

    oButton:SetAttr("onclick","buscarCEP(); return false;")
    oForm:AddChild(oButton)

    // Tabela que sera preenchida
    oPage:AddChild(oForm)

    oDivTable:SetAttr("id","tableResult")
    oPage:AddChild(oDivTable)

    // Script para requisitar ViaCEP e preencher a tabela com DataTables
    beginContent var cScript
        function buscarCEP() {
            const cep = document.getElementsByName('cep')[0].value.replace(/[^0-9]/g,'');
            if (cep.length !== 8) {
                document.getElementById('tableResult').innerHTML = '<div class=\"alert alert-danger\">CEP inv&aacute;lido.</div>';
                return;
            }
            fetch('https://viacep.com.br/ws/' + cep + '/json/')
                .then(response => response.json())
                .then(data => {
                if (data.erro) {
                    document.getElementById('tableResult').innerHTML = '<div class=\"alert alert-danger\">CEP n&atilde;o encontrado.</div>';
                } else {
                    let html = '<table id=\"example\" class=\"table table-striped table-hover mt-3\">';
                    html += '<thead><tr><th>Campo</th><th>Valor</th></tr></thead><tbody>';
                    for (let key in data) {
                        html += '<tr><td><strong>' + key + '</strong></td><td>' + data[key] + '</td></tr>';
                    }
                    html += '</tbody></table>';
                    document.getElementById('tableResult').innerHTML = html;
                    //Portuguese-Brasil translation
                    //https://datatables.net/plug-ins/i18n/Portuguese-Brasil.html
                    var table = new DataTable('#example', {
                        language: {
                            url: 'https://cdn.datatables.net/plug-ins/2.3.2/i18n/pt-BR.json',
                        },
                    });
                }
                })
                .catch(() => {
                document.getElementById('tableResult').innerHTML = '<div class=\"alert alert-danger\">Erro ao consultar o CEP.</div>';
            });
        }
    endContent

    oScript:SetContent(cScript)

    oPage:AddChild(oScript)

    cHTML:=oPage:Render()

    FreeObj(@oPage)
    FreeObj(@oForm)
    FreeObj(@oButton)
    FreeObj(@oScript)
    FreeObj(@oDivTable)

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

![image](https://github.com/user-attachments/assets/efacbddb-895b-40d6-9c39-18822cbfbf03)

