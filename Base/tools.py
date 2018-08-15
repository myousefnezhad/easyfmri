# General
from GUI.frmDataEditor import frmDataEditor
from GUI.frmResultReport import frmResultReport
from GUI.frmImageInfo import frmImageInfo
# Preprocessing
from GUI.frmScriptEditor import frmScriptEditor
from GUI.frmRenameFile import frmRenameFile
from GUI.frmfMRIConcatenator import frmfMRIConcatenator
from GUI.frmEventConcatenator import frmEventConcatenator
# Feature Analysis
from GUI.frmEzMat import frmEzMat
from GUI.frmCombineData import frmCombineData
from GUI.frmRemoveRestScan import frmRemoveRestScan
from GUI.frmRemoveRestScanCross import frmRemoveRestScanCross
# Model Analysis
from GUI.frmSKModelEditor import frmSKModelEditor
from GUI.frmSKCModelEditor import frmSKCModelEditor
# Visualization
from GUI.frmMatNITF import frmMatNITF
from GUI.frmNITFAFNI import frmNITFAFNI
from GUI.frmTransformationMatrix import frmTansformationMatrix

class Tools:
    def combo(self, combobox):
        # General
        combobox.addItem("General: Data/Result Viewer",  10001)
        combobox.addItem("General: Report from multi-file results",  10002)
        combobox.addItem("General: Image Information",  10003)
        # Preprocessing
        combobox.addItem("Preprocessing: Group Script Editor",  20001)
        combobox.addItem("Preprocessing: Group Rename Files",  20002)
        combobox.addItem("Preprocessing: fMRI Concatenator",  20003)
        combobox.addItem("Preprocessing: Event Concatenator",  20004)
        # Feature Analysis
        combobox.addItem("Feature Analysis: Create Transformation Matrix",  30001)
        combobox.addItem("Feature Analysis: Convert EasyData to MatLab",  30002)
        combobox.addItem("Feature Analysis: MatLab: Combine Datasets",  30003)
        combobox.addItem("Feature Analysis: MatLab: Remove Rest Scans (before cross validation)",  30004)
        combobox.addItem("Feature Analysis: MatLab: Remove Rest Scans (after cross validation)",  30005)
        # Model Analysis
        combobox.addItem("Model Analysis: SK Classification Model Viewer",  40001)
        combobox.addItem("Model Analysis: SK Clustring Model Viewer",  40002)
        # Visualization
        combobox.addItem("Visualization: Convert Matrix to Nifti1",  50001)
        combobox.addItem("Visualization: Convert Nifti1 to AFNI",  50002)


    def run(self, ID):
        # General
        if   ID == 10001:
            frmDataEditor.show(frmDataEditor)
        elif ID == 10002:
            frmResultReport.show(frmResultReport)
        elif ID == 10003:
            frmImageInfo.show(frmImageInfo)
        # Preprocessing
        elif ID == 20001:
            frmScriptEditor.show(frmScriptEditor)
        elif ID == 20002:
            frmRenameFile.show(frmRenameFile)
        elif ID == 20003:
            frmfMRIConcatenator.show(frmfMRIConcatenator)
        elif ID == 20004:
            frmEventConcatenator.show(frmEventConcatenator)
        # Feature Analysis
        elif ID == 30001:
            frmTansformationMatrix.show(frmTansformationMatrix)
        elif ID == 30002:
            frmEzMat.show(frmEzMat)
        elif ID == 30003:
            frmCombineData.show(frmCombineData)
        elif ID == 30004:
            frmRemoveRestScan.show(frmRemoveRestScan)
        elif ID == 30005:
            frmRemoveRestScanCross.show(frmRemoveRestScanCross)
        # Model Analysis
        elif ID == 40001:
            frmSKModelEditor.show(frmSKModelEditor)
        elif ID == 40002:
            frmSKCModelEditor.show(frmSKCModelEditor)
        # Visualization
        elif ID == 50001:
            frmMatNITF.show(frmMatNITF)
        elif ID == 50002:
            frmNITFAFNI.show(frmNITFAFNI)