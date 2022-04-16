# class A:
#     def __init__(self):
#         super().__init__()
#         print('a')
#         self.att_a = 1
#
#
# class B:
#     def __init__(self):
#         super().__init__()
#         print('b')
#         self.att_b = 2
#
#
#
# class C(B, A):
#     def __init__(self):
#         super().__init__()
#         print('c')
#
#
# c = C()


import pandas as pd
import numpy as np

data = pd.read_csv('data_python.csv')
data2 = pd.read_csv('data_r.csv')

V = data['Visible'].values
V2 = data2['Visible'].values-1
# Transition Probabilities
a = np.array(((0.50, 0.50), (0.50, 0.50)))

# Emission Probabilities
b = np.array(((0.125, 0.375, 0.5), (0.125, 0.375, 0.5)))

# Equal Probabilities for the initial distribution
initial_distribution = np.array((0.5, 0.5))

# V = np.array([0,1,2,1])

def forward(V, a, b, initial_distribution):
    alpha = np.zeros((V.shape[0], a.shape[0]))
    alpha[0, :] = initial_distribution * b[:, V[0]]

    for t in range(1, V.shape[0]):
        for j in range(a.shape[0]):
            # Matrix Computation Steps
            #                  ((1x2) . (1x2))      *     (1)
            #                        (1)            *     (1)
            alpha[t, j] = alpha[t - 1].dot(a[:, j]) * b[j, V[t]]

    return alpha



#
# def forward(V, T, E, initial_distribution):
#     """
#
#     Parameters
#     ----------
#     V: (n,), sequence of observations
#     T: (N,N), Transition Probabilities, N states
#     E: (N,M), Emission Probabilities, M observation states
#     initial_distribution: (N,), initial distribution of N states
#     t: int, time-point
#
#     Returns: (n,N), alpha, Forward Algorithm to store probability of each t_observation, O(T^2*n)
#     -------
#
#     """
#     n = V.shape[0]
#     N = T.shape[0]
#     alpha = np.zeros((n, N))
#     for i in range(n):
#         o = V[i] ## observation
#         if i == 0:
#             alpha[i, :] = initial_distribution * E[:, o]
#         else:
#             # Matrix Computation Steps,
#             # 1.(matrix multiplication) (N,) x (N,N) = (N,)
#             # 2.(element-wise product) (N,) * (N,)
#             alpha[i, :] = np.dot(alpha[i-1, :], T) * E[:, o]
#     return alpha
#
#
# alpha = forward(V, a, b, initial_distribution)
# print(alpha)



def backward(V, T, E):
    n = V.shape[0]
    N = T.shape[0]
    beta = np.zeros((n, N))
    for i in range(n):
        o = V[-1-i+1] ## observation
        if i == 0:
            beta[-1-i, :] = np.ones(N)
        else:
            # Matrix Computation Steps,
            # 1.(element-wise product) (N,) * (N,) , beta * emission
            # 2.(matrix multiplication) (N,) x (N,N) = (N,), (1) x transition
            beta[-1-i, :] = np.dot(T, beta[-1-i+1, :] * E[:, o])
    return beta

beta = backward(V, a, b)
print(beta)


def baum_welch(V, T, E, initial_distribution, n_iter=100):
    n = V.shape[0] ## sequence size
    N = T.shape[0]

    for i in range(n_iter):
        alpha = forward(V, T, E, initial_distribution)
        beta = backward(V, T, E)

        xi = np.zeros((N, N, n - 1))
        for j in range(n - 1):
            denominator = np.dot(np.dot(alpha[j, :].T, T) * E[:, V[j + 1]].T, beta[j + 1, :])
            for k in range(N):
                numerator = alpha[j, k] * T[k, :] * E[:, V[j + 1]].T * beta[j + 1, :].T
                xi[k, :, j] = numerator / denominator

        gamma = np.sum(xi, axis=1)
        T = np.sum(xi, 2) / np.sum(gamma, axis=1).reshape((-1, 1))

        # Add additional T'th element in gamma
        gamma = np.hstack((gamma, np.sum(xi[:, :, n - 2], axis=0).reshape((-1, 1))))

        K = E.shape[1]
        denominator = np.sum(gamma, axis=1)
        for l in range(K):
            E[:, l] = np.sum(gamma[:, V == l], axis=1)

        E = np.divide(E, denominator.reshape((-1, 1)))

    return T, E



def viterbi(V, a, b, initial_distribution):
    T = V.shape[0]
    M = a.shape[0]

    omega = np.zeros((T, M))
    omega[0, :] = np.log(initial_distribution * b[:, V[0]])

    prev = np.zeros((T - 1, M))

    for t in range(1, T):
        for j in range(M):
            # Same as Forward Probability
            probability = omega[t - 1] + np.log(a[:, j]) + np.log(b[j, V[t]])

            # This is our most probable state given previous state at time t (1)
            prev[t - 1, j] = np.argmax(probability)

            # This is the probability of the most probable state (2)
            omega[t, j] = np.max(probability)

    # Path Array
    S = np.zeros(T)

    # Find the most probable last hidden state
    last_state = np.argmax(omega[T - 1, :])

    S[0] = last_state

    backtrack_index = 1
    for i in range(T - 2, -1, -1):
        S[backtrack_index] = prev[i, int(last_state)]
        last_state = prev[i, int(last_state)]
        backtrack_index += 1

    # Flip the path array since we were backtracking
    S = np.flip(S, axis=0)

    # Convert numeric values to actual hidden states
    result = []
    for s in S:
        if s == 0:
            result.append("A")
        else:
            result.append("B")

    return result


# # Transition Probabilities
# a = np.ones((2, 2))
# a = a / np.sum(a, axis=1)
#
# # Emission Probabilities
# b = np.array(((1, 3, 5), (2, 4, 6)))
# b = b / np.sum(b, axis=1).reshape((-1, 1))

T, E = baum_welch(V, a, b, initial_distribution, n_iter=100)

print(viterbi(V, a, b, initial_distribution))

"""



"""