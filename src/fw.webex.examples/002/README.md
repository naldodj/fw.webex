# 💡 Exemplo de uso (2)

```advpl
#include "fw.webex.th"

#include "shell.ch"
#include "tbiconn.ch"

using namespace FWWebEx

procedure u_FWWebExExample_002()

    local lMainWnd:=(Type("oMainWnd")=="O") as logical

    private lRedefineBottom as logical

    if (!lMainWnd)
        private oMainWnd as object
        lRedefineBottom:=.T.
        DEFINE WINDOW oMainWnd FROM 00,00 TO 1024,768 TITLE ProcName()
        ACTIVATE WINDOW oMainWnd MAXIMIZED ON INIT (FWWebExExample_002(),oMainWnd:End())
        FreeObj(@oMainWnd)
    else
        lRedefineBottom:=.F.
        FWWebExExample_002()
    endif

return

static procedure FWWebExExample_002()

    local cHTML as character
    local cHTMLFile as character
    local cProcName:=ProcName() as character

    local oFWWebExPage as object

    WITH WEBEXOBJECT oFWWebExPage CLASS WebExPage ARGS cProcName
        WITH WEBEXOBJECT CLASS WebExTemplateBulkActionTable ARGS cProcName
            .:FromSQL("SELECT TOP 10 * FROM SX5990")
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

    htmlFileShow(cHTML,cProcName,cHTMLFile)

    fErase(cHTMLFile)

return
````

![image](https://github.com/user-attachments/assets/dba13e70-a014-42db-81e7-83e8a8307d20)

---

![image](https://github.com/user-attachments/assets/aab58c6f-74ae-439a-aa49-784fc2fb3326)
