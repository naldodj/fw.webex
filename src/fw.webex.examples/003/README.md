# 💡 Exemplo de uso (3)

```advpl
#include "fw.webex.th"

using namespace FWWebEx

procedure u_FWWebExExample_003()
    local bExecute as codeblock
    local cHTML as character
    local cHTMLFile as character
    local cProcName:=ProcName() as character
    bExecute:={||FWMsgRun(nil,{||cHTMLFile:=FWWebExExample_003(@cHTML)},"Aguarde",cProcName)}
    FWExampleTools():Execute(bExecute,cProcName,.T.)
    if (!Empty(cHTMLFile).and.File(cHTMLFile))
        FWExampleTools():htmlFileShow(cHTML,cProcName,cHTMLFile)
        fErase(cHTMLFile)
    endif
return

static function FWWebExExample_003(cHTML as character) as character

    local cScript as character
    local cProcName:=ProcName() as character
    local cHTMLFile:=cProcName as character

    local oFWWebExPage as object

    WITH WEBEXOBJECT oFWWebExPage CLASS WebExPage ARGS cProcName
        WITH WEBEXOBJECT CLASS WebExBody
            WITH WEBEXOBJECT CLASS WebExForm ARGS "Consulta CEP"
                .:SetMethod("get")
                .:SetAction("javascript:buscarCEP()")
                .:AddField("CEP","cep","text","Digite o CEP")
                .:AddButton(WebExButton():New("Buscar CEP"))
            END WEBEXOBJECT
            WITH WEBEXOBJECT CLASS WebExScript
                beginContent var cScript

                    function buscarCEP() {

                    const cep = document.querySelector("input[name='cep']").value.trim();
                    const url = `https://viacep.com.br/ws/${cep}/json/`;

                    fetch(url)
                        .then(response => response.json())
                        .then(data => {
                        if (data.erro) {
                            document.getElementById("resultadoCEP").innerHTML = "<div class='alert alert-danger'>CEP n&atilde;o encontrado.</div>";
                        } else {
                            document.getElementById("resultadoCEP").innerHTML = `
                            <div class='card'>
                                <div class='card-body'>
                                <h5 class='card-title'>Endere&ccedil;o</h5>
                                <p class='card-text'>
                                    <strong>CEP:</strong> ${data.cep}<br>
                                    <strong>Logradouro:</strong> ${data.logradouro} -
                                    <strong>Complemento:</strong> ${data.complemento} -
                                    <strong>Unidade:</strong> ${data.unidade}<br>
                                    <strong>Bairro:</strong> ${data.bairro} -
                                    <strong>Localidade:</strong> ${data.localidade}<br>
                                    <strong>UF:</strong> ${data.uf} -
                                    <strong>Estado:</strong> ${data.estado}<br>
                                    <strong>Regi&atilde;o:</strong> ${data.regiao} -
                                    <strong>IBGE:</strong> ${data.ibge}<br>
                                    <strong>GIA:</strong> ${data.gia} -
                                    <strong>DDD:</strong> ${data.ddd}<br>
                                    <strong>SIAFI:</strong> ${data.siafi}<br>
                                </p>
                                </div>
                            </div>
                            `;
                        }
                        })
                        .catch(() => {
                        document.getElementById("resultadoCEP").innerHTML = "<div class='alert alert-danger'>Erro ao consultar o CEP.</div>";
                        });
                    }

                endContent
                .:SetContent(cScript)
            END WEBEXOBJECT
            WITH WEBEXOBJECT CLASS WebExControl TYPE div
                .:SetAttr("id","resultadoCEP")
                .:SetAttr("class","mt-4")
            END WEBEXOBJECT
        END WEBEXOBJECT
    END WEBEXOBJECT

    WebFileTools():HTMLFromControl(oFWWebExPage,"\web\fwwebex\tmp\",@cHTMLFile,@cHTML,.T.)

    WEBEXOBJECT CLEAN

return(cHTMLFile)
````

![image](https://github.com/user-attachments/assets/20f6358a-b92e-4a97-9b65-6c5621c744ee)

---

![image](https://github.com/user-attachments/assets/35b18409-a756-4c57-b4de-e81a641d8def)
