import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'WEGE3.SA', 'ABEV3.SA']


dados = yf.download(tickers, period="1y")


retornos = dados.pct_change().dropna()
correlacao = retornos.corr()


plt.style.use("dark_background")
plt.figure(figsize=(8, 8))


sns.heatmap(correlacao, 
            annot=True, 
            cmap="RdYlGn",
            fmt=".2f", 
            linewidths=1,
            linecolor='black',
            cbar_kws={"shrink": .8},
            square=True)

plt.title('Mapa de Correlação - Ibovespa (1 Ano)', fontsize=16, pad=20, weight='bold')
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12, rotation=0)


plt.tight_layout()
plt.savefig('heatmap_ibovespa_ig.png', dpi=300, bbox_inches='tight')
plt.show()
