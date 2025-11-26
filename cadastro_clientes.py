import csv
import re
from pathlib import Path
from datetime import datetime

ARQUIVO_CSV = "clientes.csv"
E164_BR = re.compile(r"^\+55\d{10,11}$")


def normalizar_tel_br(bruto: str) -> str:
    """Converte telefone para padrão +55DDDNUMERO."""
    d = re.sub(r"\D", "", bruto)

    if d.startswith("55"):
        d = "+" + d
    elif len(d) in (10, 11):
        d = "+55" + d
    else:
        raise ValueError("Telefone inválido. Use DDD + número.")

    if not E164_BR.match(d):
        raise ValueError("Telefone inválido. Use DDD + número.")
    return d


def salvar_cliente(nome, telefone_br, consentiu):
    telefone = normalizar_tel_br(telefone_br)

    existe = Path(ARQUIVO_CSV).exists()
    with open(ARQUIVO_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not existe:
            w.writerow(["nome", "telefone_e164", "consentiu", "criado_em"])
        w.writerow([nome, telefone, consentiu, datetime.now().isoformat()])

    print("\n✔ Cliente salvo!\n")


def listar_clientes():
    if not Path(ARQUIVO_CSV).exists():
        print("\nNenhum cliente cadastrado ainda.\n")
        return

    with open(ARQUIVO_CSV, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        print("\n===== CLIENTES CADASTRADOS =====")
        for row in r:
            print(f"{row['nome']} | {row['telefone_e164']} | Consentiu: {row['consentiu']}")
        print("=================================\n")


def exportar_vcf():
    if not Path(ARQUIVO_CSV).exists():
        print("\nNenhum cliente cadastrado para exportar.\n")
        return

    nome_arquivo = f"contatos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.vcf"

    with open(ARQUIVO_CSV, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)

        linhas = []
        for row in r:
            if row["consentiu"] == "1":
                linhas += [
                    "BEGIN:VCARD",
                    "VERSION:3.0",
                    f"N:{row['nome']};;;;",
                    f"FN:{row['nome']}",
                    f"TEL;TYPE=CELL:{row['telefone_e164']}",
                    "END:VCARD",
                    ""
                ]

    if linhas:
        Path(nome_arquivo).write_text("\n".join(linhas), encoding="utf-8")
        print(f"\n✔ Arquivo VCF gerado: {nome_arquivo}")
        print("Importe no seu celular para criar uma lista de transmissão.\n")
    else:
        print("\nNenhum cliente com opt-in para exportar.\n")


def menu():
    while True:
        print("""
===============================
 CADASTRO DE CLIENTES - LOJA
===============================
1 - Cadastrar cliente
2 - Listar clientes
3 - Exportar contatos (VCF)
4 - Sair
""")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("\nNome do cliente: ")
            tel = input("Telefone (com DDD): ")
            consentiu = input("Cliente permitiu receber novidades? (s/n): ").lower() == "s"

            try:
                salvar_cliente(nome, tel, int(consentiu))
            except Exception as e:
                print(f"\n❌ Erro: {e}\n")

        elif opc == "2":
            listar_clientes()

        elif opc == "3":
            exportar_vcf()

        elif opc == "4":
            print("Saindo...")
            break

        else:
            print("\nOpção inválida.\n")


if __name__ == "__main__":
    menu()
