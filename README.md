# FW.WebEX — Framework Web Extensível para Protheus (ADVPL/TLPP)
![dna_tech_logo_black_panter](https://github.com/user-attachments/assets/b3e14547-41e0-484f-9d42-533fc71c28b8)
--
**FW.WebEX** é um microframework escrito em ADVPL/TLPP que permite criar interfaces web responsivas, modernas e funcionais **diretamente do seu código no Protheus**, sem precisar de Angular, React ou qualquer outra parafernália.

> **Do Protheus para o browser. Simples. Direto. Web.**

---

## 🚀 Por que FW.WebEX?

A TOTVS está indo para o web. Mas o desenvolvedor ADVPL não precisa reaprender Angular ou TypeScript só pra fazer uma tela de cadastro ou uma tabela com ação.

**FW.WebEX** nasceu da ideia de manter o espírito do desenvolvimento no Protheus:
- Rápido
- Sem burocracia
- Produtivo

Só que agora... **na web.**

---

## ⚙️ O que ele faz?

- Gera páginas HTML com sintaxe 100% TLPP
- Usa **Bootstrap** para comportamento (modais, tabelas, botões)
- Pode usar **PO UI (opcional)** para identidade visual padrão TOTVS
- Tem componentes já prontos como:
  - `fw.webex.page`
  - `fw.webex.control`
  - `fw.webex.table` (com checkbox, modal de exclusão, etc.)
- Permite encadeamento estilo `WITH OBJECT ... END`, via `WithObject()/EndWith()`

---

## 💡 Exemplo de uso

```advpl
WithObject(FWPage():New("Cadastro"))
   SetAttr("class", "container")

   WithObject(FWTable():FromSQL("SELECT * FROM TABELA"))
      SetAttr("class", "table-striped")
   EndWith()

EndWith()
````

---

## 🧩 Dependências

* Nenhuma no backend (ADVPL puro)
* Frontend usa:

  * [Bootstrap 5.3](https://getbootstrap.com)
  * (opcional) [PO UI CSS](https://po-ui.io)

---

## 📦 Como usar

1. Clone o repositório
2. Copie os arquivos `.tlpp` para seu projeto
3. Use o `FWPage():Render()` como entrada principal
4. Adicione seus próprios componentes ou estenda os existentes

---

## 🤝 Quer contribuir?

Toda ajuda é bem-vinda! A ideia aqui é **evoluir juntos** como comunidade Protheus:

* Criar novos componentes (`fw.webex.form`, `fw.webex.chart`, etc.)
* Melhorar o renderizador
* Adicionar eventos dinâmicos
* Documentar com mais exemplos

---

## ✨ Visão

> Acreditamos que dá pra evoluir mantendo o que o Protheus tem de melhor: a produtividade.
> FW\.WebEX é o passo que faltava pra quem quer ir pro web **sem perder a alma ADVPL**.

---

## 📄 Licença

[MIT](LICENSE)

---
