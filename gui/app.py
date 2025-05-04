import sys
import os
# Adiciona o diretório pai ao sys.path para importar módulos corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import random
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from puzzle.state import State
from puzzle.solver import Puzzle
from puzzle.algorithms import Algorithms, Heuristics

class PuzzleGUI:
    """
    Classe para a interface gráfica do jogo 8-Puzzle.
    """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("8-Puzzle - IA")
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.selected_algorithm = tk.StringVar(value=Algorithms.BFS.name)
        self.selected_heuristic = tk.StringVar(value=Heuristics.NONE.name)
        self.initial_state = None
        self.goal_state = State([[1,2,3],[4,5,6],[7,8,0]])
        self.solution_path = []
        self.step_index = 0
        self.puzzle = None
        self.start_time = None
        self.timer_running = False

        self.build_navbar()
        self.build_main_area()
    # __init__

    def build_navbar(self):
        """
        Cria a barra de navegação com os botões para escolher algoritmo, heurística e outras ações.
        """
        navbar = tk.Frame(self.root)
        navbar.pack(pady=10)

        # Algoritmo
        ttk.Label(navbar, text="Algoritmo:").pack(side="left")
        algo_menu = ttk.OptionMenu(navbar, self.selected_algorithm, self.selected_algorithm.get(), *[a.name for a in Algorithms])
        algo_menu.pack(side="left", padx=5)

        # Heurística
        ttk.Label(navbar, text="Heurística:").pack(side="left")
        heur_menu = ttk.OptionMenu(navbar, self.selected_heuristic, self.selected_heuristic.get(), *[h.name for h in Heuristics])
        heur_menu.pack(side="left", padx=5)

        # Botões
        ttk.Button(navbar, text="Carregar Estado", command=self.load_state).pack(side="left", padx=5)
        ttk.Button(navbar, text="Aleatório", command=self.generate_random).pack(side="left", padx=5)
        ttk.Button(navbar, text="Resolver", command=self.solve_puzzle).pack(side="left", padx=5)
        ttk.Button(navbar, text="Reiniciar", command=self.reset_puzzle).pack(side="left", padx=5)
        ttk.Button(navbar, text="Sair", command=self.root.quit).pack(side="left", padx=5)
        ttk.Button(navbar, text="Sobre", command=self.show_about).pack(side="left", padx=5)
    # build_navbar

    def show_about(self):
        about_text = (
            "8-Puzzle Solver\n\n"
            "Autor: Vinícius Miranda de Araújo\n\n"
            # "Matrícula: 812839\n\n"
            "Curso: Ciência da Computação\n\n"
            "Instituição: Pontificia Universidade Católica de Minas Gerais\n\n"
            "Disciplina: Inteligência Artificial - 1º semestre de 2025\n\n"
            "GitHub: https://github.com/vinimiraa/\n\n"
            "Repositório: https://github.com/vinimiraa/8puzzle"
        )
        messagebox.showinfo("Sobre o Projeto", about_text, parent=self.root, icon="info")
    # show_about

    def build_main_area(self):
        """
        Cria a área principal da interface com o título, tabuleiro e contadores.
        """
        self.title_label = tk.Label(self.root, text="8-Puzzle Solver", font=("Helvetica", 18, "bold"))
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(self.root, text="Escolha algoritmo e heurística para começar")
        self.info_label.pack(pady=5)

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=10)
        self.buttons = [[tk.Button(self.board_frame, width=4, height=2, font=("Helvetica", 18)) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.status_label = tk.Label(self.root, text="Passos: 0 | Tempo: 0.00s")
        self.status_label.pack(pady=10)
    # build_main_area

    def update_board(self, state: State):
        """
        Atualiza o tabuleiro com o estado atual do puzzle.
        """
        for i in range(3):
            for j in range(3):
                val = state.board[i][j]
                self.buttons[i][j]["text"] = "" if val == 0 else str(val)
    # update_board

    def generate_random(self):
        """
        Gera um estado inicial aleatório para o puzzle.
        """
        try:
            nums = list(range(9))
            random.shuffle(nums)
            self.initial_state = State([nums[i:i+3] for i in range(0, 9, 3)])
            self.update_board(self.initial_state)
        except Exception as e:
            messagebox.showerror("Erro ao gerar estado aleatório", str(e))
    # generate_random

    def load_state(self):
        """
        Carrega um estado inicial a partir de um arquivo de texto.
        O arquivo deve conter 3 linhas, cada uma com 3 números inteiros representando o estado do puzzle.
        
        Exemplo:
        >1 2 3\n
        >4 5 6\n
        >7 8 0\n
        """
        try:
            path = filedialog.askopenfilename(title="Escolher arquivo", filetypes=[("Text files", "*.txt")])
            if not path:
                return
            with open(path) as f:
                lines = f.readlines()
                if len(lines) != 3:
                    raise ValueError("O arquivo deve conter exatamente 3 linhas.")
                grid = [list(map(int, line.strip().split())) for line in lines]
                if any(len(row) != 3 for row in grid):
                    raise ValueError("Cada linha deve conter exatamente 3 números.")
                self.initial_state = State(grid)
                self.update_board(self.initial_state)
        except Exception as e:
            messagebox.showerror("Erro ao carregar estado", str(e))
    # load_state

    def solve_puzzle(self):
        """
        Inicia a resolução do puzzle com o algoritmo e heurística selecionados.
        """
        try:
            if not self.initial_state:
                messagebox.showerror("Erro", "Escolha um estado inicial primeiro.")
                return

            algorithm = Algorithms[self.selected_algorithm.get()]
            heuristic = Heuristics[self.selected_heuristic.get()]

            if algorithm in {Algorithms.A_STAR, Algorithms.GREEDY} and heuristic == Heuristics.NONE:
                messagebox.showerror("Erro", "Selecione uma heurística para o algoritmo escolhido.")
                return

            self.puzzle = Puzzle(self.initial_state, self.goal_state, algorithm=algorithm, heuristic=heuristic)

            def run_solver():
                """
                Executa a resolução do puzzle em uma thread separada para evitar travamento da interface.
                """
                try:
                    self.start_time = time.time()
                    self.timer_running = True
                    self.update_timer()
                    path = self.puzzle.solve()
                    self.timer_running = False

                    if path is None:
                        messagebox.showerror("Erro", "Não foi possível encontrar uma solução.")
                        return

                    self.solution_path = path
                    self.step_index = 0
                    self.animate_solution()
                except Exception as e:
                    self.timer_running = False
                    messagebox.showerror("Erro durante a resolução", str(e))

            threading.Thread(target=run_solver).start()
        except Exception as e:
            messagebox.showerror("Erro ao iniciar a resolução", str(e))
    # solve_puzzle

    def animate_solution(self):
        """
        Anima a solução do puzzle, atualizando o tabuleiro a cada passo.
        """
        try:
            if not self.solution_path or self.step_index >= len(self.solution_path):
                return
            state = self.solution_path[self.step_index]
            self.update_board(state)
            self.step_index += 1
            self.status_label["text"] = f"Passos: {self.step_index} | Tempo: {time.time() - self.start_time:.2f}s"
            self.root.after(500, self.animate_solution)
        except Exception as e:
            messagebox.showerror("Erro durante a animação", str(e))
    # animate_solution

    def update_timer(self):
        """
        Atualiza o contador de tempo a cada 100ms.
        """
        if self.timer_running:
            elapsed = time.time() - self.start_time
            self.status_label["text"] = f"Passos: {self.step_index} | Tempo: {elapsed:.2f}s"
            self.root.after(100, self.update_timer)
    # update_timer

    def reset_puzzle(self):
        """
        Reinicia o jogo, limpando o tabuleiro e os contadores.
        """
        if self.initial_state:
            self.update_board(self.initial_state)
            self.solution_path = []
            self.step_index = 0
            self.status_label["text"] = "Passos: 0 | Tempo: 0.00s"
    # reset_puzzle
# PuzzleGUI

class UI:
    """
    Classe para executar a interface gráfica do quebra-cabeça.
    """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.puzzle_gui = PuzzleGUI(root)
    # __init__

    def run_gui(self):
        """
        Executa a interface gráfica.
        """
        self.root.mainloop()
    # run_gui
# UI

if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    app.run_gui()
