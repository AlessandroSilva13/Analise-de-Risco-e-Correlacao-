# Ibovespa Correlation Heatmap

## Sobre o Projeto
Este projeto é um script de **Análise Quantitativa** desenvolvido em Python para mapear o risco e a diversificação de portfólio. Ele extrai dados históricos da B3, calcula a matriz de correlação de retornos diários entre os principais ativos do Ibovespa e gera um mapa de calor (heatmap) de alta fidelidade visual.

A análise de correlação é indispensável para investidores e gestores que buscam balancear carteiras. Este módulo foi desenhado para ser rápido e gerar *outputs* já estilizados (Dark Mode), ideais tanto para consumo executivo quanto para integração em um Terminal Financeiro mais abrangente.

## Tecnologias Utilizadas
* **Python 3.x**
* **[yfinance](https://pypi.org/project/yfinance/):** Para conexão via API e ingestão de cotações históricas de fechamento ajustado.
* **[Pandas](https://pandas.pydata.org/):** Para sanitização dos dados temporais (`dropna`) e cálculo da matriz de correlação de Pearson sobre as variações percentuais.
* **[Seaborn](https://seaborn.pydata.org/) & [Matplotlib](https://matplotlib.org/):** Para a renderização visual do heatmap, utilizando colormap divergente (`RdYlGn`) e exportação em alta resolução (300 DPI).

## Funcionalidades
1. **Extração Dinâmica:** Download simultâneo de séries temporais de 1 ano para uma cesta de ativos selecionados (ex: `PETR4.SA`, `VALE3.SA`, `ITUB4.SA`).
2. **Cálculo de Retornos:** Conversão das cotações em retornos logarítmicos/diários para medir a real volatilidade e dependência entre as ações.
3. **Design Estilizado:** Gráfico configurado com *Dark Background* e paleta Semáforo (Verde = Correlação Positiva, Vermelho = Correlação Negativa), formatado para legibilidade em relatórios e mídias sociais.
4. **Exportação Automática:** Salvamento direto do output em `.png` com enquadramento ajustado (`bbox_inches='tight'`).
