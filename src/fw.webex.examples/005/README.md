# 💡 Exemplo de uso (5)

```advpl
#include "fw.webex.th"

#include "shell.ch"
#include "totvs.ch"

using namespace FWWebEx

procedure u_FWWebExExample_005()

    local lMainWnd:=(Type("oMainWnd")=="O") as logical

    private lRedefineBottom as logical

    if (!lMainWnd)
        private oMainWnd as object
        lRedefineBottom:=.T.
        DEFINE WINDOW oMainWnd FROM 00,00 TO 1024,768 TITLE ProcName()
        ACTIVATE WINDOW oMainWnd MAXIMIZED ON INIT (FWWebExExample_005(),oMainWnd:End())
        FreeObj(@oMainWnd)
    else
        lRedefineBottom:=.F.
        FWWebExExample_005()
    endif

return

static procedure FWWebExExample_005()

    local cHTML as character
    local cHTMLFile as character

    local cScript as character
    local cProcName:=ProcName() as character

    local oDiv as object
    local oButton as object

    local oPage:=WebExPage():New("Exemplo 005 - Formul&aacute;rio ViaCEP") as object
    local oForm:=WebExForm():New("Consulta de CEP") as object
    local oScript:=WebExControl():New("script") as object

    oForm:SetMethod("get")
    oForm:SetAction("#")

    // Campo de busca
    oForm:AddField("CEP","cep","text","Digite o CEP")

    // Campos que serao atualizados via Ajax (ja definidos)
    oForm:AddField("Logradouro","logradouro","text","")
    oForm:AddField("Bairro","bairro","text","")
    oForm:AddField("Cidade","localidade","text","")
    oForm:AddField("UF","uf","text","")
    oForm:AddField("C&oacute;digo IBGE","ibge","text","")

    oDiv:=WebExControl():New("div")
    oDiv:SetAttr("id","resultadoCEP")

    oButton:=WebExButton():New("Buscar")
    oButton:SetAttr("onclick","buscarCEP(); return false;")

    oForm:AddChild(oDiv)
    oForm:AddChild(oButton)

    oPage:AddChild(oForm)

    // Adiciona o script para consulta Ajax do ViaCEP
    beginContent var cScript
        function buscarCEP() {
            const cep = document.getElementsByName('cep')[0].value.replace(/[^0-9]/g,'');
            if (cep.length !== 8) {
                document.getElementById('resultadoCEP').innerHTML = '<div class=\"alert alert-danger\">CEP inv&aacute;lido.</div>';
                return;
            }
            fetch('https://viacep.com.br/ws/' + cep + '/json/')
                .then(response => response.json())
                .then(data => {
                if (data.erro) {
                    document.getElementById('resultadoCEP').innerHTML = '<div class=\"alert alert-danger\">CEP n&atilde;o encontrado.</div>';
                } else {
                    document.getElementsByName('logradouro')[0].value = data.logradouro || '';
                    document.getElementsByName('bairro')[0].value = data.bairro || '';
                    document.getElementsByName('localidade')[0].value = data.localidade || '';
                    document.getElementsByName('uf')[0].value = data.uf || '';
                    document.getElementsByName('ibge')[0].value = data.ibge || '';
                    document.getElementById('resultadoCEP').innerHTML = '';
                }
            }).catch(() => {
                document.getElementById('resultadoCEP').innerHTML = '<div class=\"alert alert-danger\">Erro ao consultar o CEP.</div>';
            });
        }
    endContent

    oScript:SetContent(cScript)

    oPage:AddChild(oScript)
    cHTML:=oPage:Render()

    FreeObj(@oDiv)
    FreeObj(@oPage)
    FreeObj(@oForm)
    FreeObj(@oScript)
    FreeObj(@oButton)

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

![image](https://github.com/user-attachments/assets/1e2db3f4-343c-4230-a5b4-43d6bd4ff475)

---

![image](https://github.com/user-attachments/assets/8d083612-2a35-44a0-a8f7-1e0616ba8abc)
