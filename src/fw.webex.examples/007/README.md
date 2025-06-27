# 💡 Exemplo de uso (7)

```advpl
#include "fw.webex.th"

#include "shell.ch"
#include "totvs.ch"
#include "tbiconn.ch"

#include "tlpp-core.th"
#include "tlpp-rest.th"

using namespace FWWebEx

procedure u_FWWebExExample_007()

    local lMainWnd as logical

    private lRedefineBottom as logical

    lMainWnd:=(Type("oMainWnd")=="O")
    if (!lMainWnd)
        PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"
            private oMainWnd as object
            lRedefineBottom:=.T.
            DEFINE WINDOW oMainWnd FROM 00,00 TO 1024,768 TITLE ProcName()
            ACTIVATE WINDOW oMainWnd MAXIMIZED ON INIT (FWWebExExample_007(),oMainWnd:End())
            FreeObj(@oMainWnd)
        RESET ENVIRONMENT
    else
        lRedefineBottom:=.F.
        FWWebExExample_007()
    endif

return

static procedure FWWebExExample_007()

    local aParamBox:=Array(0) as array
    local aParamRet:=Array(0) as array

    local cHTML as character
    local cHTMLFile as character

    local cScript as character
    local cProcName:=ProcName() as character
    local cBasicAuth as character
    local cDNATechAuth as character

    local oPage as object
    local oScript as object
    local oDivTable as object
    local oTableStyle as object

    aAdd(aParamBox,{1,"Usuario",Space(100),"@","NaoVazio()","","AllWaysTrue()",100,.T.})
    aAdd(aParamBox,{1,"Senha",Space(100),"@","NaoVazio()","","AllWaysTrue()",100,.T.})
    aAdd(aParamBox,{1,"URL REST",Space(200),"@","NaoVazio()","","AllWaysTrue()",200,.T.})
    if (!ParamBox(@aParamBox,"Selecione os Parametros",@aParamRet,nil,nil,.T.,nil,nil,nil,nil,.T.,.T.))
        return
    endif

    aParamRet[1]:=AllTrim(aParamRet[1])
    aParamRet[2]:=AllTrim(aParamRet[2])
    aParamRet[3]:=AllTrim(aParamRet[3])
    if (Right(aParamRet[3],1)!="/")
        aParamRet[3]+="/"
    endif

    cBasicAuth:="Basic "+Encode64(aParamRet[1]+":"+aParamRet[1])

    oPage:=WebExPage():New("Exemplo 007 - Funcionarios (REST + DataTable)")
    oTableStyle:=WebExControl():New("style")

    beginContent var cTableStyle
        table.dataTable.compact tbody td {
            padding: 4px 8px !important;
        }
        #custom-loader {
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        height: 4px !important;
        background: linear-gradient(270deg, #0dcaf0, #0d6efd) !important;
        animation: progressbar-stripes 1s linear infinite !important;
        }
        @keyframes progressbar-stripes {
        0% { background-position: 1rem 0; }
        100% { background-position: 0 0; }
        }
    endContent
    oTableStyle:SetContent(cTableStyle)
    oPage:AddChild(oTableStyle)

    oScript:=WebExControl():New("script")

    // Adiciona container de tabela
    oDivTable:=WebExControl():New("div")
    oDivTable:SetAttr("id","tableResult")
    oPage:AddChild(oDivTable)

    /*
        Tabela do DOM (so pra referencia)
        https://datatables.net/reference/option/dom
        | Letra | Elemento que aparece           |
        | ----- | ------------------------------ |
        | **B** | Botoes (exportacao etc.)       |
        | **l** | Seletor de "linhas por pagina" |
        | **f** | Campo de busca (filtro)        |
        | **r** | Texto "processing..."          |
        | **t** | Tabela                         |
        | **i** | Info de "Mostrando x a y de z" |
        | **p** | Paginacao                      |
    */
    // Script com server-side pagination ativado
    beginContent var cScript
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('tableResult').innerHTML = `
                <div id="custom-loader" style="display:none; width: 100%;">
                    <div class="progress">
                        <div class="progress-bar progress-bar-striped progress-bar-animated bg-primary" style="width: 100%">
                            Carregando...
                        </div>
                    </div>
                </div>
                <table id="example" class="table table-striped table-hover display compact nowrap">
                    <thead>
                        <tr>
                            <th>Filial</th>
                            <th>Matr&iacute;cula</th>
                            <th>Apelido</th>
                            <th>Centro de Custo</th>
                            <th>Sal&aacute;rio</th>
                            <th>Adt.Servi&ccedil;o</th>
                            <th>Cat.Func.</th>
                            <th>Sexo</th>
                        </tr>
                    </thead>
                </table>`;
            const table = new DataTable('#example', {
                serverSide: true,
                processing: false,
                dom: 'Blfrtip',
                lengthMenu: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,25,30,35,40,45,50,100,-1],
                pageLength: 13,//DEFAULT
                buttons: [
                    'copy',
                    'csv',
                    'print',
                    {
                        extend: 'excelHtml5',
                        title: 'u_FWWebExExample_007',
                        filename: 'relatorio_excel',
                        autoFilter: true
                    },
                    {
                        extend: 'pdf',
                        title: 'u_FWWebExExample_007',
                        filename: 'relatorio_pdf'
                    }
                ],
                responsive: true,
                className: 'compact',
                language: {
                    url: 'https://cdn.datatables.net/plug-ins/2.3.2/i18n/pt-BR.json',
                    lengthLabels: {
                        '-1': 'Todos' //https://datatables.net/reference/option/lengthMenu
                    }
                },
                "preDrawCallback": function(settings) {
                    $('#custom-loader').show();
                },
                "drawCallback": function(settings) {
                    $('#custom-loader').hide();
                    // This drawCallback ensures consistent table height across pages.
                    // It calculates how many empty rows are needed to fill the remaining space,
                    // and appends them to the table so all pages have the same visual height.
                    const api = this.api();
                    const rows = api.rows({ page: 'current' }).count();
                    const pageSize = api.page.len();
                    const emptyRows = pageSize - rows;
                    for (let i = 0; i < emptyRows; i++) {
                        $('#example tbody').append('<tr class="empty-row"><td colspan="999">&nbsp;</td></tr>');
                    }
                },
                ajax: function (data, callback) {
                    const pageNumber = Math.floor(data.start / data.length) + 1;
                    const rowsPerPage = data.length === -1 ? 999999 : data.length;
                    //const basicAuth = 'Basic ' + btoa('admin:admin');
                    fetch('http://localhost:9898/rest/callProcRestCrudTLPP/post/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Authorization': basicAuth,
                            'X-DNATech-Auth-Token': 'DNATechAuth'
                        },
                        body: JSON.stringify({
                            ClassName: 'userRestCrudTLPPCoreFunction',
                            FunctionName: 'dna.tech.codAliasPost',
                            codAlias: 'SRA',
                            yesFields: 'RA_FILIAL,RA_MAT,RA_APELIDO,RA_CC,RA_SALARIO,RA_ADTPOSE,RA_CATFUNC,RA_DEPIR,RA_SEXO',
                            Filter: {
                                RA_SEXO: 'M'
                            },
                            PageNumber: pageNumber,
                            RowspPage: rowsPerPage,
                            cEmp: '99',
                            cFil: '01',
                            lChkPrepEnv: false,
                            lHTTPCTLen: true,
                            lFWHTTpEncode: true,
                            cHTTPCTType: 'application/json; charset=UTF-8',
                            lHTTPCTType: true
                        })
                    })
                    .then(res => {
                        if (!res.ok) throw new Error('HTTP ' + res.status);
                        return res.text();
                    })
                    .then(text => {
                        console.log('RAW response:', text);
                        const json = JSON.parse(text);
                        if (!json.table || !json.table.items) throw new Error('JSON incompleto');
                        const rows = json.table.items.map(row => {
                            const i = row.detail.items;
                            return [
                                        i.RA_FILIAL || '',
                                        i.RA_MAT || '',
                                        i.RA_APELIDO || '',
                                        i.RA_CC || '',
                                        i.RA_SALARIO || '',
                                        i.RA_ADTPOSE || '',
                                        i.RA_CATFUNC || '',
                                        i.RA_DEPIR || '',
                                        i.RA_SEXO || ''
                                    ];
                        });
                        callback({
                            data: rows,
                            recordsTotal: json.TotalRows,
                            recordsFiltered: json.TotalRows
                        });
                    })
                    .catch(err => console.error('Erro ao carregar dados:', err));
                }
            });
             //captura do evento de processamento
            table.on('processing.dt', function (e, settings, processing) {
                if (processing) {
                    $('#custom-loader').show();
                } else {
                    $('#custom-loader').hide();
                }
            });
        });
    endContent

    if (!FindClass("DNA.TECH.USERRESTCRUDTLPP"))
        //Considerando que callProcRestCrudTLPP depende de DNA.TECH.USERRESTCRUDTLPP
        //u_callProcRestCrudTLPP atuara como um mock da callProcRestCrudTLPP.
        cScript:=StrTran(cScript,"callProcRestCrudTLPP","u_callProcRestCrudTLPP")
    else
        cDNATechAuth:=MemoRead("\dna.tech\authentication\authentication.aut")
        cDNATechAuth:=Encode64("token:"+cDNATechAuth)
        cScript:=StrTran(cScript,"DNATechAuth",cDNATechAuth)
    endif
    cScript:=StrTran(cScript,"basicAuth","'"+cBasicAuth+"'")
    cScript:=StrTran(cScript,"http://localhost:9898/rest/",aParamRet[3])

    oScript:SetContent(cScript)
    oPage:AddChild(oScript)
    *oPage:SetAttr("style","min-height:100vh;padding:1rem;box-sizing:border-box;overflow:auto;")

    cHTML:=oPage:Render()

    FreeObj(@oPage)
    FreeObj(@oScript)
    FreeObj(@oDivTable)
    FreeObj(@oTableStyle)

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

![image](https://github.com/user-attachments/assets/929a5909-5b08-4582-a06e-d98c2ad5aec7)

---

https://github.com/user-attachments/assets/6a432b89-e127-4936-a3cc-463f79c9d9c8
