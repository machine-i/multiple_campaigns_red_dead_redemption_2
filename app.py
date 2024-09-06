from os import rename, walk
from tkinter import *
from time import sleep
import subprocess

RAIZ = "C:/Users/Renê/Documents/Rockstar Games"


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title('Test')
        self.root.configure(background="#feffff")

        self.podeComecar = False

        # Dividindo a tela
        frame_cima = Frame(self.root, width=800, height=50, bg="#feffff", relief="flat")
        frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        frame_baixo = Frame(self.root, width=800, height=650, bg="#feffff", relief="flat")
        frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

        # Configurando parte de cima da tela
        nome_login = Label(frame_cima, text='ESCOLHE A CONTA QUE VAI JOGAR', height=1, anchor=NE, font=('Ivy 25 '), bg="#feffff",
                              fg="#403d3d")
        nome_login.place(x=5, y=5)

        linha_login = Label(frame_cima, width=765, text="", height=1, anchor=NW, font=('Ivy 1 '), bg="#00BFFF")
        linha_login.place(x=10, y=45)

        # Configurando parte de baixo da tela
        btn1 = Button(frame_baixo, command=lambda: self.mudar_pasta('wandinho'), text="WANDINHO", width=30, height=10,
                                  bg="#00BFFF", fg="#feffff", font=('Ivy 12 bold'),
                                  relief=RAISED, overrelief=RIDGE)
        btn1.place(x=15, y=50)

        btn2 = Button(frame_baixo, command=lambda: self.mudar_pasta('lucas'), text="LUCAS", width=30, height=10,
                                  bg="#00BFFF", fg="#feffff", font=('Ivy 12 bold'),
                                  relief=RAISED, overrelief=RIDGE)
        btn2.place(x=470, y=50)

        btn3 = Button(frame_baixo, command=lambda: self.mudar_pasta('levi'), text="LEVI", width=30, height=10,
                                  bg="#00BFFF", fg="#feffff", font=('Ivy 12 bold'),
                                  relief=RAISED, overrelief=RIDGE)
        btn3.place(x=15, y=300)

        btn4 = Button(frame_baixo, command=lambda: self.mudar_pasta('luan'), text="LUAN", width=30, height=10,
                                  bg="#00BFFF", fg="#feffff", font=('Ivy 12 bold'),
                                  relief=RAISED, overrelief=RIDGE)
        btn4.place(x=470, y=300)

        self.msm_erro = Label(frame_baixo, text="", height=1, anchor=NW, font=('Ivy 12 bold'), bg="#feffff", fg="red")
        self.msm_erro.place(x=350, y=570)

        self.root.protocol("WM_DELETE_WINDOW", self.fechar_janela)

    def mudar_pasta(self, jogador):
        try:
            self.salvar_pasta()

            src = f"{RAIZ}/Red Dead Redemption 2 - {jogador}"
            des = f"{RAIZ}/Red Dead Redemption 2"

            rename(src, des)

            self.podeComecar = True
            self.fechar_janela()
        except:
            self.exibir_erro_dashboard('Erro ao mudar a pasta.')

    def salvar_pasta(self):
        try:
            jogadores = ['wandinho', 'lucas', 'levi', 'luan']

            arquivos = []
            for root, dirs, file in walk(RAIZ):
                arquivos = dirs
                break

            arquivos_red_dead_atual = []
            for a in arquivos:
                if "Red Dead Redemption 2" in a:
                    arquivos_red_dead_atual.append(a.split(' - ')[-1])

            jogador_atual = [jogador for jogador in jogadores if jogador not in arquivos_red_dead_atual]

            src = f"{RAIZ}/Red Dead Redemption 2"
            des = f"{RAIZ}/Red Dead Redemption 2 - {jogador_atual[0]}"

            rename(src, des)
        except:
            self.exibir_erro_dashboard('Erro ao salvar arquivo do jogador anterior.')

    def exibir_erro_dashboard(self, mensagem):
        self.msm_erro.config(text=mensagem)

    def fechar_janela(self):
        sleep(1)

        if self.podeComecar:
            caminho_red_dead = 'C:/Program Files (x86)/Steam/steamapps/common/Red Dead Redemption 2/PlayRDR2.exe'

            sleep(1)

            self.root.destroy()

            try:
                resultado = subprocess.run([caminho_red_dead], check=True)
                print("Execução bem-sucedida.")
            except subprocess.CalledProcessError as e:
                print(f"Ocorreu um erro durante a execução: {e}")

        else:
            self.root.destroy()


tk = Tk()
tk.geometry('800x700')
win = Window(tk)

tk.mainloop()
