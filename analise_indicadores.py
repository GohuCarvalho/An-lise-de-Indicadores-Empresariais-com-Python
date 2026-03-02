import pandas as pd

tabelas = pd.read_csv("dados.csv")

print("\n📊 VISÃO GERAL DOS INDICADORES")
print(tabelas.describe())

prejuizo = tabelas[tabelas["lucro"] < 0]

if not prejuizo.empty:
    print("\n⚠️ REGISTROS COM PREJUÍZO:")
    print(prejuizo[["mes", "lucro"]])
else:
    print("\n✅ Nenhum mês com prejuízo detectado.")

media_reclamacoes = tabelas["reclamacoes"].mean()
reclamacoes_acima_media = tabelas[tabelas["reclamacoes"] > media_reclamacoes]

print(f"\n📈 Média de reclamações: {media_reclamacoes:.0f}")

if not reclamacoes_acima_media.empty:
    print("\n⚠️ MESES COM RECLAMAÇÕES ACIMA DA MÉDIA:")
    print(reclamacoes_acima_media[["mes", "reclamacoes"]])

tabelas["variacao_clientes"] = tabelas["clientes_ativos"].diff()
queda_clientes = tabelas[tabelas["variacao_clientes"] < 0]

if not queda_clientes.empty:
    print("\n⚠️ QUEDA NO NÚMERO DE CLIENTES ATIVOS:")
    print(queda_clientes[["mes", "variacao_clientes"]])

media_atendimento = tabelas["tempo_medio_atendimento"].mean()
atendimento_acima_media = tabelas[
    tabelas["tempo_medio_atendimento"] > media_atendimento
]

print(f"\n⏱ Tempo médio geral de atendimento: {media_atendimento:.1f} minutos")

if not atendimento_acima_media.empty:
    print("\n⚠️ MESES COM TEMPO DE ATENDIMENTO ACIMA DA MÉDIA:")
    print(atendimento_acima_media[["mes", "tempo_medio_atendimento"]])

print("\n🧠 DIAGNÓSTICO AUTOMÁTICO")

tabelas["status"] = "🟢 Estável"

for _, linha in tabelas.iterrows():
    if linha["lucro"] < 0 or linha["reclamacoes"] > media_reclamacoes * 1.3:
        tabelas.loc[linha.name, "status"] = "🔴 Crítico"

    elif (
        linha["variacao_clientes"] < 0
        or linha["tempo_medio_atendimento"] > media_atendimento
    ):
        tabelas.loc[linha.name, "status"] = "🟡 Atenção"

print("\n📋 RESUMO FINAL DOS INDICADORES")
print(
    tabelas[
        [
            "mes",
            "lucro",
            "reclamacoes",
            "clientes_ativos",
            "tempo_medio_atendimento",
            "status",
        ]
    ]
)

print("\n📄 RESUMO EXECUTIVO")

lucro_medio = tabelas["lucro"].mean()
meses_prejuizo = len(prejuizo)

print(
    f"O período analisado apresentou um lucro médio de {lucro_medio:.0f}. "
    f"Foram identificados {meses_prejuizo} mês(es) com prejuízo. "
    f"A média de reclamações foi de {media_reclamacoes:.0f} "
    f"e o tempo médio de atendimento ficou em {media_atendimento:.1f} minutos."
)

with open("relatorio_analise.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("RELATÓRIO DE ANÁLISE DE INDICADORES\n\n")
    arquivo.write("RESUMO EXECUTIVO\n")
    arquivo.write(
        f"Lucro médio: {lucro_medio:.0f}\n"
        f"Meses com prejuízo: {meses_prejuizo}\n"
        f"Média de reclamações: {media_reclamacoes:.0f}\n"
        f"Tempo médio de atendimento: {media_atendimento:.1f} minutos\n\n"
    )
    arquivo.write("DETALHAMENTO DOS INDICADORES\n")
    arquivo.write(tabelas.to_string(index=False))