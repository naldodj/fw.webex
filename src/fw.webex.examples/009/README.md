# 💡 Exemplo de uso (9)

```advpl
#include "fw.webex.th"

#include "shell.ch"

using namespace FWWebEx

procedure u_FWWebExExample_009()

    local lMainWnd as logical

    private lRedefineBottom as logical

    lMainWnd:=(Type("oMainWnd")=="O")
    if (!lMainWnd)
        private oMainWnd as object
        lRedefineBottom:=.T.
        DEFINE WINDOW oMainWnd FROM 00,00 TO 1024,768 TITLE ProcName()
        ACTIVATE WINDOW oMainWnd MAXIMIZED ON INIT (FWWebExExample_009(),oMainWnd:End())
        FreeObj(@oMainWnd)
    else
        lRedefineBottom:=.F.
        FWWebExExample_009()
    endif

return

static procedure FWWebExExample_009()

    local aEmpresas:={;
         {;
            "99";
           ,"TOTVS";
          ,{;
                {;
                     "99-0001";
                    ,"DEPARTAMENTO 0001";
                    ,"50%";
                };
            };
        };
        ,{;
            "01";
           ,"DNATech";
          ,{;
                {;
                     "01-0001";
                    ,"DEPARTAMENTO 0001";
                    ,".5%";
                };
            };
        };
    } as array

    local cHTML as character
    local cHTMLFile as character
    local cHTMLDrillDown as character

    local cProcName:=ProcName() as character

    local nEmpresa as numeric
    local nEmpresas:=Len(aEmpresas) as numeric

    local oPage as object
    local oTable as object
    local oTableDrillDown as object

    oTable:=WebExTable():New("Turnover por Empresa")
    oTable:SeTitleBefore(.T.)
    oTable:EnableDrillDown()

    oTable:AddColumnHeader("C&oacute;digo")
    oTable:AddColumnHeader("Nome")
    oTable:BuildHeader()

    for nEmpresa:=1 to nEmpresas
        oTableDrillDown:=WebExTable():New()
        oTableDrillDown:SeTitleBefore(.T.)
        oTableDrillDown:AddColumnHeader("C&oacute;digo")
        oTableDrillDown:AddColumnHeader("Nome")
        oTableDrillDown:AddColumnHeader("% Turnover")
        aEval(aEmpresas[nEmpresa][3],{|aRowDrillDown|;
                 oTableDrillDown:SetTitle("Turnover Departamento ["+aRowDrillDown[1]+"]");
                ,oTableDrillDown:AddCell(aRowDrillDown[1]);
                ,oTableDrillDown:AddCell(aRowDrillDown[2]);
                ,oTableDrillDown:AddCell(aRowDrillDown[3]);
                ,oTableDrillDown:BuildBodyRow();
            };
        )
        cHTMLDrillDown:=oTableDrillDown:RenderHTML()
        cHTMLDrillDown:=WebExHelper():EscapeAll(cHTMLDrillDown)
        FreeObj(@oTableDrillDown)
        oTable:AddCell(aEmpresas[nEmpresa][1])
        oTable:AddCell(aEmpresas[nEmpresa][2])
        oTable:BuildBodyRow(cHTMLDrillDown)
    next nEmpresa

    oPage:=WebExPage():New("Drill-down Exemplo")
    oPage:AddChild(oTable)
    cHTML:=oPage:RenderHTML()

    FreeObj(@oTable)
    FreeObj(@oPage)

    FWFreeArray(@aEmpresas)

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

![image](https://github.com/user-attachments/assets/f984fc01-c4d7-4b9c-964f-f953720f3bb1)

---

![image](https://github.com/user-attachments/assets/1df36047-b1b7-422e-996c-e7cc8f9a1f45)
