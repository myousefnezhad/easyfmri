class BrainExtractor():
    def run(self,SettingFileName,isshow=True):
        import os
        import numpy as np
        import nibabel as nb
        from nipype.interfaces import fsl
        import matplotlib
        matplotlib.rcParams['backend'] = "Qt5Agg"
        matplotlib.interactive(False)
        import matplotlib.pyplot as plt


        from utility import fixstr
        from Setting import Setting

        setting = Setting()
        setting.Load(SettingFileName)
        if (setting.empty) or (setting.Anat == False) :
            if setting.empty:
                print("Error in loading the setting file!")
            if not setting.Anat:
                print("This feature is disable for in setting file. Please turn it on from Advance menu!")
            return False
        else:
            SubNum = np.int32(setting.SubNum)
            SubLen = np.int32(setting.SubLen)

            for s in range(1, SubNum + 1):
                print("Analyzing Subject %d ..." % (s))
                SubDIR = setting.mainDIR + "/" + "sub-" + fixstr(s, SubLen, setting.SubPer)
                # checking anat file
                InFilename  = "sub-" + fixstr(s, SubLen, setting.SubPer) + "_T1w." + setting.BOLD
                OutFilename = "sub-" + fixstr(s, SubLen, setting.SubPer) + "_T1w_BET." + setting.BOLD
                PDFfilename = "sub-" + fixstr(s, SubLen, setting.SubPer) + "_T1w_BET.pdf"
                InAddr      = SubDIR + "/anat/" + InFilename
                OutAddr     = SubDIR + "/anat/" + OutFilename
                PDFAddr     = SubDIR + "/anat/" + PDFfilename
                if not os.path.isfile(InAddr):
                    print(InAddr, " - file not find!")
                    return False
                else:
                    bet                 = fsl.BET()
                    bet.inputs.in_file  = InAddr
                    bet.inputs.out_file = OutAddr
                    bet.run()
                    # Visualize In File
                    nii  = nb.load(InAddr)
                    data = nii.get_data()
                    dim  = np.shape(data)
                    if len(dim) > 3:
                        data = data[:, :, :, 0]
                    Ox = int(dim[0] / 2)
                    imgIn = data[Ox, :, :]
                    # Visualize Out File
                    nii  = nb.load(OutAddr)
                    data = nii.get_data()
                    dim  = np.shape(data)
                    if len(dim) > 3:
                        data = data[:, :, :, 0]
                    Ox = int(dim[0] / 2)
                    imgOut = data[Ox, :, :]
                    # Plot In and Out Images in a PDF file
                    fig, (ax1, ax2) = plt.subplots(1, 2, sharex='col', sharey='row')
                    ax1.set_title("Brain extractor result for Subject: " + str(s))
                    ax1.imshow(np.flipud(np.transpose(imgIn)), interpolation='nearest',  aspect='auto', cmap=plt.cm.gray)
                    ax2.imshow(np.flipud(np.transpose(imgOut)), interpolation='nearest', aspect='auto', cmap=plt.cm.gray)
                    plt.savefig(PDFAddr)
                    if isshow:
                        import webbrowser
                        webbrowser.open_new("file://"+PDFAddr)
                    print("Anatomical Brain for Subject " + str(s) + " is extracted.")
