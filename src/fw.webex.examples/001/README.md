# 💡 Exemplo de uso (1)

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
