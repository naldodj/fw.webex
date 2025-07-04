# 💡 Exemplo de uso (4)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_004()
    local bExecute as codeblock
    local cHTML as character
    local cHTMLFile as character
    local cProcName:=ProcName() as character
    bExecute:={||FWMsgRun(nil,{||cHTMLFile:=FWWebExExample_004(@cHTML)},"Aguarde",cProcName)}
    FWExampleTools():Execute(bExecute,cProcName,.T.)
    if (File(cHTMLFile))
        FWExampleTools():htmlFileShow(cHTML,cProcName,cHTMLFile)
        fErase(cHTMLFile)
    endif
return

static function FWWebExExample_004(cHTML as character) as character

    local cProcName:=ProcName() as character
    local cHTMLFile:=cProcName as character

    local oFWWebExPage as object

    WITH WEBEXOBJECT oFWWebExPage CLASS WebExPage ARGS cProcName
        // ALERTA DE ERRO
        WITH WEBEXOBJECT CLASS WebExAlert ARGS "Erro ao carregar os dados do cliente.","danger"
        END WEBEXOBJECT
        // SEPARADOR HORIZONTAL
        WITH WEBEXOBJECT CLASS WebExHR
        END WEBEXOBJECT
        // ALERTA DE SUCESSO
        WITH WEBEXOBJECT CLASS WebExAlert ARGS "Opera&ccedil;&atilde;o realizada com sucesso!","success"
        END WEBEXOBJECT
        // SEPARADOR HORIZONTAL
        WITH WEBEXOBJECT CLASS WebExHR
        END WEBEXOBJECT
        // CARD COM TEXTO ENCORPADO
        WITH WEBEXOBJECT CLASS WebExCard ARGS "Cliente Encontrado",""
            WITH WEBEXOBJECT CLASS WebExControl TYPE p
                .:AddClass("card-text teste")
                .:AddClass("teste")
                .:RemoveClass("teste")
                WITH WEBEXOBJECT CLASS WebExStrong ARGS "&nbsp;&nbsp;&nbsp;Nome:"
                END WEBEXOBJECT
                WITH WEBEXOBJECT CLASS WebExControl TYPE span
                    .:SetContent("&nbsp;Jo&atilde;o da Silva")
                END WEBEXOBJECT
            END WEBEXOBJECT
            WITH WEBEXOBJECT CLASS WebExControl TYPE p
                .:SetAttr("class","card-text")
                WITH WEBEXOBJECT CLASS WebExStrong ARGS "&nbsp;&nbsp;&nbsp;Cidade:"
                END WEBEXOBJECT
                WITH WEBEXOBJECT CLASS WebExControl TYPE span
                    .:SetContent("&nbsp;Vit&oacute;ria - ES")
                END WEBEXOBJECT
            END WEBEXOBJECT
        END WEBEXOBJECT
        // SEPARADOR HORIZONTAL
        WITH WEBEXOBJECT CLASS WebExHR
        END WEBEXOBJECT
        // CARD COM BODY
        WITH WEBEXOBJECT CLASS WebExCard ARGS "TITLE","BODY"
        END WEBEXOBJECT
        // SEPARADOR HORIZONTAL
        WITH WEBEXOBJECT CLASS WebExHR
        END WEBEXOBJECT
        // CARD KPI
        WITH WEBEXOBJECT CLASS WebExCardKPI ARGS "Turnover Geral","12,5%","bg-danger",WebExIcon():New("bi-bar-chart")
        END WEBEXOBJECT
        // SEPARADOR HORIZONTAL
        WITH WEBEXOBJECT CLASS WebExHR
        END WEBEXOBJECT
    END WEBEXOBJECT

    WebFileTools():HTMLFromControl(oFWWebExPage,"\web\tmp\",@cHTMLFile,@cHTML,.T.)

    WEBEXOBJECT CLEAN

return(cHTMLFile)
````

![image](https://github.com/user-attachments/assets/3de7731a-e9a4-4e3c-8854-c736c7460590)

---

![image](https://github.com/user-attachments/assets/f469ee0e-ff18-4eb5-b204-722887df0fde)
