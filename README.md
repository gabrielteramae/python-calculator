# Python Calculator — calculadora gráfica

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-stdlib-3776AB)

Janela Tkinter com as quatro operações, troca de sinal, porcentagem, apagar o último caractere e limpar. A expressão fica no histórico acima do visor. Não há dependência externa e o repositório não fixa a versão do Python.

| Avaliação | O que entra | O que fica de fora |
| --- | --- | --- |
| `ast.parse(..., mode="eval")` e `eval` com `__builtins__` vazio | número, `+`, `-`, `*`, `/` e unário | nome, chamada, potência e qualquer outro nó; divisão por zero vira `Erro` |

O resultado numérico passa por `round(..., 10)`. O botão de vírgula acrescenta `.`. O visor troca `*` por `×` e `/` por `÷`. O tema é `clam`, para a cor do `ttk.Button` valer no macOS.

## Stack

- `tkinter` e `ttk` (biblioteca padrão)
- `ast` para barrar expressão que não seja aritmética

## Estrutura

```
.
├── calculadora.py    # janela, botões e evaluate
└── .gitignore
```

Não existe `requirements.txt`. Fundo `#0c1024`, botões de operação `#ffb84d`, igual `#5b8def`. A janela não é redimensionável.

## Como rodar

```bash
git clone https://github.com/gabrielteramae/python-calculator.git
cd python-calculator
python3 calculadora.py
```

Precisa de um Python com Tk (a maioria dos instaladores oficiais traz; alguns builds mínimos de Linux não) e de uma sessão gráfica. Sem display, o `Tk()` falha na hora.

## Testes realizados

Não há suíte de testes.

---

© 2026 Gabriel Teramae Chan
