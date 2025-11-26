import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

# Lista para armazenar os clientes em memória
clientes = []


def salvar_cliente():
    nome = entry_nome.get().strip()
    telefone = entry_telefone.get().strip()
    recebe_novidades = var_novidades.get()

    if not nome or not telefone:
        messagebox.showwarning("Campo obrigatório", "Preencha nome e telefone.")
        return

    cliente = {
        "nome": nome,
        "telefone": telefone,
        "novidades": recebe_novidades
    }
    clientes.append(cliente)

    atualizar_lista()

    # Limpa campos
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    var_novidades.set(False)

    messagebox.showinfo("Sucesso", "Cliente salvo com sucesso! ✅")


def atualizar_lista():
    # Limpa a listbox
    listbox_clientes.delete(0, tk.END)

    for i, c in enumerate(clientes, start=1):
        recebe = "Sim" if c["novidades"] else "Não"
        texto = f"{i}. {c['nome']} | {c['telefone']} | Novidades: {recebe}"
        listbox_clientes.insert(tk.END, texto)


def exportar_vcf():
    if not clientes:
        messagebox.showwarning("Sem clientes", "Nenhum cliente para exportar.")
        return

    nome_arquivo = f"contatos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.vcf"

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            for c in clientes:
                f.write("BEGIN:VCARD\n")
                f.write("VERSION:3.0\n")
                f.write(f"FN:{c['nome']}\n")
                f.write(f"TEL;TYPE=CELL:{c['telefone']}\n")
                if c["novidades"]:
                    f.write("NOTE:Aceita receber novidades da loja\n")
                else:
                    f.write("NOTE:Não deseja receber novidades\n")
                f.write("END:VCARD\n\n")

        messagebox.showinfo(
            "Exportação concluída",
            f"Contatos exportados para o arquivo:\n{nome_arquivo}"
        )
    except Exception as e:
        messagebox.showerror("Erro ao exportar", f"Ocorreu um erro:\n{e}")


# ----------------- INTERFACE -----------------

janela = tk.Tk()
janela.title("Cadastro de Clientes - Loja")
janela.geometry("600x450")
janela.resizable(False, False)

# Cor de fundo
janela.configure(bg="#1e1e2f")

# Estilo geral
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TLabel",
    background="#1e1e2f",
    foreground="#ffffff",
    font=("Segoe UI", 10)
)

style.configure(
    "TButton",
    font=("Segoe UI", 10, "bold"),
    padding=6
)

style.configure(
    "Card.TLabelframe",
    background="#27293d",
    foreground="#ffffff",
    borderwidth=0,
    relief="flat"
)

style.configure(
    "Card.TLabelframe.Label",
    background="#27293d",
    foreground="#ffffff",
    font=("Segoe UI", 11, "bold")
)

# Título
titulo = tk.Label(
    janela,
    text="🛍️  CADASTRO DE CLIENTES  🛍️",
    bg="#1e1e2f",
    fg="#ffffff",
    font=("Segoe UI", 16, "bold")
)
titulo.pack(pady=10)

# Frame de cadastro
frame_cadastro = ttk.Labelframe(
    janela,
    text=" Dados do Cliente ",
    style="Card.TLabelframe"
)
frame_cadastro.pack(padx=15, pady=10, fill="x")

# Nome
label_nome = ttk.Label(frame_cadastro, text="Nome do cliente:")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_nome = ttk.Entry(frame_cadastro, width=40)
entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Telefone
label_telefone = ttk.Label(frame_cadastro, text="Telefone (com DDD):")
label_telefone.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_telefone = ttk.Entry(frame_cadastro, width=40)
entry_telefone.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Checkbox novidades
var_novidades = tk.BooleanVar()
check_novidades = ttk.Checkbutton(
    frame_cadastro,
    text="Cliente permite receber novidades?",
    variable=var_novidades
)
check_novidades.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Frame de botões
frame_botoes = tk.Frame(janela, bg="#1e1e2f")
frame_botoes.pack(pady=10)

btn_salvar = ttk.Button(frame_botoes, text="💾 Salvar cliente", command=salvar_cliente)
btn_salvar.grid(row=0, column=0, padx=5)

btn_exportar = ttk.Button(frame_botoes, text="📤 Exportar contatos (VCF)", command=exportar_vcf)
btn_exportar.grid(row=0, column=1, padx=5)

btn_atualizar = ttk.Button(frame_botoes, text="🔄 Atualizar lista", command=atualizar_lista)
btn_atualizar.grid(row=0, column=2, padx=5)

# Frame da lista de clientes
frame_lista = ttk.Labelframe(
    janela,
    text=" Clientes cadastrados ",
    style="Card.TLabelframe"
)
frame_lista.pack(padx=15, pady=10, fill="both", expand=True)

listbox_clientes = tk.Listbox(
    frame_lista,
    bg="#191a2a",
    fg="#ffffff",
    font=("Consolas", 10),
    height=10,
    selectbackground="#3b3f72",
    borderwidth=0,
    highlightthickness=0
)
listbox_clientes.pack(side="left", fill="both", expand=True, padx=8, pady=8)

scrollbar = tk.Scrollbar(frame_lista, command=listbox_clientes.yview)
scrollbar.pack(side="right", fill="y", pady=8)

listbox_clientes.config(yscrollcommand=scrollbar.set)

# Loop da interface
janela.mainloop()
