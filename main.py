# $ python main.py

if __name__ == "__main__":
    from puzzle.solver import Puzzle
    from puzzle.state import State
    from puzzle.algorithms import Algorithms, Heuristics

    estado_inicial = State([[0, 8, 7], [6, 5, 4], [3, 2, 1]])
    estado_final = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    print("Estado inicial:")
    print(estado_inicial)
    print("-" * 20)
    print("Estado final:")
    print(estado_final)
    print("-" * 20)
    

    # Por padrao, o algoritmo A* e a heuristica de Manhattan sao usados	
    puzzle = Puzzle(estado_inicial, estado_final)

    caminho_solucao = puzzle.solve()

    if caminho_solucao:
        print("Solução encontrada!")
        for i, estado in enumerate(caminho_solucao):
            print(f"Passo {i}:")
            print(estado)            
    else:
        print("Nenhuma solução encontrada.")

    print("-" * 20)

    print("Abrir interface? (s/n)")
    abrir_interface = input().strip().lower()
    
    if abrir_interface == "s":
        import tkinter as tk
        from gui.app import UI
        ui = UI(tk.Tk())
        ui.run_gui()

