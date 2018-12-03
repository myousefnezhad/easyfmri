import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

class DrawRSA():
    def ShowFigure(self, var, labels, title, FontSize=14, XRot=45, YRot=0):
        NumData = np.shape(var)[0]
        plt.figure(num=None, figsize=(NumData, NumData), dpi=100)
        plt.pcolor(var, vmin=np.min(var), vmax=np.max(var))
        plt.xlim([0, NumData])
        plt.ylim([0, NumData])
        cbar = plt.colorbar()
        cbar.ax.tick_params(labelsize=FontSize)
        ax = plt.gca()
        ax.invert_yaxis()
        ax.set_aspect(1)
        ax.set_yticks(np.arange(NumData) + 0.5, minor=False)
        ax.set_xticks(np.arange(NumData) + 0.5, minor=False)
        ax.set_xticklabels(labels, minor=False, fontsize=FontSize, rotation=XRot)
        ax.set_yticklabels(labels, minor=False, fontsize=FontSize, rotation=YRot)
        ax.grid(False)
        ax.set_aspect(1)
        ax.set_frame_on(False)
        for t in ax.xaxis.get_major_ticks():
            t.tick1On = False
            t.tick2On = False
        for t in ax.yaxis.get_major_ticks():
            t.tick1On = False
            t.tick2On = False
        plt.title(title)
        plt.show(block=False)


    def ShowMat(self, var, title, FontSize=14):
        NumData = np.shape(var)[0]
        plt.matshow(var)
        plt.xlim([0, NumData])
        plt.ylim([0, NumData])
        cbar = plt.colorbar()
        cbar.ax.tick_params(labelsize=FontSize)
        frame1 = plt.gca()
        for xlabel_i in frame1.axes.get_xticklabels():
            xlabel_i.set_visible(False)
            xlabel_i.set_fontsize(0.0)
        for xlabel_i in frame1.axes.get_yticklabels():
            xlabel_i.set_fontsize(0.0)
            xlabel_i.set_visible(False)
        for tick in frame1.axes.get_xticklines():
            tick.set_visible(False)
        for tick in frame1.axes.get_yticklines():
            tick.set_visible(False)
        plt.title(title)
        plt.show(block=False)


    def ShowDend(self, Z, labels, title, FontSize=14, Rot=45):
        plt.figure(figsize=(25, 10), )
        plt.title(title)
        dendrogram(Z, labels=labels, leaf_font_size=FontSize, color_threshold=1, leaf_rotation=Rot)
        plt.show(block=False)