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
    if (!Empty(cHTMLFile).and.File(cHTMLFile))
        FWExampleTools():htmlFileShow(cHTML,cProcName,cHTMLFile)
        fErase(cHTMLFile)
    endif
return

static procedure FWWebExExample_012(cHTML as character) as character

    local cScript as character
    local cProcName:=ProcName() as character
    local cHTMLFile:=cProcName as character

    local oH1 as object

    local oTopBar as object
    local oWrapper as object
    local oContentWrapper as object

    local oFWWebExBody as object
    local oFWWebExMain as object
    local oFWWebExIcon as object
    local oFWWebExPage as object
    local oFWWebExStyle as object
    local oFWWebExScript as object
    local oFWWebExNavSide as object
    local oFWWebExSideBar as object
    local oFWWebExCardKPI1 as object
    local oFWWebExCardKPI2 as object

    oH1:=WebExControl():New("h1")
    oH1:AddClass("h4")
    oH1:SetContent("Dashboard")

    oTopBar:=WebExControl():New("nav")
    oTopBar:AddClass("navbar shadow mb-3")
    oTopBar:AddChild(oH1)

    oFWWebExSideBar:=WebExSideBar():New()

    // Menu lateral com data-toggle-kpi
    oFWWebExNavSide:=WebExNavSide():New()
    oFWWebExNavSide:cType:="div"
    oFWWebExNavSide:SetAttr("id","webex-sidebar")
    oFWWebExNavSide:AddClass("collapse")
    oFWWebExNavSide:AddClass("show")
    oFWWebExNavSide:SetAttr("class","collapse show")
    oFWWebExNavSide:SetBrand("Side Menu")

    oFWWebExIcon:=WebExIcon():New("bi-bar-chart")
    oFWWebExNavSide:AddItem("Dashboard KPI","#",oFWWebExIcon):SetAttr("data-toggle-kpi","kpi")

    oFWWebExIcon:=WebExIcon():New("bi-graph-up")
    oFWWebExNavSide:AddItem("Dashboard KPI 2","#",oFWWebExIcon):SetAttr("data-toggle-kpi","kpi2")

    oFWWebExNavTop:=WebExNavTop():New("FWWebEx")
    oFWWebExSideBar:AddChild(oFWWebExNavTop)
    oFWWebExSideBar:AddChild(oFWWebExNavSide)

    // KPI 1
    oFWWebExCardKPI1:=WebExContainer():New(.T.)
    oFWWebExCardKPI1:SetAttr("id","kpi")
    oFWWebExCardKPI1:SetAttr("style","display:none")
    oFWWebExCardKPI1:AddChild(WebExCardKPI():New("Faturamento","$10.000","bg-primary",WebExIcon():New("bi-cash")))
    oFWWebExCardKPI1:AddChild(WebExCardKPI():New("Clientes Ativos","152","bg-success",WebExIcon():New("bi-people")))

    // KPI 2
    oFWWebExCardKPI2:=BuildKPI2Content()

    oFWWebExMain:=WebExMain():New()
    oFWWebExMain:AddChild(oFWWebExCardKPI1)
    oFWWebExMain:AddChild(oFWWebExCardKPI2)

    oContentWrapper:=WebExControl():New("div")
    oContentWrapper:AddClass("d-flex flex-column w-100")
    oContentWrapper:AddChild(oTopBar)
    oContentWrapper:AddChild(oFWWebExMain)

    oWrapper:=WebExControl():New("div")
    oWrapper:AddClass("d-flex")
    oWrapper:AddChild(oFWWebExSideBar)     // menu lateral
    oWrapper:AddChild(oContentWrapper)     // conteudo principal

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
        document.addEventListener("DOMContentLoaded", ()=>{
            const sidebar = document.getElementById("webex-sidebar");
            const brand = document.querySelector(".navbar-brand");

            const observer = new MutationObserver(() => {
                if (!sidebar.classList.contains("show")) {
                    brand.classList.add("collapse-hide");
                } else {
                    brand.classList.remove("collapse-hide");
                }
            });

            observer.observe(sidebar, { attributes: true, attributeFilter: ["class"] });
        });
    endContent

    oFWWebExScript:=WebExScript():New()
    oFWWebExScript:SetContent(cScript)

    beginContent var cStyle
        #webex-sidebar {
            transition: all 0.3s ease;
            width: 250px;
            overflow: hidden;
        }
        .navbar-brand.collapse-hide {
            display: none !important;
        }
    endContent
    oFWWebExStyle:=WebExStyle():New()
    oFWWebExStyle:SetContent(cStyle)

    oFWWebExBody:=WebExBody():New()
    oFWWebExBody:AddChild(oWrapper)

    oFWWebExPage:=WebExPage():New(cProcName)
    oFWWebExPage:AddChild(oFWWebExBody)

    WebFileTools():HTMLFromControl(oFWWebExPage,"\web\fwwebex\tmp\",@cHTMLFile,@cHTML,.T.)

    oFWWebExPage:Clean()

    FreeObj(@oH1)

    FreeObj(@oTopBar)
    FreeObj(@oWrapper)
    FreeObj(@oContentWrapper)

    FreeObj(@oFWWebExBody)
    FreeObj(@oFWWebExMain)
    FreeObj(@oFWWebExIcon)
    FreeObj(@oFWWebExPage)
    FreeObj(@oFWWebExScript)
    FreeObj(@oFWWebExNavSide)
    FreeObj(@oFWWebExSideBar)
    FreeObj(@oFWWebExCardKPI1)
    FreeObj(@oFWWebExCardKPI2)

return(cHTMLFile)
````

![image](https://github.com/user-attachments/assets/19ee0a9c-22c2-4459-9160-9fa6b5ca2a86)

![image](https://github.com/user-attachments/assets/c5328742-ec6f-42c6-9fab-5621d3df154e)

![image](https://github.com/user-attachments/assets/0a3464a6-908c-4eac-86af-27d4065345d7)
