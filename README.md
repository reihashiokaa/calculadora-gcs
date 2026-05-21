# Calculadora GCS

Laboratório colaborativo da disciplina de Gerência de Configuração de Software.

## Integrantes

| Nome | GitHub | Papel | Módulo |
|---|---|---|---|
| Reinaldo | reihashiokaa | Mantenedor | Revisão, merges e proteção da main |
| Beatriz | biavieirakkj | Desenvolvedora | Módulo A — Básico |
| Luciana | lunah1 | Desenvolvedora | Módulo B — Potência |
| Duda | dudamacedo26 | Desenvolvedora | Módulo C — Percentual |
| Isabela | isaabelamg | Desenvolvedora | Módulo D — Estatística |
| Miguel | miguelpaullo | Desenvolvedor | Módulo E — Conversão |

## Link do repositório

https://github.com/reihashiokaa/calculadora-gcs

## Fluxo de trabalho adotado

Este projeto segue o GitHub Flow:

1. Criar uma feature branch a partir da main.
2. Implementar o módulo na feature branch.
3. Fazer commits com mensagens claras.
4. Enviar a branch para o GitHub.
5. Abrir Pull Request.
6. Revisar o Pull Request.
7. Fazer merge na main somente após aprovação.
8. Todos os integrantes atualizam a main local com `git pull origin main`.

## Distribuição dos módulos

| Módulo | Arquivo | Responsável | Funções |
|---|---|---|---|
| A — Básico | `calc_basico.py` | Beatriz | `somar()`, `subtrair()`, `multiplicar()`, `dividir()` |
| B — Potência | `calc_potencia.py` | Luciana | `potencia()`, `raiz_quadrada()`, `raiz_cubica()` |
| C — Percentual | `calc_percentual.py` | Duda | `percentual()`, `acrescimo()`, `desconto()` |
| D — Estatística | `calc_estatistica.py` | Isabela | `media()`, `mediana()`, `desvio_padrao()` |
| E — Conversão | `calc_conversao.py` | Miguel | `celsius_para_fahrenheit()`, `km_para_milhas()`, `kg_para_libras()` |

## Como executar

```bash
python main.py