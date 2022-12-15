
# edit by jiawei 2.00

import numpy as np
import matplotlib.pyplot as plt

def generate_guass(mu, sigma, n):

#    mu     - Mean of distribution
#    sigma - Covariance matrix of distribution
#    n     - Number of vectors 

    return np.random.multivariate_normal(mu, sigma, n)

def guass(mu, n):

    guass = generate_guass(mu, np.eye(2), n)
    return guass


def boundary():

    guass1 = guass([1, 0], 1000)
    guass2 = guass([-1, 0], 1000)
    plt.figure()
    plt.scatter(guass1[:,0], guass1[:,1], s=50, marker='.')
    plt.scatter(guass2[:,0], guass2[:,1], s=50, marker='.')
    plt.plot([0, 0], [-3, 3], linewidth = 4, c = 'g')
    plt.legend(['boundary','Class1', 'Class2'])
    plt.savefig('bound')


def err(guass_1, guass_2):

    err = (np.sum(guass_1[:, 0] < 0) + np.sum(guass_2[:, 0] > 0) )/(guass_1.shape[0] + guass_2.shape[0])
    return err


if __name__ == '__main__':

    boundary()
    x, y = [], []
    for i in range(100, 1100, 100):

        guass_1 = guass([1, 0], i)
        guass_2 = guass([-1, 0], i)
        x.append(i)
        y.append(err(guass_1, guass_2))
    plt.figure()
    plt.plot(x, y)
    plt.xlabel('number of samples')
    plt.ylabel('error')
    plt.savefig('err1')

    for i in range(100, 100000, 100):

        guass_1 = guass([1, 0], i)
        guass_2 = guass([-1, 0], i)
        x.append(i)
        y.append(err(guass_1, guass_2))
    plt.figure()
    plt.plot(x, y)
    plt.xlabel('number of samples')
    plt.ylabel('error')
    plt.savefig('err2')

    plt.show()

