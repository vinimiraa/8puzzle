import os
import sys

# ----------------------------
# Configuração do ambiente
# ----------------------------

# Adiciona o diretório pai ao sys.path para importar módulos corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import tracemalloc
from puzzle.state import State
from puzzle.solver import Puzzle
from puzzle.algorithms import Algorithms, Heuristics


# ----------------------------
# Definições de entrada
# ----------------------------

TEST_CASES = {
    "Easy": State([[1, 2, 3], [4, 5, 6], [0, 7, 8]]),
    "Medium": State([[1, 2, 3], [4, 0, 6], [7, 5, 8]]),
    "Hard": State([[7, 2, 4], [5, 0, 6], [8, 3, 1]])
}

GOAL_STATE = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

benchmark_results = []

# ----------------------------
# Funções auxiliares
# ----------------------------

def format_label(algorithm: Algorithms, heuristic: Heuristics) -> str:
    """
    Formata o nome do algoritmo e heurística para exibição.
    """
    label = algorithm.name
    if algorithm in [Algorithms.A_STAR, Algorithms.GREEDY]:
        label += f" ({heuristic.name})"
    return label
# format_label

def run_benchmark(case_name: str, initial_state: State, 
                  algorithm: Algorithms, heuristic: Heuristics = Heuristics.NONE) -> None:
    """
    Executa o benchmark de um caso com determinado algoritmo e heurística.
    """
    solver = Puzzle(initial_state, GOAL_STATE, algorithm=algorithm, heuristic=heuristic)

    tracemalloc.start()
    start_time = time.time()
    path = solver.solve()
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time_elapsed = end_time - start_time
    memory_kb = peak / 1024
    steps = len(path) - 1 if path else -1

    benchmark_results.append({
        "Caso": case_name,
        "Algoritmo": format_label(algorithm, heuristic),
        "Tempo (s)": f"{time_elapsed:.4f}",
        "Memória (KB)": f"{memory_kb:.2f}",
        "Passos": steps,
    })
# run_benchmark

def run_all_tests() -> None:
    """
    Executa todos os testes com combinações de algoritmos e heurísticas.
    """
    for case_name, initial_state in TEST_CASES.items():
        for algorithm in Algorithms:
            if algorithm in [Algorithms.A_STAR, Algorithms.GREEDY]:
                for heuristic in [Heuristics.MANHATTAN, Heuristics.MISPLACED]:
                    run_benchmark(case_name, initial_state, algorithm, heuristic)
            else:
                run_benchmark(case_name, initial_state, algorithm)
# run_all_tests

def display_results() -> None:
    """
    Exibe os resultados formatados em tabela.
    """
    print(f"{'Caso':<10} {'Algoritmo':<25} {'Tempo (s)':<10} {'Memória (KB)':<15} {'Passos':<10}")
    print("-" * 80)
    for result in benchmark_results:
        print(f"{result['Caso']:<10} {result['Algoritmo']:<25} "
              f"{result['Tempo (s)']:<10} {result['Memória (KB)']:<15} {result['Passos']:<10}")
# display_results

def save_results_to_files(directory="resultados"):
    """
    Salva os resultados em arquivos separados por caso.
    """
    os.makedirs(directory, exist_ok=True)

    grouped_results = {}
    for result in benchmark_results:
        case = result["Caso"]
        grouped_results.setdefault(case, []).append(result)

    for case_name, case_results in grouped_results.items():
        filename = os.path.join(directory, f"{case_name}.txt")
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Case: {case_name}\n\n")
            file.write(f"Initial State:\n{TEST_CASES[case_name]}\n\n")
            file.write(f"Goal State:\n{GOAL_STATE}\n\n")
            file.write(f"Results:\n")

            file.write("-" * 70 + "\n")
            file.write(f"{'Algorithms':<25} {'Time (s)':<10} {'Memory (KB)':<15} {'Steps':<10}\n")
            file.write("-" * 70 + "\n")

            for r in case_results:
                file.write(f"{r['Algoritmo']:<25} {r['Tempo (s)']:<10} "
                           f"{r['Memória (KB)']:<15} {r['Passos']:<10}\n")
# save_results_to_files

# ----------------------------
# Execução principal
# ----------------------------

if __name__ == "__main__":
    run_all_tests()
    display_results()
    save_results_to_files('tests/data')
