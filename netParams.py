from netpyne import specs, sim
from neuron import h

try:
	from __main__ import cfg  # import SimConfig object with params from parent module
except:
	from cfg import cfg  # if no simConfig in parent module, import directly from tut8_cfg module

import random
# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters


################################################################################################
## Population parameters
################################################################################################
netParams.sizeX = 100 # x-dimension (horizontal length) size in um
netParams.sizeY = 1000 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 100 # z-dimension (horizontal length) size in um

#netParams.popParams['S'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}
#netParams.popParams['M'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}

#netParams.popParams['CN'] = {'cellType': 'CN', 'numCells': 1, 'cellModel': 'HH'}
#netParams.defaultThreshold = -10.0
netParams.popParams['TC'] = {'cellType': 'TC_cell', 'numCells': 1, 'yRange': [100,300], 'cellModel': 'HH'}


#spkTimes = [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 850]

#spkTimes = [3.3, 19.8, 34.8, 45.65, 58.4, 74.85, 88.15, 103.25, 113.65, 125.6, 139.3, 149.3, 163.2, 180.5, 195.35, 208.9, 221.95, 233.4, 244, 249.55, 260.3, 271.5, 295.5, 309.3, 322.45, 335.9, 347.9, 364.2, 379.15, 395.5, 407.8, 425.8, 438.5, 452.7, 467.7, 482.35, 500.4, 509.2, 523.3, 541.1, 551.35, 572, 584.55, 594.5, 607.6, 624.7, 647.2, 659.5, 668.5, 679.2, 688.4, 701.2, 711.8, 732.3, 742.5, 758.9, 777.7, 793.3, 801.5, 822.5, 833.3, 842.6, 853.6, 871.6, 884.8, 895.7, 916.7, 928.1, 940, 952.8, 968.4, 980.9, 994.05, 1200]
#200MS PAUSE
#spkTimes = [3.3, 19.8, 34.8, 45.65, 58.4, 74.85, 88.15, 103.25, 113.65, 125.6, 139.3, 149.3, 163.2, 180.5, 195.35, 208.9, 221.95, 233.4, 244, 249.55, 260.3, 271.5, 295.5, 309.3, 322.45, 335.9, 347.9, 364.2, 379.15, 395.5, 407.8, 425.8, 438.5, 452.7, 467.7, 482.35, 500.4, 509.2, 523.3, 541.1, 551.35, 572, 584.55, 594.5, 607.6, 624.7, 647.2, 659.5, 668.5, 679.2, 688.4, 701.2, 711.8, 732.3, 742.5, 758.9, 777.7, 793.3, 801.5, 822.5, 833.3, 842.6, 853.6, 871.6, 884.8, 895.7, 916.7, 928.1, 940, 952.8, 968.4, 980.9, 994.05, 1200, 1208.9, 1221.95, 1233.4, 1244, 1249.55, 1260.3, 1271.5, 1295.5]
#100MS PAUSE
spkTimes = [503.3, 519.8, 534.8, 545.65, 558.4, 574.85, 588.15, 603.25, 613.65, 625.6, 639.3, 649.3, 663.2, 680.5, 695.35, 708.9, 721.95, 733.4, 744, 749.55, 760.3, 771.5, 795.5, 809.3, 822.45, 835.9, 847.9, 864.2, 879.15, 895.5, 907.8, 925.8, 938.5, 952.7, 967.7, 982.35, 1000.4, 1009.2, 1023.3, 1041.1, 1051.35, 1072, 1084.55, 1094.5, 1107.6, 1124.7, 1147.2, 1159.5, 1168.5, 1179.2, 1188.4, 1201.2, 1211.8, 1232.3, 1242.5, 1258.9, 1277.7, 1293.3, 1301.5, 1322.5, 1333.3, 1342.6, 1353.6, 1371.6, 1384.8, 1395.7, 1416.7, 1428.1, 1440, 1452.8, 1468.4, 1480.9, 1494.05, 16100, 1603.25, 1613.65, 1625.6, 1639.3, 1649.3, 1663.2, 1680.5]

pulses = [{'start': 500, 'end': 1500, 'rate': 100, 'noise': 1}, {'start': 1700, 'end': 2700, 'rate': 100, 'noise': 1}, {'start': 2800, 'end': 5000, 'rate': 100, 'noise': 1}]



#netParams.popParams['artif_CN_sync'] = {'pop': 'artif_CN_sync', 'cellModel': 'VecStim', 'numCells': 2,'yRange': [300,600], 'spkTimes': spkTimes}  #'noise': 1'noise': 0.5
netParams.popParams['artif_CN_sync'] = {'pop': 'artif_CN_sync', 'cellModel': 'VecStim', 'numCells': 2,'yRange': [300,600], 'spkTimes': spkTimes, 'pulses': pulses}  #'noise': 1'noise': 0.5


#netParams.popParams['artif_CN'] = {'pop': 'artif_CN', 'cellModel': 'NetStim', 'numCells': 1, 'start': 100, 'number': 10, 'interval': 20, 'noise': 0 }  #'noise': 1'noise': 0.5

netParams.popParams['artif_CN_desync'] = {'pop': 'artif_CN_desync', 'cellModel': 'NetStim', 'interval': 10, 'numCells': 4, 'start': 500, 'noise': 1}  #'noise': 1'noise': 0.5



################################################################################################
## Cell property rules
################################################################################################

#cellRule = netParams.importCellParams(label = 'CN', conds = {'pop': 'CN'} , fileName = 'import_swc_CN.py', cellName = 'MakeCell', importSynMechs=True)

cellRule = netParams.importCellParams(label = 'TC_cell', conds = {'pop': 'TC'} , fileName = 'import_swc_TC.py', cellName = 'MakeCell', importSynMechs=True)
#cellRule = netParams.importCellParams(label = 'CA_229hoc', conds = {'pop': 'CA_229hoc'} , fileName = 'cells/CA_229.hoc', cellName = '', importSynMechs=False)


#cellRule = {'conds': {'cellType': 'PYR'},  'secs': {}} 	# cell rule dict, make an new matrix called secs, in which the data will be spit
#cellRule['secs']['soma'] = {'geom': {}, 'mechs': {}}  														# soma params dict
#cellRule['secs']['soma']['geom'] = {'diam': 18.8, 'L': 18.8, 'Ra': 123.0}  			# big dictionary with all the values we want to add into the model						# soma geometry
#cellRule['secs']['soma']['mechs']['hh'] = {'gnabar': 0.12, 'gkbar': 0.036, 'gl': 0.003, 'el': -70}  		# soma hh mechanism
#netParams.cellParams['PYRrule'] = cellRule  
												# add dict to list of cell params



################################################################################################
# Stimulation parameters
################################################################################################

#netParams.stimSourceParams['TC_bkg'] = {'type': 'NetStim', 'interval': '50', 'start': 500, 'noise': 0} #ms  nA
#netParams.stimTargetParams['pulse->TC'] = {'source': 'TC_bkg', 'conds': {'cellType': 'TC_cell'}, 'sec':'soma_0', 'loc':0.5}


#netParams.stimSourceParams['CB_syn'] = {'type': 'AlphaSynapse', 'onset': 'uniform(300,600)', 'tau': 5, 'gmax': 'post_ynorm', 'e': 0}
#netParams.stimTargetParams['CB_syn->TC'] = {'source': 'CB_syn', 'sec':'soma', 'loc': 0.5, 'conds': {'pop':'TC'}}

#netParams.stimSourceParams['pulse_TC'] = {'type': 'IClamp', 'del':200, 'dur':200, 'amp':-0.5} #ms  nA
#netParams.stimTargetParams['pulse->TC'] = {'source': 'pulse_TC', 'conds': {'cellType': 'TC_cell'}, 'sec':'soma_0', 'loc':0.5}

#netParams.stimSourceParams['pulse_CN_IClamp'] = {'type': 'IClamp', 'del':1000, 'dur':3, 'amp':5} #ms  nA
#netParams.stimTargetParams['pulse->CN'] = {'source': 'pulse_CN_IClamp', 'conds': {'cellType': 'CN'}, 'sec':'soma_0', 'loc':0.5}

#spkTimes = [138, 155, 270]
#netParams.stimSourceParams['pulse_CN'] = {'type': 'NetStim', 'interval': 20, 'number': 50, 'start': 500, 'noise': 0.5} # 
#netParams.stimSourceParams['pulse_CN'] = {'type': 'VecStim', 'SpkTime': spkTimes} # 

#netParams.stimTargetParams['pulse->CN'] = {'source': 'pulse_CN', 'conds': {'cellType': 'CN'}, 'sec':'soma_0', 'loc':0.5}
#netParams.stimTargetParams['pulse_CN->CN'] = {'source': 'pulse_CN', 'conds': {'cellType': 'CN'}, 'weight': 0.001, 'delay': 100, 'synMech': 'exc'}
#netParams.stimSourceParams['Input_4'] = {'type': 'NetStim', 'interval': 'uniform(20,100)', 'number': 1000, 'start': 600, 'noise': 0.1}




################################################################################################
## Synaptic mechanism parameters, most of them get imported from somewhere else
################################################################################################

#netParams.synMechParams['exc'] = {'mod': 'Exp2Syn', 'tau1': 0.35, 'tau2': 5, 'e': 0}  # excitatory exponential synaptic mechanism, i = synaptic current in nA, tau1 = rise time, tau2 = decay time, e = synaptic reversal potential
#netParams.synMechParams['inh'] = {'mod': 'Exp2Syn', 'tau1': 0.6, 'tau2': 8.5, 'e': -75}  # GABA synaptic mechanism
#netParams.synMechParams['depSyn'] = {'mod': 'Recov2Exp', 'e': 0, 'tau': 1, 'k': 0.05, 'tau_rec': 80, 'U': 0.5, }  #'tau_rec': 80 depressing excitatory exponential synaptic mechanism, from Rudnicki and Hemmert 2017 'High entrainment constrains synaptic depression in a globular bushy cell'
netParams.synMechParams['depSyn'] = {'mod': 'Recov2Exp', 'e': 0, 'tau': 1, 'k': 0.1, 'tau_fast': 0.05, 'tau_slow': 100, 'U': 0.5}  #

################################################################################################
## Cell connectivity rules0
################################################################################################
                 #number of synapses
 
                 #number of synapses 
#number = h.Random()
netParams.connParams['CN1->TC'] = { 	#  S -> M label
	'preConds': {'pop': ['artif_CN_desync', 'artif_CN_sync']}, 	# conditions of presyn cells
	#'preConds': {'pop': 'artif_CN_sync'}, 
    'postConds': {'pop': 'TC'}, # conditions of postsyn cells
	'probability': 1, 			# probability of connection
	'weight': 0.001,            		# synaptic weight
	'delay': 0,						# transmission delay (ms)
	'synMech': 'depSyn',      #synaptic mechanism
     #'sec': ['dend_0', dend_1, dend_2, dend_3, dend[4], dend[5], dend[6], dend[7], dend[8], dend[9], dend[10], dend[11], dend[12], dend[13], dend[14], dend[15], dend[16], dend[17], dend[18], dend[19], dend[20], dend[21], dend[22], dend[23], dend[24], dend[25], dend[26], dend[27], dend[28], dend[29], dend[30], dend[31], dend[32], dend[33], dend[34], dend[35], dend[36], dend[37], dend[38], dend[39], dend[40], dend[41], dend[42], dend[43], dend[44], dend[45], dend[46], dend[47], dend[48], dend[49], dend[50], dend[51], dend[52], dend[53], dend[54], dend[55], dend[56], dend[57], dend[58], dend[59], dend[60], dend[61], dend[62], dend[63], dend[64], dend[65], dend[66], dend[67], dend[68], dend[69], dend[70], dend[71], dend[72], dend[73], dend[74], dend[75], dend[76], dend[77], dend[78], dend[79], dend[80], dend[81], dend[82], dend[83], dend[84], dend[85], dend[86], dend[87], dend[88], dend[89], dend[90], dend[91], dend[92], dend[93], dend[94], dend[95], dend[96], dend[97], dend[98], dend[99], dend[100], dend[101], dend[102], dend[103], dend[104], dend[105], dend[106], dend[107], dend[108], dend[109], dend[110], dend[111], dend[112], dend[113], dend[114], dend[115], dend[116], dend[117], dend[118], dend[119], dend[120], dend[121], dend[122], dend[123], dend[124], dend[125], dend[126], dend[127], dend[128], dend[129], dend[130], dend[131], dend[132], dend[133], dend[134]],# for several enter dendrites, each section is plotted 
     #'sec': h.dend(),
     #'sec': ['dend_1', 'dend_130'],
     'sec': (["dend_"+str(num) for num in range(1,137)]),
     'loc': 'uniform(0.1,0.9)',                  #location of synapses that make a connection
     'synsPerConn': 5}                  #number of synapses'
 

