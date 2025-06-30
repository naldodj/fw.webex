# 💡 Exemplo de uso (4)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_004()
    FWExampleTools():Execute({||FWWebExExample_004()},ProcName(),.F.)
return

static procedure FWWebExExample_004()

    local cHTML as character
    local cHTMLFile as character

    local cProcName:=ProcName() as character

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
        cHTML:=oFWWebExPage:RenderHTML()
    END WEBEXOBJECT

    WEBEXOBJECT CLEAN

    cHTML:=EncodeUTF8(cHTML)
    if (!lIsDir("\web\tmp\"))
        FWMakeDir("\web\tmp\",.F.)
    endif
    cHTMLFile:="\web\tmp\"+Lower(cProcName)+".html"
    MemoWrite(cHTMLFile,cHTML)

    FWExampleTools():htmlFileShow(cHTML,cProcName,cHTMLFile)

    fErase(cHTMLFile)

return
````

![image](https://github.com/user-attachments/assets/3de7731a-e9a4-4e3c-8854-c736c7460590)

---

![image](https://github.com/user-attachments/assets/f469ee0e-ff18-4eb5-b204-722887df0fde)
