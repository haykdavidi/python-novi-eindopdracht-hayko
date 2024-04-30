# Module die door middel van matplotlib een heatmap genereert waarin je de meest vervuilde locaties kunt achterhalen

import os
import numpy as np
import matplotlib.pyplot as plt

CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
GAS_FILE = os.path.join(CURRENT_DIRECTORY, "assignment-files", "gases.csv")


# Inlezen CO2 data vanuit het csv-gassenbestand en plotten data
def lees_gas_co2(gases_file):
    gasarray = (np.loadtxt(gases_file, delimiter=',', skiprows=1, usecols=2)).reshape((100, 100))

    print(gasarray)
    plt.imshow(gasarray)
    plt.colorbar()
    plt.show()
