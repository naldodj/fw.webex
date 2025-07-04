# 💡 Exemplo de uso (2)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_002()
    local bExecute as codeblock
    local cHTML as character
    local cHTMLFile as character
    local cProcName:=ProcName() as character
    bExecute:={||FWMsgRun(nil,{||cHTMLFile:=FWWebExExample_002(@cHTML)},"Aguarde",cProcName)}
    FWExampleTools():Execute(bExecute,cProcName,.T.)
    if (File(cHTMLFile))
        FWExampleTools():htmlFileShow(cHTML,cProcName,cHTMLFile)
        fErase(cHTMLFile)
    endif
return

static function FWWebExExample_002(cHTML as character) as character

    local cHTMLFile as character
    local cProcName:=ProcName() as character

    local oFWWebExPage as object

    WITH WEBEXOBJECT oFWWebExPage CLASS WebExPage ARGS cProcName
        WITH WEBEXOBJECT CLASS WebExTemplateBulkActionTable ARGS cProcName+" (Tabela 32)"
            .:FromSQL("SELECT * FROM SX5990 WHERE X5_TABELA='32' AND D_E_L_E_T_<>'*'")
        END WEBEXOBJECT
        WITH WEBEXOBJECT CLASS WebExHR
        END WEBEXOBJECT
        WITH WEBEXOBJECT CLASS WebExTemplateBulkActionTable ARGS cProcName+" (Tabela 35)"
            .:FromSQL("SELECT * FROM SX5990 WHERE X5_TABELA='35' AND D_E_L_E_T_<>'*'")
        END WEBEXOBJECT
    END WEBEXOBJECT

    cHTMLFile:=cProcName
    WebFileTools():HTMLFromControl(oFWWebExPage,"\web\tmp\",@cHTMLFile,@cHTML,.T.)

    WEBEXOBJECT CLEAN

return(cHTMLFile)
````

![image](https://github.com/user-attachments/assets/dba13e70-a014-42db-81e7-83e8a8307d20)

---

![image](https://github.com/user-attachments/assets/aab58c6f-74ae-439a-aa49-784fc2fb3326)
