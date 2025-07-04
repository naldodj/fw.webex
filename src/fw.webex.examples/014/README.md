# 💡 Exemplo de uso (12)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_014()
    local bExecute as codeblock
    local cHTML as character
    local cHTMLFile as character
    local cProcName:=ProcName() as character
    bExecute:={||FWMsgRun(nil,{||cHTMLFile:=FWWebExExample_014(@cHTML)},"Aguarde",cProcName)}
    FWExampleTools():Execute(bExecute,cProcName,.T.)
    if (File(cHTMLFile))
        FWExampleTools():htmlFileShow(cHTML,cProcName,cHTMLFile)
        fErase(cHTMLFile)
    endif
return

// Dashboard básico com layout SBAdmin
static function FWWebExExample_014(cHTML as character) as character

    local cProcName:=ProcName() as character
    local cHTMLFile:=cProcName as character

    local oMain as object
    local oPage as object
    local oTopbar as object
    local oDivider as object
    local oWrapper as object
    local oSidebar as object

    local oContainer as object
    local oBrandLink as object
    local oBrandIcon as object
    local oBrandText as object

    local oMenuItem as object
    local oMenuLink as object
    local oMenuIcon as object
    local oMenuText as object

    local oContentWrapper as object

    oPage:=WebExPage():New("FWWebEx SBAdmin Clone")
    oWrapper:=WebExControl():New("div")
    oWrapper:AddClass("d-flex")
    oSidebar:=WebExControl():New("ul")
    oSidebar:AddClass("nav flex-column bg-primary text-white p-3")

    // Brand
    oBrandLink:=WebExControl():New("a")
    oBrandLink:AddClass("d-flex align-items-center justify-content-center mb-3 text-white fw-bold text-decoration-none")
    oBrandLink:SetAttr("href","#")

    oBrandIcon:=WebExControl():New("div")
    oBrandIcon:AddClass("sidebar-brand-icon")
    oBrandIcon:AddChild(WebExIcon():New("bi-bar-chart"))

    oBrandText:=WebExControl():New("div")
    oBrandText:AddClass("sidebar-brand-text mx-3")
    oBrandText:SetContent("FWWebEx")

    oBrandLink:AddChild(oBrandIcon)
    oBrandLink:AddChild(oBrandText)
    oSidebar:AddChild(oBrandLink)

    // Itens de menu
    oDivider:=WebExHR():New("hr")
    oDivider:AddClass("my-2") // Bem Bootstrap
    oSidebar:AddChild(oDivider)

    oMenuItem:=WebExControl():New("li")
    oMenuItem:AddClass("nav-item active")
    oMenuLink:=WebExControl():New("a")
    oMenuLink:AddClass("nav-link"):SetAttr("href","#")
    oMenuIcon:=WebExIcon():New("bi-speedometer2")
    oMenuText:=WebExControl():New("span")
    oMenuText:SetContent("Dashboard")
    oMenuLink:AddChild(oMenuIcon)
    oMenuLink:AddChild(oMenuText)
    oMenuItem:AddChild(oMenuLink)
    oSidebar:AddChild(oMenuItem)

    // Conteúdo principal
    oContentWrapper:=WebExControl():New("div")
    oContentWrapper:AddClass("d-flex flex-column w-100")
    oTopbar:=WebExControl():New("nav")
    oTopbar:AddClass("navbar shadow mb-3")

    oH1:=WebExControl():New("h1")
    oH1:AddClass("h4")
    oH1:SetContent("Dashboard")
    oTopbar:AddChild(oH1)

    oMain:=WebExMain():New()
    oContainer:=WebExContainer():New(.T.)

    // Cards
    oContainer:AddChild(WebExCardKPI():New("Earnings (Monthly)","$40,000","bg-primary",WebExIcon():New("bi-calendar")))
    oContainer:AddChild(WebExCardKPI():New("Earnings (Annual)","$215,000","bg-success",WebExIcon():New("bi-cash")))
    oContainer:AddChild(WebExCardKPI():New("Tasks","50%","bg-info",WebExIcon():New("bi-clipboard")))
    oContainer:AddChild(WebExCardKPI():New("Pending Requests","18","bg-warning",WebExIcon():New("bi-chat")))

    oMain:AddChild(oContainer)
    oContentWrapper:AddChild(oTopbar)
    oContentWrapper:AddChild(oMain)

    oWrapper:AddChild(oSidebar)
    oWrapper:AddChild(oContentWrapper)
    oPage:AddChild(oWrapper)

    WebFileTools():HTMLFromControl(oPage,"\web\tmp\",@cHTMLFile,@cHTML,.T.)

    oPage:Clean()

    FreeObj(@oMain)
    FreeObj(@oPage)
    FreeObj(@oTopbar)
    FreeObj(@oDivider)
    FreeObj(@oWrapper)
    FreeObj(@oSidebar)

    FreeObj(@oContainer)
    FreeObj(@oBrandLink)
    FreeObj(@oBrandIcon)
    FreeObj(@oBrandText)

    FreeObj(@oMenuItem)
    FreeObj(@oMenuLink)
    FreeObj(@oMenuIcon)
    FreeObj(@oMenuText)

    FreeObj(@oContentWrapper)

return(cHTMLFile)
````
