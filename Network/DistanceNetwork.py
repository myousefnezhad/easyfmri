import numpy as np
import nibabel as nb
from Visualization.AtlasParcellation import AtlasParcellation

def ClassicNetworkAnalysis(X, L, Coord, Integration, Metric, AtlasImg, affine=np.eye(4), KeepRegions=None, AtlasPath="/tmp/atlas.nii.gz", Threshold=0.95):
    listL = sorted(np.unique(L))
    print(f"List of labels {listL}")
    # Generate RegMap
    RegionMap = {}
    for cooIdx, coo in enumerate(Coord):
        reg = AtlasImg[coo[0], coo[1], coo[2]]
        if reg != 0:
            try:
                RegionMap[reg].append(cooIdx)
            except:
                RegionMap[reg] = list()
                RegionMap[reg].append(cooIdx)
    AtlasRegNum = len(RegionMap.keys())
    print(f"Number of regions: {AtlasRegNum}")
    print("Region map is generated!")
    # Reshape data over label
    XR = list()
    for ll in listL:
        xl = X[np.where(L == ll)[0], :]
        xri = list()
        for regID in sorted(RegionMap.keys()):
            xlr = xl[:, RegionMap[regID]]
            xlri = Integration(xlr)
            xri.append(xlri)
            print(f"Label: {ll}, Region {regID} is done.")
        XR.append(np.transpose(xri))
    NetworkNum = np.shape(XR)[0]
    print(f"Number of networks: {NetworkNum}")
    # Generate Network
    Net = np.zeros((NetworkNum, AtlasRegNum, AtlasRegNum))
    for nn, xxr in enumerate(XR):
        for i in range(AtlasRegNum):
            for j in range(i + 1, AtlasRegNum):
                Net[nn, i, j] = Metric(xxr[:, i], xxr[:, j])
                Net[nn, j, i] = Net[nn, i, j]
                print(f"Label: {nn}, Network: {i} vs {j} is compared.")
    NetMaxValue = np.max(Net[:])
    print(f"Network maximum value: {NetMaxValue}")
    NetThreshold = Threshold * NetMaxValue
    print(f"Network Threshold: {NetThreshold}")
    # Threshold
    for nn, _ in enumerate(XR):
        for i in range(AtlasRegNum):
            for j in range(i + 1, AtlasRegNum):
                if Net[nn, i, j] < NetThreshold:
                    Net[nn, i, j] = 0
                    Net[nn, j, i] = 0
                    print(f"Label: {nn}, Network: {i} vs {j} is thresholded.")
    # Active Region
    ActiveRegions = list()
    ActiveRegionIndex = list()
    for regIndx, regID in enumerate(sorted(RegionMap.keys())):
        IsZero = True
        if regID in KeepRegions:
            IsZero = False
        else:
            for nn, _ in enumerate(XR):
                if sum(Net[nn, regIndx, :]) != 0:
                    IsZero = False
                    break
        if not IsZero:
            ActiveRegions.append(regID)
            ActiveRegionIndex.append(regIndx)
    print(f"Number of active regions: {np.shape(ActiveRegions)[0]}")
    print(f"Active Regions: {ActiveRegions}")
    print("Generating thresholded networks ...")
    ThrNet = list()
    for nn in Net:
        nn1 = nn[ActiveRegionIndex, :]
        ThrNet.append(nn1[:, ActiveRegionIndex])
    # Generate Atlas
    print("Generating atlas...")
    AtlasShape = np.shape(AtlasImg)
    A = np.zeros(AtlasShape)
    for ar in ActiveRegions:
        for index in RegionMap[ar]:
            A[Coord[index, 0], Coord[index, 1], Coord[index, 2]] = ar
    AIMG = nb.Nifti1Image(A, affine)
    nb.save(AIMG, AtlasPath)
    # Atlas parcellation
    print("Parcellating atlas ...")
    ACoord = AtlasParcellation(AtlasPath)
    return Net, ThrNet, ActiveRegions, A, ACoord, listL
