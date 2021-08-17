import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#print([f.name for f in matplotlib.font_manager.fontManager.ttflist])

plt.rcParams['pdf.use14corefonts'] = True
plt.rcParams['ps.useafm'] = True
# plt.rcParams['text.usetex'] = True

plt.rcParams['font.family'] = ['Helvetica']
# plt.rcParams['pdf.fonttype'] = 42
# plt.rcParams['ps.fonttype'] = 42

plt.figure(1, (7, 4))
plt.subplot(1, 1, 1)

width = 0.5
interval = 0.2

basex = np.linspace(1, 5, 3)

y1 = [3.875, 3.484, 3.024]
y2 = [8.057, 7.464, 6.561]

plt.ylim(0,11)

plt.bar(basex - interval / 2 - width / 2, y1, width=width, fc="#FFC125", label="w/o ElasticBF")   # hatch="/"
plt.bar(basex + interval / 2 + width / 2, y2, width=width, fc="#1874CD", label="with ElasticBF")

plt.ylabel('KOPS', fontsize=24)
plt.xticks(basex, ['LevelDB', 'RocksDB', 'PebblesDB'], fontsize=24)
plt.yticks(np.linspace(0, 10, 3), fontsize=26)
plt.legend(loc = "upper center", fontsize=18, ncol=2)
plt.savefig('aa.pdf', bbox_inches='tight')
