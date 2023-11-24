from matplotlib import pyplot as plt
import numpy as np

data = {}
cur_obj = ''
with open('solar_system_statistic_dt100.txt') as file:
    for line in file.readlines():
        pars = line.split(' ')
##        print(pars[0])
        if pars[0].isalpha():
##            print('Yeh')
            if pars[0] in data:
                i = 1
                while pars[0]+f'{i}' in data:
                    i += 1
                cur_obj = pars[0]+f'{i}'
            else:
                cur_obj = pars[0]
            data[cur_obj] = []
        else:
##            print('Argh')
            data[cur_obj].append(list(map(float, pars)))

fig, ax = plt.subplots(len(data.keys()) - 1, 3, figsize = (21, 30))
## Нам нужно построить модуль скорости от времени, растояние от времени, модуль скорости от растояния
star = 'star'
star_data   = np.array(data[star])
counter_mod = 0
for i, planet in enumerate(list(data.keys())):
    if planet == star:
        counter_mod = -1
        continue
    i += counter_mod
    planet_data = np.array(data[planet])

    t = planet_data[:,0]
    r = ((planet_data[:,1] - star_data[:,1])**2 + (planet_data[:,2] - star_data[:,2])**2)**.5
    v = ((planet_data[:,3] - star_data[:,3])**2 + (planet_data[:,4] - star_data[:,4])**2)**.5
    ax[i, 0].plot(t, v)
    ax[i, 0].set_title('v(t)')
    ax[i, 0].grid()
    ax[i, 1].plot(t, r)
    ax[i, 1].set_title('r(t)')
    ax[i, 1].grid()
    ax[i, 2].plot(r, v)
    ax[i, 2].set_title('v(r)')
    ax[i, 2].grid()
plt.show()
    

