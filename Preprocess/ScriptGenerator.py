class ScriptGenerator:
    def run(self,SettingFileName):
        import numpy as np
        import nibabel as nb
        import scipy.io as io

        from Base.utility import fixstr,setParameters3, strRange, strMultiRange
        from Base.Setting import Setting
        setting = Setting()
        setting.Load(SettingFileName)
        if setting.empty:
            print("Error in loading the setting file!")
            return False
        else:
            Subjects = strRange(setting.SubRange,Unique=True)
            if Subjects is None:
                print("Cannot load Subject Range!")
                return False
            SubSize = len(Subjects)

            Counters = strMultiRange(setting.ConRange,SubSize)
            if Counters is None:
                print("Cannot load Counter Range!")
                return False

            Runs = strMultiRange(setting.RunRange,SubSize)
            if Runs is None:
                print("Cannot load Run Range!")
                return False

            for si, s in enumerate(Subjects):
                  for cnt in Counters[si]:
                        print("Analyzing Subject %d, Counter %d ..." % (s, cnt))
                        for r in Runs[si]:
                            ScriptAddr = setParameters3(setting.Script,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),\
                                                           fixstr(r, setting.RunLen, setting.RunPer), setting.Task,\
                                                           fixstr(cnt, setting.ConLen, setting.ConPer))


                            ScriptOutputAddr = setParameters3(setting.Analysis,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),\
                                                               fixstr(r, setting.RunLen, setting.RunPer), setting.Task,\
                                                           fixstr(cnt, setting.ConLen, setting.ConPer))

                            BOLDaddr = setParameters3(setting.BOLD,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),\
                                                        fixstr(r, setting.RunLen, setting.RunPer), setting.Task,\
                                                           fixstr(cnt, setting.ConLen, setting.ConPer))

                            MRIFile = nb.load(BOLDaddr)

                            # Generate Script
                            scriptFile = open(ScriptAddr,"w")
                            scriptFile.write("\n# FEAT version number\nset fmri(version) 6.00\n\n# Are we in MELODIC?\nset fmri(inmelodic) 0\n\n")
                            scriptFile.write("# Analysis level\n# 1 : First-level analysis\n# 2 : Higher-level analysis\nset fmri(level) 1\n\n")
                            scriptFile.write("# Which stages to run\n# 0 : No first-level analysis (registration and/or group stats only)\n")
                            scriptFile.write("# 7 : Full first-level analysis\n# 1 : Pre-processing\n# 2 : Statistics\nset fmri(analysis) 7\n\n")
                            scriptFile.write("# Use relative filenames\nset fmri(relative_yn) 0\n\n")
                            scriptFile.write("# Balloon help\nset fmri(help_yn) 1\n\n")
                            scriptFile.write("# Run Featwatcher\nset fmri(featwatcher_yn) 0\n\n")
                            scriptFile.write("# Cleanup first-level standard-space images\nset fmri(sscleanup_yn) 0\n\n")
                            scriptFile.write("# Output directory\nset fmri(outputdir) \"" + ScriptOutputAddr + "\"\n\n")
                            # TR
                            scriptFile.write("# TR(s)\nset fmri(tr) %0.6f\n\n" % setting.TR)
                            # Total Volumes
                            if setting.TotalVol == 0:
                                print("Auto Detect Total Volumes = " + str(MRIFile.get_shape()[3]) + ", File: " + BOLDaddr)
                                scriptFile.write("# Total volumes\nset fmri(npts) " + str(MRIFile.get_shape()[3]) + "\n\n")
                            else:
                                scriptFile.write("# Total volumes\nset fmri(npts) " + str(setting.TotalVol) + "\n\n")
                            # Delete Volumes
                            scriptFile.write("# Delete volumes\nset fmri(ndelete) " + str(setting.DeleteVol) + "\n\n")

                            scriptFile.write("# Perfusion tag/control order\nset fmri(tagfirst) 1\n\n")
                            scriptFile.write("# Number of first-level analyses\nset fmri(multiple) 1\n\n")
                            scriptFile.write("# Higher-level input type\n# 1 : Inputs are lower-level FEAT directories\n# 2 : Inputs are cope images from FEAT directories\nset fmri(inputtype) 2\n\n")
                            scriptFile.write("# Carry out pre-stats processing?\nset fmri(filtering_yn) 1\n\n")
                            scriptFile.write("# Brain/background threshold, %\nset fmri(brain_thresfh) 10\n\n")
                            scriptFile.write("# Critical z for design efficiency calculation\nset fmri(critical_z) " + str(setting.DEZT) + "\n\n")
                            scriptFile.write("# Noise level\nset fmri(noise) " + str(setting.DENL) + "\n\n# Noise AR(1)\nset fmri(noisear) " + str(setting.DETS) + "\n\n")
                            # Motion Correction: ALWAYS ON
                            scriptFile.write("# Motion correction\n# 0 : None\n# 1 : MCFLIRT\nset fmri(mc) 1\n\n")

                            scriptFile.write("# Spin-history (currently obsolete)\nset fmri(sh_yn) 0\n\n")
                            scriptFile.write("# B0 fieldmap unwarping?\nset fmri(regunwarp_yn) 0\n\n")
                            scriptFile.write("# EPI dwell time (ms)\nset fmri(dwell) 0.7\n\n")
                            scriptFile.write("# EPI TE (ms)\nset fmri(te) 35\n\n")
                            scriptFile.write("# % Signal loss threshold\nset fmri(signallossthresh) 10\n\n")
                            scriptFile.write("# Unwarp direction\nset fmri(unwarp_dir) y-\n\n")
                            scriptFile.write("# Slice timing correction\n# 0 : None\n# 1 : Regular up (0, 1, 2, 3, ...)\n# 2 : Regular down\n")
                            scriptFile.write("# 3 : Use slice order file\n# 4 : Use slice timings file\n# 5 : Interleaved (0, 2, 4 ... 1, 3, 5 ... )\n")
                            # Slice Timing
                            scriptFile.write("set fmri(st) " + str(setting.TimeSlice) + "\n\n")

                            scriptFile.write("# Slice timings file\nset fmri(st_file) \"\"\n\n")
                            scriptFile.write("# BET brain extraction\nset fmri(bet_yn) 1\n\n")
                            # FWHM
                            scriptFile.write("# Spatial smoothing FWHM (mm)\nset fmri(smooth) " + str(setting.FWHM) + "\n\n")

                            scriptFile.write("# Intensity normalization\nset fmri(norm_yn) 0\n\n")
                            scriptFile.write("# Perfusion subtraction\nset fmri(perfsub_yn) 0\n\n")
                            scriptFile.write("# Highpass temporal filtering\nset fmri(temphp_yn) 1\n\n")
                            scriptFile.write("# Lowpass temporal filtering\nset fmri(templp_yn) 0\n\n")
                            scriptFile.write("# MELODIC ICA data exploration\nset fmri(melodic_yn) 0\n\n")
                            scriptFile.write("# Carry out main stats?\nset fmri(stats_yn) 1\n\n")
                            scriptFile.write("# Carry out prewhitening?\nset fmri(prewhiten_yn) 1\n\n")
                            scriptFile.write("# Add motion parameters to model\n# 0 : No\n# 1 : Yes\nset fmri(motionevs) 1\nset fmri(motionevsbeta) \"\"\nset fmri(scriptevsbeta) \"\"\n\n")
                            scriptFile.write("# Robust outlier detection in FLAME?\nset fmri(robust_yn) 0\n\n")
                            scriptFile.write("# Higher-level modelling\n# 3 : Fixed effects\n# 0 : Mixed Effects: Simple OLS\n# 2 : Mixed Effects: FLAME 1\n# 1 : Mixed Effects: FLAME 1+2\nset fmri(mixed_yn) 2\n\n")
                            # Conditions
                            #ConditionFile = SubDIR + "/func/" + "sub-" + fixstr(s, SubLen, setting.SubPer) + "_task-" + setting.Task + "_run-" + fixstr(r, RunLen, setting.RunPer) + "_events/Cond.mat"
                            ConditionFile =  setParameters3(setting.EventFolder,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),\
                                                        fixstr(r, setting.RunLen, setting.RunPer), setting.Task, fixstr(cnt, setting.ConLen, setting.ConPer)) + setting.CondPre + ".mat"

                            Cond = io.loadmat(ConditionFile)
                            Conditions = Cond["Cond"]
                            CondLen = len(Conditions)
                            scriptFile.write("# Number of EVs\nset fmri(evs_orig) "+str(CondLen)+"\nset fmri(evs_real) "+str(CondLen)+"\nset fmri(evs_vox) 0\n\n")
                            scriptFile.write("# Number of contrasts\nset fmri(ncon_orig) "+str(CondLen)+"\nset fmri(ncon_real) "+str(CondLen)+"\n\n")
                            scriptFile.write("# Number of F-tests\nset fmri(nftests_orig) 0\nset fmri(nftests_real) 0\n\n")
                            scriptFile.write("# Add constant column to design matrix? (obsolete)\nset fmri(constcol) 0\n\n")
                            scriptFile.write("# Carry out post-stats steps?\nset fmri(poststats_yn) 1\n\n")
                            scriptFile.write("# Pre-threshold masking?\nset fmri(threshmask) \"\"\n\n")

                            # Clustering
                            scriptFile.write("# Thresholding\n# 0 : None\n# 1 : Uncorrected\n# 2 : Voxel\n# 3 : Cluster\nset fmri(thresh) 3\n\n")
                            scriptFile.write("# P threshold\nset fmri(prob_thresh) " + str(setting.CTPT) + "\n\n")

                            scriptFile.write("# Z threshold\nset fmri(z_thresh) " + str(setting.CTZT) + "\n\n")
                            scriptFile.write("# Z min/max for colour rendering\n# 0 : Use actual Z min/max\n# 1 : Use preset Z min/max\nset fmri(zdisplay) 0\n\n")
                            scriptFile.write("# Z min in colour rendering\nset fmri(zmin) 2\n\n")
                            scriptFile.write("# Z max in colour rendering\nset fmri(zmax) 8\n\n")
                            scriptFile.write("# Colour rendering type\n# 0 : Solid blobs\n# 1 : Transparent blobs\nset fmri(rendertype) 1\n\n")
                            scriptFile.write("# Background image for higher-level stats overlays\n# 1 : Mean highres\n# 2 : First highres\n# 3 : Mean functional\n# 4 : First functional\n# 5 : Standard space template\nset fmri(bgimage) 1\n\n")
                            scriptFile.write("# Create time series plots\nset fmri(tsplot_yn) 1\n\n")
                            scriptFile.write("# Registration to initial structural\nset fmri(reginitial_highres_yn) 0\n\n")
                            scriptFile.write("# Search space for registration to initial structural\n# 0   : No search\n# 90  : Normal search\n# 180 : Full search\nset fmri(reginitial_highres_search) 90\n\n")
                            scriptFile.write("# Degrees of Freedom for registration to initial structural\nset fmri(reginitial_highres_dof) 3\n\n")

                            # Anat
                            if setting.Anat:
                                scriptFile.write("# Registration to main structural\nset fmri(reghighres_yn) 1\n\n")
                                scriptFile.write("# Search space for registration to main structural\n# 0   : No search\n# 90  : Normal search\n# 180 : Full search\nset fmri(reghighres_search) 90\n\n")
                                scriptFile.write("# Degrees of Freedom for registration to main structural\nset fmri(reghighres_dof) 12\n\n")

                            else:
                                scriptFile.write("# Registration to main structural\nset fmri(reghighres_yn) 0\n\n")
                                scriptFile.write("# Search space for registration to main structural\n# 0   : No search\n# 90  : Normal search\n# 180 : Full search\nset fmri(reghighres_search) 90\n\n")
                                scriptFile.write("# Degrees of Freedom for registration to main structural\nset fmri(reghighres_dof) BBR\n\n")

                            # Standard Space
                            scriptFile.write("# Registration to standard image?\nset fmri(regstandard_yn) 1\n\n")
                            scriptFile.write("# Use alternate reference images?\nset fmri(alternateReference_yn) 0\n\n")

                            # Get {FSLDIR}
                            #StandardTemp = os.path.dirname(os.path.realpath(__file__)) + "/MNI152_T1_2mm_brain"
                            scriptFile.write("# Standard image\nset fmri(regstandard) \"" + setting.MNISpace + "\"\n\n")

                            scriptFile.write("# Search space for registration to standard space\n# 0   : No search\n# 90  : Normal search\n# 180 : Full search\nset fmri(regstandard_search) 90\n\n")
                            scriptFile.write("# Degrees of Freedom for registration to standard space\nset fmri(regstandard_dof) 12\n\n")
                            scriptFile.write("# Do nonlinear registration from structural to standard space?\nset fmri(regstandard_nonlinear_yn) 0\n\n")
                            scriptFile.write("# Control nonlinear warp field resolution\nset fmri(regstandard_nonlinear_warpres) 10\n\n")

                            # High Pass
                            scriptFile.write("# High pass filter cutoff\nset fmri(paradigm_hp) %d\n\n" % setting.HighPass)


                            # Total Voxel

                            TotalVoxel = MRIFile.get_shape()[0] * MRIFile.get_shape()[1] * MRIFile.get_shape()[2] * MRIFile.get_shape()[3]
                            scriptFile.write("# Total voxels\nset fmri(totalVoxels) " + str(TotalVoxel) + "\n\n\n")

                            scriptFile.write("# Number of lower-level copes feeding into higher-level analysis\nset fmri(ncopeinputs) 0\n\n")
                            scriptFile.write("# 4D AVW data or FEAT directory (1)\nset feat_files(1) \"" + BOLDaddr + "\"\n\n")
                            scriptFile.write("# Add confound EVs text file\nset fmri(confoundevs) 0\n\n")
                            if setting.Anat:
                                AnatAddr = setParameters3(setting.BET,setting.mainDIR, fixstr(s, setting.SubLen, setting.SubPer),"",setting.Task,\
                                                           fixstr(cnt, setting.ConLen, setting.ConPer))

                                scriptFile.write("# Subject's structural image for analysis 1\nset highres_files(1) \"" + AnatAddr + "\"\n\n")

                            # Condition Files
                            for cond in range(1,CondLen + 1):
                                scriptFile.write("# EV " + str(cond) + " title\nset fmri(evtitle"+str(cond)+") \""+Conditions[cond-1][1][0]+"\"\n\n")
                                scriptFile.write("# Basic waveform shape (EV " + str(cond) + ")\n# 0 : Square\n# 1 : Sinusoid\n# 2 : Custom (1 entry per volume)\n# 3 : Custom (3 column format)\n# 4 : Interaction\n# 10 : Empty (all zeros)\nset fmri(shape" + str(cond) + ") 3\n\n")
                                scriptFile.write("# Convolution (EV " + str(cond) + ")\n# 0 : None\n# 1 : Gaussian\n# 2 : Gamma\n# 3 : Double-Gamma HRF\n# 4 : Gamma basis functions\n# 5 : Sine basis functions\n# 6 : FIR basis functions\nset fmri(convolve" + str(cond) + ") 2\n\n")
                                scriptFile.write("# Convolve phase (EV " + str(cond) + ")\nset fmri(convolve_phase" + str(cond) + ") 0\n\n")
                                scriptFile.write("# Apply temporal filtering (EV " + str(cond) + ")\nset fmri(tempfilt_yn" + str(cond) + ") 1\n\n")
                                scriptFile.write("# Add temporal derivative (EV " + str(cond) + ")\nset fmri(deriv_yn" + str(cond) + ") 0\n\n")
                                ConditionFile =  setParameters3(setting.EventFolder,setting.mainDIR, fixstr(s, setting.SubLen,setting.SubPer), \
                                                                                fixstr(r, setting.RunLen, setting.RunPer), setting.Task,\
                                                           fixstr(cnt, setting.ConLen, setting.ConPer)) + setting.CondPre + "_" +  str(cond) + ".tab"
                                scriptFile.write("# Custom EV file (EV " + str(cond) + ")\nset fmri(custom" + str(cond) + ") \"" + ConditionFile + "\"\n\n")
                                scriptFile.write("# Gamma sigma (EV " + str(cond) + ")\nset fmri(gammasigma" + str(cond) + ") 3\n\n")
                                scriptFile.write("# Gamma delay (EV " + str(cond) + ")\nset fmri(gammadelay" + str(cond) + ") 6\n\n")
                                for ev in range(0,CondLen + 1):
                                    scriptFile.write("# Orthogonalise EV " + str(cond) + " wrt EV " + str(ev) + "\nset fmri(ortho" + str(cond) + "." + str(ev) + ") 0\n\n")

                            scriptFile.write("# Contrast & F-tests mode\n# real : control real EVs\n# orig : control original EVs\nset fmri(con_mode_old) orig\nset fmri(con_mode) orig\n\n")
                            # Contrast & F-tests mode
                            for cond in range(1,CondLen + 1):
                                scriptFile.write("# Display images for contrast_real " + str(cond) + "\nset fmri(conpic_real." + str(cond) + ") 1\n\n")
                                scriptFile.write("# Title for contrast_real " + str(cond) + "\nset fmri(conname_real." + str(cond) + ") \"" + Conditions[cond-1][1][0] + "\"\n\n")
                                for ev in range(1, CondLen + 1):
                                    if ev == cond:
                                        scriptFile.write("# Real contrast_real vector " + str(cond) + " element " + str(ev) + "\nset fmri(con_real" + str(cond) + "." + str(ev) + ") " + str(CondLen) + "\n\n")
                                    else:
                                        scriptFile.write("# Real contrast_real vector " + str(cond) + " element " + str(ev) + "\nset fmri(con_real" + str(cond) + "." + str(ev) + ") -1\n\n")

                            for cond in range(1,CondLen + 1):
                                scriptFile.write("# Display images for contrast_orig " + str(cond) + "\nset fmri(conpic_orig." + str(cond) + ") 1\n\n")
                                scriptFile.write("# Title for contrast_orig " + str(cond) + "\nset fmri(conname_orig." + str(cond) + ") \"" + Conditions[cond-1][1][0] + "\"\n\n")
                                for ev in range(1, CondLen + 1):
                                    if ev == cond:
                                        scriptFile.write("# Real contrast_orig vector " + str(cond) + " element " + str(ev) + "\nset fmri(con_orig" + str(cond) + "." + str(ev) + ") " + str(CondLen) + "\n\n")
                                    else:
                                        scriptFile.write("# Real contrast_orig vector " + str(cond) + " element " + str(ev) + "\nset fmri(con_orig" + str(cond) + "." + str(ev) + ") -1\n\n")

                            scriptFile.write("# Contrast masking - use >0 instead of thresholding?\nset fmri(conmask_zerothresh_yn) 0\n\n")
                            scriptFile.write("")

                            for cond in range(1,CondLen + 1):
                                for ev in range(1,CondLen + 1):
                                    if cond != ev:
                                        scriptFile.write("# Mask real contrast/F-test " + str(cond) + " with real contrast/F-test " + str(ev) + "?\nset fmri(conmask" + str(cond) + "_" + str(ev) + ") 0\n\n")

                            scriptFile.write("# Do contrast masking at all?\nset fmri(conmask1_1) 0\n\n")
                            scriptFile.write("##########################################################\n# Now options that don't appear in the GUI\n\n")
                            scriptFile.write("# Alternative (to BETting) mask image\nset fmri(alternative_mask) \"\"\n\n")
                            scriptFile.write("# Initial structural space registration initialisation transform\nset fmri(init_initial_highres) \"\"\n\n")
                            scriptFile.write("# Structural space registration initialisation transform\nset fmri(init_highres) \"\"\n\n")
                            scriptFile.write("# Standard space registration initialisation transform\nset fmri(init_standard) \"\"\n\n")
                            scriptFile.write("# For full FEAT analysis: overwrite existing .feat output dir?\nset fmri(overwrite_yn) 0")

                            scriptFile.close()
                            print("SCRIPT: " + ScriptAddr + " is generated!")