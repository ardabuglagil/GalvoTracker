import matplotlib.pyplot as plt
import numpy as np


a_m5 = [0.044,
0.026,
0.023,
0.024,
0.005,
0.006,
0,
0.009,
0.016,
0.017,
0.015,
0.001,
0.02



]

a_0 =[0.008,
0.012,
0.018,
0.009,
0.016,
0.023,
0,
0.021,
0.029,
0.003,
0.006,
0.017,
0.025



]

a_5 =[0.018,
0.025,
0.014,
0.01,
0.015,
0.002,
0,
0.004,
0.012,
0.003,
0.012,
0.03,
0.035


    
]


x = [-3,
-2.5,
-2,
-1.5,
-1,
-0.5,
0,
0.5,
1,
1.5,
2,
2.5,
3
]


plt.plot(x, a_m5)
plt.plot(x, a_0)
plt.plot(x, a_5)

plt.xlabel("x (mm)")
plt.ylabel("Absolute Error (mm)")
plt.legend(["y = -5 mm", "y = 0 mm", "y = 5 mm"])
plt.grid()
plt.show()
