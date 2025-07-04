# 💡 Exemplo de uso (1)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_001()
    local bExecute as codeblock
    local cHTMLFile as character
    local cProcName:=ProcName() as character
    bExecute:={||FWMsgRun(nil,{||cHTMLFile:=FWWebExExample_001()},"Aguarde",cProcName)}
    FWExampleTools():Execute(bExecute,cProcName,.T.)
    if (File(cHTMLFile))
        ShellExecute("open",cHTMLFile,"","",1)
    endif
return

static function FWWebExExample_001() as character

    local cHTML as character
    local cProcName:=ProcName() as character
    local cHTMLFile:=cProcName as character

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

    WebFileTools():HTMLFromControl(oFWWebExPage,GetTempPath(),@cHTMLFile,@cHTML,.T.)

    WEBEXOBJECT CLEAN

return(cHTMLFile)
````

![image](https://github.com/user-attachments/assets/9c9b7e12-0cb1-45a0-aca6-c53704bd0e67)

---

![image](https://github.com/user-attachments/assets/a897b5f4-2977-4c98-9701-7019bc278b89)
