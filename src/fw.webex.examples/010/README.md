# 💡 Exemplo de uso (10)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_010()
    FWExampleTools():Execute({||FWWebExExample_010()},ProcName(),.F.)
return

static procedure FWWebExExample_010()

    local cHTML as character
    local cHTMLFile as character

    local cProcName:=ProcName() as character

    local oFWWebExPage as object

    local oFWWebExRow1 as object
    local oFWWebExRow2 as object

    local oFWWebExCol1 as object
    local oFWWebExCol2 as object
    local oFWWebExCol3 as object
    local oFWWebExCol4 as object

    local oFWWebExCardKPI as object

    // KPI 1
    oFWWebExCol1:=WebExCol():New(4)
    oFWWebExCardKPI:=WebExCardKPI():New("Faturamento","R$ 125.000","bg-success",WebExIcon():New("bi-bar-chart"))
    oFWWebExCol1:AddChild(oFWWebExCardKPI)

    // KPI 2
    oFWWebExCol2:=WebExCol():New(4)
    oFWWebExCol2:AddClass("border-start")
    oFWWebExCol2:AddClass("border-secondary")
    oFWWebExCol2:AddClass("ps-3")
    oFWWebExCardKPI:=WebExCardKPI():New("Despesas","R$ 87.000","bg-danger",WebExIcon():New("bi-graph-up"))
    oFWWebExCol2:AddChild(oFWWebExCardKPI)

    // KPI 3
    oFWWebExCol3:=WebExCol():New(4)
    oFWWebExCol3:AddClass("border-start")
    oFWWebExCol3:AddClass("border-secondary")
    oFWWebExCol3:AddClass("ps-3")
    oFWWebExCardKPI:=WebExCardKPI():New("Outros","R$ 75.000","bg-info",WebExIcon():New("bi-currency-dollar"))
    oFWWebExCol3:AddChild(oFWWebExCardKPI)

    oFWWebExRow1:=WebExRow():New()
    oFWWebExRow1:AddChild(oFWWebExCol1)
    oFWWebExRow1:AddChild(oFWWebExCol2)
    oFWWebExRow1:AddChild(oFWWebExCol3)

    oFWWebExCol3:=WebExCol():New(6)
    oFWWebExCardKPI:=WebExCardKPI():New("Clientes Ativos","1.024","bg-info",WebExIcon():New("analytics","material"))
    oFWWebExCardKPI:SetIconBefore(.F.)
    oFWWebExCol3:AddChild(oFWWebExCardKPI)

    oFWWebExCol4:=WebExCol():New(6)
    oFWWebExCardKPI:=WebExCardKPI():New("Ticket M&eacute;dio","R$ 122,00","bg-warning",WebExIcon():New("insights","material"))
    oFWWebExCardKPI:SetIconBefore(.F.)
    oFWWebExCol4:AddChild(oFWWebExCardKPI)

    // Segunda linha com KPI
    oFWWebExRow2:=WebExRow():New()
    oFWWebExRow2:AddChild(oFWWebExCol3)
    oFWWebExRow2:AddChild(oFWWebExCol4)

    oFWWebExPage:=WebExPage():New("KPI Dashboard")
    oFWWebExPage:AddChild(oFWWebExRow1)
    oFWWebExPage:AddChild(WebExHR():New()) // separador horizontal
    oFWWebExPage:AddChild(oFWWebExRow2)

    cHTML:=oFWWebExPage:RenderHTML()
    oFWWebExPage:Clean()

    FreeObj(@oFWWebExCardKPI)
    FreeObj(@oFWWebExRow1)
    FreeObj(@oFWWebExRow2)
    FreeObj(@oFWWebExCol1)
    FreeObj(@oFWWebExCol2)
    FreeObj(@oFWWebExCol3)
    FreeObj(@oFWWebExCol4)
    FreeObj(@oFWWebExPage)

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

![image](https://github.com/user-attachments/assets/16d7dd2e-7077-4f80-872b-b4c8cfa5ccf2)
