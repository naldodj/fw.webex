# 💡 Exemplo de uso (12)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_012()
    local bExecute as codeblock
    local cHTML as character
    local cHTMLFile as character
    local cProcName:=ProcName() as character
    bExecute:={||FWMsgRun(nil,{||cHTMLFile:=FWWebExExample_012(@cHTML)},"Aguarde",cProcName)}
    FWExampleTools():Execute(bExecute,cProcName,.T.)
    if (File(cHTMLFile))
        FWExampleTools():htmlFileShow(cHTML,cProcName,cHTMLFile)
        fErase(cHTMLFile)
    endif
return

static procedure FWWebExExample_012(cHTML as character) as character

    local cScript as character
    local cProcName:=ProcName() as character
    local cHTMLFile:=cProcName as character

    local oFWoSideBar as object
    local oFWWebExMain as object
    local oFWWebExIcon as object
    local oFWWebExShell as object
    local oFWWebExScript as object
    local oFWWebExCardKPI as object
    local oFWWebExContainer as object
    local oFWWebExNavSideMenu as object

    local oFWWebExRow1 as object
    local oFWWebExRow2 as object

    local oFWWebExCol1 as object
    local oFWWebExCol2 as object
    local oFWWebExCol3 as object
    local oFWWebExCol4 as object

    // Monta menu lateral
    oFWWebExNavSideMenu:=WebExNavSide():New()
    oFWWebExNavSideMenu:SetBrand("FWWebEx")
    oFWWebExNavSideMenu:AddHeader("Geral")
    oFWWebExNavSideMenu:AddItem("Dashboard KPI","#kpi",WebExIcon():New("bi-bar-chart")):SetAttr("data-toggle-kpi","kpi")
    oFWWebExNavSideMenu:AddDivider()
    oFWWebExNavSideMenu:AddItem("Dashboard KPI 2","#kpi2",WebExIcon():New("bi-bar-chart")):SetAttr("data-toggle-kpi","kpi2")
    oFWWebExNavSideMenu:AddDivider()
    oFWWebExNavSideMenu:AddHeader("Admin")
    oFWWebExNavSideMenu:AddItem("Usu&aacute;rios","#",WebExIcon():New("bi-person"))

    oFWoSideBar:=WebExSideBar():New()
    oFWoSideBar:AddChild(oFWWebExNavSideMenu)

    // Cards KPI dentro do Container e Main
    oFWWebExCol1:=WebExCol():New(4)
    oFWWebExCardKPI:=WebExCardKPI():New("Faturamento","R$ 125.000","bg-success",WebExIcon():New("bi-bar-chart"))
    oFWWebExCol1:AddChild(oFWWebExCardKPI)

    oFWWebExCol2:=WebExCol():New(4)
    oFWWebExCol2:AddClass("border-start")
    oFWWebExCol2:AddClass("border-secondary")
    oFWWebExCol2:AddClass("ps-3")
    oFWWebExCardKPI:=WebExCardKPI():New("Despesas","R$ 87.000","bg-danger",WebExIcon():New("bi-graph-up"))
    oFWWebExCol2:AddChild(oFWWebExCardKPI)

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
    oFWWebExIcon:=WebExIcon():New("analytics","material")
    oFWWebExCardKPI:=WebExCardKPI():New("Clientes Ativos","1.024","bg-info",oFWWebExIcon)
    oFWWebExCardKPI:SetIconBefore(.F.)
    oFWWebExCol3:AddChild(oFWWebExCardKPI)

    oFWWebExCol4:=WebExCol():New(6)
    oFWWebExIcon:=WebExIcon():New("insights","material")
    oFWWebExCardKPI:=WebExCardKPI():New("Ticket M&eacute;dio","R$ 122,00","bg-warning",oFWWebExIcon)
    oFWWebExCardKPI:SetIconBefore(.F.)
    oFWWebExCol4:AddChild(oFWWebExCardKPI)

    oFWWebExRow2:=WebExRow():New()
    oFWWebExRow2:AddChild(oFWWebExCol3)
    oFWWebExRow2:AddChild(oFWWebExCol4)

    oFWWebExContainer:=WebExContainer():New()
    oFWWebExContainer:SetAttr("id","kpi")
    oFWWebExContainer:SetAttr("style","display:none")
    oFWWebExContainer:AddChild(oFWWebExRow1)
    oFWWebExContainer:AddChild(WebExHR():New())
    oFWWebExContainer:AddChild(oFWWebExRow2)

    oFWWebExMain:=WebExMain():New()
    oFWWebExMain:AddChild(oFWWebExContainer)
    oFWWebExMain:AddChild(WebExHR():New())
    oFWWebExMain:AddChild(BuildKPI2Content())

    oFWWebExShell:=WebExShell():New(cProcName)
    oFWWebExShell:AddChild(oFWoSideBar)
    oFWWebExShell:AddChild(oFWWebExMain)

    // Script para alternar exibicao dos KPIs
    beginContent var cScript
        document.addEventListener("DOMContentLoaded",()=>{
            document.querySelectorAll("[data-toggle-kpi]").forEach(el=>{
                el.addEventListener("click",()=>{
                ["kpi","kpi2"].forEach(id=>{
                    document.getElementById(id).style.display = (id === el.dataset.toggleKpi) ? "block" : "none";
                    });
                });
            });
        });
    endContent

    oFWWebExScript:=WebExScript():New()
    oFWWebExScript:SetContent(cScript)

    WebFileTools():HTMLFromControl(oFWWebExShell,"\web\tmp\",@cHTMLFile,@cHTML,.T.)

    oFWWebExShell:Clean()

    FreeObj(@oFWoSideBar)
    FreeObj(@oFWWebExMain)
    FreeObj(@oFWWebExIcon)
    FreeObj(@oFWWebExShell)
    FreeObj(@oFWWebExScript)
    FreeObj(@oFWWebExCardKPI)
    FreeObj(@oFWWebExContainer)
    FreeObj(@oFWWebExNavSideMenu)

    FreeObj(@oFWWebExRow1)
    FreeObj(@oFWWebExRow2)

    FreeObj(@oFWWebExCol1)
    FreeObj(@oFWWebExCol2)
    FreeObj(@oFWWebExCol3)
    FreeObj(@oFWWebExCol4)

return(cHTMLFile)
````
