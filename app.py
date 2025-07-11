import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode("dark")  # Modo escuro  


# Criação da janela principal
app = ctk.CTk()  # Cria a janela principal
app.geometry("400x300")  # Define o tamanho da janela
app.title("Sistema de Login")  # Define o título da janela

# Criação dos campos
#label
label_usuario = ctk.CTkLabel(app, text="Usuário")  # Cria um rótulo
label_usuario.pack(pady=10)  # Adiciona o rótulo à janela com espaçamento vertical
# entry
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite o seu usuário")  # Cria um campo de entrada
campo_usuario.pack(pady=10)  # Adiciona o campo de entrada à janela   
# label 
label_senha = ctk.CTkLabel(app, text="Senha")  # Cria um rótulo para a senha
label_senha.pack(pady=10)  # Adiciona o rótulo à janela
# entry
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite a sua senha", show="*")  # Cria um campo de entrada para a senha, com caracteres ocultos
campo_senha.pack(pady=10)  # Adiciona o campo de entrada à janela   

# Criação de funções de funcionalidades     
def validar_login():
    usuario = campo_usuario.get()  # Obtém o texto do campo de usuário
    senha = campo_senha.get()  # Obtém o texto do campo de senha
    
    # Verifica se os campos estão preenchidos
    if not usuario or not senha:
        campo_feedback.configure(text="Por favor, preencha todos os campos.", text_color="red")
        return
    
    # Aqui você pode adicionar a lógica de autenticação
    if usuario == "admin" and senha == "1234":
        campo_feedback.configure(text="Login bem-sucedido!", text_color="green")
    else:
        campo_feedback.configure(text="Usuário ou senha incorretos.", text_color="red")

#buttom     
botao_login = ctk.CTkButton(app, text="Login" ,command=validar_login)  # Cria um botão de login
botao_login.pack(pady=20)  # Adiciona o botão à janela          

# campo feed-back de login
campo_feedback = ctk.CTkLabel(app, text="")   # Cria um rótulo para feedback de login
campo_feedback.pack(pady=10)  # Adicion   
# Inicia o loop da aplicação

app.mainloop()  # Inicia o loop da aplicação, mantendo a janela aberta

