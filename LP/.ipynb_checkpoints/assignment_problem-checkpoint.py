import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linear_sum_assignment

def assignment_solver(cost_matrix):
    _, assignment = linear_sum_assignment(cost_matrix)
    assignments = np.zeros_like(cost_matrix)
    assignments[np.arange(len(assignment)), assignment] = 1
    total_cost = np.sum(assignments * cost_matrix)

    return assignments, total_cost

def assignment(cost_matrix):
    assignments, total_cost = assignment_solver(cost_matrix)
    print("Optimal Assignments:\n")
    print(assignments)
    print("\nTotal Cost:", total_cost)
    print("\n")
    fig, ax = plt.subplots()
    im = ax.imshow(cost_matrix, cmap='Greys', interpolation='nearest', origin='upper')

    for i in range(assignments.shape[0]):
        for j in range(assignments.shape[1]):
            if assignments[i, j] == 1:
                plt.text(j, i, f'{cost_matrix[i, j]}', color='red', ha='center', va='center', fontsize=12)
            else:
                plt.text(j, i, f'{cost_matrix[i, j]}', color='blue', ha='center', va='center', fontsize=12)

    plt.xlabel('Agents')
    plt.ylabel('Tasks')
    plt.title('Assignment Problem Solution')
    plt.axis('off')
    plt.show()
