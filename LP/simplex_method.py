import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
import warnings

def simplex(c, A, b, maximize=True, plot_3d=False):
    def simplex_solver(c, A, b, maximize=True):
        if maximize:
            c = -c  # Convert maximization to minimization
        result = linprog(c, A_ub=A, b_ub=b)
        return result

    def simplex_print_solution(result):
        print("Decision Variables:", result.x)
        print("Objective Value:", -result.fun)  # Convert back to maximization if needed

    def plot_2d_solution(result, A, b):
        x = np.linspace(0, 10, 100)
        for i in range(len(b)):
            y = (b[i] - A[i, 0] * x) / A[i, 1]
            plt.plot(x, y, label=f'Constraint {i + 1}')

        plt.scatter(result.x[0], result.x[1], color='red', marker='o', label='Optimal Point')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Feasible Region and Optimal Point')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_3d_solution(result, A, b):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            x = np.linspace(0, 10, 100)
            y = np.linspace(0, 10, 100)
            X, Y = np.meshgrid(x, y)

            for i in range(len(b)):
                Z = (b[i] - A[i, 0] * X - A[i, 1] * Y) / A[i, 2]
                ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100)

            ax.scatter(result.x[0], result.x[1], -result.fun, color='red', marker='o', label='Optimal Point')

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title('Feasible Region and Optimal Point')
            plt.show()

    result = simplex_solver(c, A, b, maximize)

    if plot_3d:
        plot_3d_solution(result, A, b)
    else:
        plot_2d_solution(result, A, b)

    simplex_print_solution(result)