from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msb
from bd import *

########## Definindo Cores ##########

green = "#44d63c"
black = "#000"
black1 = "#333333"
white = "#fff"
blue = "#0074eb"  
red = "#f04141"  
green1 = "#59b356"

########## Funções de Tela e Banco ##########
global tree

dataBase()

def mostrar():
    tree.delete(*tree.get_children())
    elementos = selecionar()
    for elemento in elementos:
        tree.insert("", END, values=elemento, tag='1')

def deletarInfo(): # Só ta apagando no momento, nao ta deletando do banco
    if not tree.selection():
        msb.showwarning('ALERTA DE ERRO', 'Por favor, selecione o item na lista.', icon='warning')
    else:
        resultado = msb.askquestion('', 'Tem certeza que deseja deletar o contato?')
        if resultado == 'yes':
            treev_dados = tree.focus()
            treev_itens = (tree.item(treev_dados))
            tree_lista = treev_itens['values']
            id = tree_lista[0]
            tree.delete(treev_dados)
            deletar(id)
            msb.showinfo('Sucesso', 'Dados deletados com sucesso!')
            mostrar()

def addWindow(): # MEXER NO ATUALIZAR
    def adicionar():
        name = name_entry.get()
        brand = brand_entry.get()
        category = category_entry.get()
        provider = provider_entry.get()
        price = price_entry.get()
        regist_date = regist_date_entry.get()

        dados = [name, brand, category, provider, price, regist_date]
        if name == "" or brand == "" or category == "":
            msb.showerror('Erro', 'Preencha todos os campos!')
        else:
            inserir(dados)
            msb.showinfo('Sucesso', 'Dados inseridos com sucesso!')
            name_entry.delete(0, 'end')
            brand_entry.delete(0, 'end')
            category_entry.delete(0, 'end')
            provider_entry.delete(0, 'end')
            price_entry.delete(0, 'end')
            regist_date_entry.delete(0, 'end')
            """ for widget in addWindow.winfo_children():
                widget.destroy() """
        
        mostrar()
         
    addWindow = Tk()
    addWindow.resizable(width=FALSE, height=FALSE)
    addWindow.geometry('600x300')
    addWindow.title('*********ADICIONANDO PRODUTO*********') 
    addWindow.configure(background=black1)
    form_titulo = Frame(addWindow)
    form_titulo.pack(side=TOP)
    form_prod = Frame(addWindow)
    form_prod.pack(side=TOP, pady=10)

    # --------- LABELS - CADASTRAR -------------
    lbl_title = Label(form_titulo, text='Adicionando Produto',
                    font=('arial', 18), bg=black, fg=green, width=280)
    lbl_title.pack(fill=X)
    lbl_name = Label(form_prod, text='Nome', font=('arial', 12))
    lbl_name.grid(row=0, sticky=W)
    lbl_brand = Label(form_prod, text='Marca', font=('arial', 12))
    lbl_brand.grid(row=1, sticky=W)
    lbl_category = Label(form_prod, text='Categoria', font=('arial', 12))
    lbl_category.grid(row=2, sticky=W)
    lbl_provider = Label(form_prod, text='Fornecedor', font=('arial', 12))
    lbl_provider.grid(row=3, sticky=W)
    lbl_price = Label(form_prod, text='Preço', font=('arial', 12))
    lbl_price.grid(row=4, sticky=W)
    lbl_regist_date = Label(form_prod, text='Data de Registro', font=('arial', 12))
    lbl_regist_date.grid(row=5, sticky=W)

    # --------- ENTRY - CADASTRAR -------------
    name_entry = Entry(form_prod, font=('arial', 12))
    name_entry.grid(row=0, column=1)
    name_entry.focus()
    brand_entry = Entry(form_prod, font=('arial', 12))
    brand_entry.grid(row=1, column=1)
    category_entry = Entry(form_prod, font=('arial', 12))
    category_entry.grid(row=2, column=1)
    provider_entry = Entry(form_prod, font=('arial', 12))
    provider_entry.grid(row=3, column=1)
    price_entry = Entry(form_prod, font=('arial', 12))
    price_entry.grid(row=4, column=1)
    regist_date_entry = Entry(form_prod, font=('arial', 12))
    regist_date_entry.grid(row=5, column=1)

    dados = [[name_entry.get(), brand_entry.get(), category_entry.get(), provider_entry.get(), price_entry.get(), regist_date_entry.get()]]

    # --------- BOTÃO - CADASTRAR -------------
    bttn_enviardados = Button(form_prod, text="Cadastrar",
                            width=50, command=adicionar, bg=green, fg=black)
    bttn_enviardados.grid(row=6, columnspan=2, pady=10)

def updWindow():
    def atualizarInfo():
            try:
                treev_dados = tree.focus()
                treev_itens = tree.item(treev_dados)
                tree_lista = treev_itens['values']

                valor = tree_lista[0]

                name_entry.delete(0, 'end')
                brand_entry.delete(0, 'end')
                category_entry.delete(0, 'end')
                provider_entry.delete(0, 'end')
                price_entry.delete(0, 'end')
                regist_date_entry.delete(0, 'end')

                name_entry.insert(0, 'tree_lista[1]')
                brand_entry.insert(0, 'tree_lista[2]')
                category_entry.insert(0, 'tree_lista[3]')
                provider_entry.insert(0, 'tree_lista[4]')
                price_entry.insert(0, 'tree_lista[5]')
                regist_date_entry.insert(0, 'tree_lista[6]')

                atualizarCheck()
            except IndexError:
                msb.showerror('Erro', 'Selecione um dos dados na tabela!') 

    def atualizarCheck():
        name = name_entry.get()
        brand = brand_entry.get()
        category = category_entry.get()
        provider = provider_entry.get()
        price = price_entry.get()
        regist_date = regist_date_entry.get()

        dados = [name, brand, category, provider, price, regist_date]
        if name == "" or brand == "" or category == "":
            msb.showerror('Erro', 'Preencha todos os campos!')
        else:
            atualizar(dados)
            msb.showinfo('Sucesso', 'Dados inseridos com sucesso!')
            name_entry.delete(0, 'end')
            brand_entry.delete(0, 'end')
            category_entry.delete(0, 'end')
            provider_entry.delete(0, 'end')
            price_entry.delete(0, 'end')
            regist_date_entry.delete(0, 'end')
            """ for widget in addWindow.winfo_children():
                widget.destroy() """
        mostrar()

    atualizarInfo()

    addWindow = Tk()
    addWindow.resizable(width=FALSE, height=FALSE)
    addWindow.geometry('600x300')
    addWindow.title('*********ATUALIZANDO PRODUTO*********') 
    addWindow.configure(background=black1)
    form_titulo = Frame(addWindow)
    form_titulo.pack(side=TOP)
    form_prod = Frame(addWindow)
    form_prod.pack(side=TOP, pady=10)

    # --------- LABELS - CADASTRAR -------------
    lbl_title = Label(form_titulo, text='Atualizando Produto',
                    font=('arial', 18), bg=black, fg=green, width=280)
    lbl_title.pack(fill=X)
    lbl_name = Label(form_prod, text='Nome', font=('arial', 12))
    lbl_name.grid(row=0, sticky=W)
    lbl_brand = Label(form_prod, text='Marca', font=('arial', 12))
    lbl_brand.grid(row=1, sticky=W)
    lbl_category = Label(form_prod, text='Categoria', font=('arial', 12))
    lbl_category.grid(row=2, sticky=W)
    lbl_provider = Label(form_prod, text='Fornecedor', font=('arial', 12))
    lbl_provider.grid(row=3, sticky=W)
    lbl_price = Label(form_prod, text='Preço', font=('arial', 12))
    lbl_price.grid(row=4, sticky=W)
    lbl_regist_date = Label(form_prod, text='Data de Registro', font=('arial', 12))
    lbl_regist_date.grid(row=5, sticky=W)

    # --------- ENTRY - CADASTRAR -------------
    name_entry = Entry(form_prod, font=('arial', 12))
    name_entry.grid(row=0, column=1)
    name_entry.focus()
    brand_entry = Entry(form_prod, font=('arial', 12))
    brand_entry.grid(row=1, column=1)
    category_entry = Entry(form_prod, font=('arial', 12))
    category_entry.grid(row=2, column=1)
    provider_entry = Entry(form_prod, font=('arial', 12))
    provider_entry.grid(row=3, column=1)
    price_entry = Entry(form_prod, font=('arial', 12))
    price_entry.grid(row=4, column=1)
    regist_date_entry = Entry(form_prod, font=('arial', 12))
    regist_date_entry.grid(row=5, column=1)

    dados = [[name_entry.get(), brand_entry.get(), category_entry.get(), provider_entry.get(), price_entry.get(), regist_date_entry.get()]]

    # --------- BOTÃO - ATUALIZAR -------------
    bttn_atualizar = Button(form_prod, text="Atualizar",
                        width=50, command=atualizarCheck(), bg=green, fg=black)
    bttn_atualizar.grid(row=6, columnspan=2, pady=10)

########## Criando Janela Principal ##########

window = Tk()
window.resizable(width=FALSE, height=FALSE)
window.geometry('800x400')
window.title('TecStore') 
window.configure(background=black1)

########## Dividindo a janela em duas partes left e right ##########
left_frame = Frame(window, width=500, height=400, bg=white, relief="flat",)
left_frame.grid(row=0, column=0, sticky=NSEW)
right_frame = Frame(window, width=300, height=400, bg=black,  relief="flat",)
right_frame.grid(row=0, column=1, sticky=NSEW)

##### dividindo o frame esquerdo em três partes, top mid e bottom ######
left_t_frame = Frame(left_frame, width=500,
                     height=50, bg=black1, relief="flat",)
left_t_frame.grid(row=0, column=0, sticky=NSEW)
left_m_frame = Frame(left_frame, width=300,
                      height=50, bg=white, relief="flat",)
left_m_frame.grid(row=1, column=0, sticky=NSEW)
left_b_frame = Frame(left_frame, width=300,
                      height=300, bg=white, relief="flat",)
left_b_frame.grid(row=2, column=0, sticky=NSEW)

##### dividindo o frame direito em duas partes, top e bottom ######
right_t_frame = Frame(right_frame, width=300,
                     height=100, bg=black, relief="flat",)
right_t_frame.grid(row=0, column=0, sticky=NSEW)
right_b_frame = Frame(right_frame, width=300,
                      height=300, bg=black, relief="flat",)
right_b_frame.grid(row=1, column=0, sticky=NSEW)

##### criando botões no frame right_b_frame  ########
b_create = Button(right_b_frame, text="+ Novo", width=20, height=2, bg=blue, fg="white",
                font="5", anchor="center", relief=RAISED, command=addWindow)
b_create.grid(row=0, column=0,  sticky=NSEW, pady=15, padx=50)

b_delete = Button(right_b_frame, text="Remover", width=20, height=2, bg=red,
                   fg="white", font="5", anchor="center", relief=RAISED, command=deletarInfo)
b_delete.grid(row=1, column=0,  sticky=NSEW, pady=15, padx=50)

b_update = Button(right_b_frame, text="Atualizar", width=20, height=2, bg=green1, fg="white",
                     font="5", anchor="center", relief=RAISED, command=updWindow)
b_update.grid(row=2, column=0,  sticky=NSEW, pady=15, padx=50)

######### Adicionando Label e TreeView no left_t_frame e left_b_frame ########
label = Label(left_t_frame, text="TecStore", width=32, height=2, pady=2, relief="flat", anchor="center", font=('Courier  20 bold'), bg=white, fg=black1)
label.grid(row=0, column=0,  sticky=NSEW, pady=1)

tree = ttk.Treeview(left_b_frame, selectmode="browse", column=("coluna1", "coluna2", "coluna3", "coluna4", "coluna5", "coluna6", "coluna7"), show='headings')
tree.column("coluna1", width=50, minwidth=5, stretch=NO, anchor="center")
tree.heading("#1", text='Id')
tree.column("coluna2", width=90, minwidth=5, stretch=NO, anchor="center")
tree.heading("#2", text='Nome')
tree.column("coluna3", width=73, minwidth=5, stretch=NO, anchor="center")
tree.heading("#3", text='Marca')
tree.column("coluna4", width=73, minwidth=5, stretch=NO, anchor="center")
tree.heading("#4", text='Categoria')
tree.column("coluna5", width=75, minwidth=5, stretch=NO, anchor="center")
tree.heading("#5", text='Fornecedor')
tree.column("coluna6", width=60, minwidth=5, stretch=NO, anchor="center")
tree.heading("#6", text='Preço')
tree.column("coluna7", width=80, minwidth=5, stretch=NO, anchor="center")
tree.heading("#7", text='Data Registro')
tree.grid(row=0, column=0, padx=5)

mostrar()

window.mainloop()
