from netpyne import specs, sim

try:
	from __main__ import cfg  # import SimConfig object with params from parent module
except:
	from cfg import cfg  # if no simConfig in parent module, import directly from tut8_cfg module

# Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters


################################################################################################
## Population parameters
################################################################################################


#netParams.popParams['S'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}
#netParams.popParams['M'] = {'cellType': 'PYR', 'numCells': 20, 'cellModel': 'HH'}

#netParams.popParams['CN'] = {'cellType': 'CN', 'numCells': 1, 'cellModel': 'HH'}
#netParams.defaultThreshold = -10.0
netParams.popParams['TC'] = {'cellType': 'TC_cell', 'numCells': 1, 'cellModel': 'HH'}


spkTimes = [500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 900]

#spkTimes = [3.3, 19.8, 34.8, 45.65, 58.4, 74.85, 88.15, 103.25, 113.65, 125.6, 139.3, 149.3, 163.2, 180.5, 195.35, 208.9, 221.95, 233.4, 244, 249.55, 260.3, 271.5, 295.5, 309.3, 322.45, 335.9, 347.9, 364.2, 379.15, 395.5, 407.8, 425.8, 438.5, 452.7, 467.7, 482.35, 500.4, 509.2, 523.3, 541.1, 551.35, 572, 584.55, 594.5, 607.6, 624.7, 647.2, 659.5, 668.5, 679.2, 688.4, 701.2, 711.8, 732.3, 742.5, 758.9, 777.7, 793.3, 801.5, 822.5, 833.3, 842.6, 853.6, 871.6, 884.8, 895.7, 916.7, 928.1, 940, 952.8, 968.4, 980.9, 994.05, 1200]
#200MS PAUSE
#spkTimes = [3.3, 19.8, 34.8, 45.65, 58.4, 74.85, 88.15, 103.25, 113.65, 125.6, 139.3, 149.3, 163.2, 180.5, 195.35, 208.9, 221.95, 233.4, 244, 249.55, 260.3, 271.5, 295.5, 309.3, 322.45, 335.9, 347.9, 364.2, 379.15, 395.5, 407.8, 425.8, 438.5, 452.7, 467.7, 482.35, 500.4, 509.2, 523.3, 541.1, 551.35, 572, 584.55, 594.5, 607.6, 624.7, 647.2, 659.5, 668.5, 679.2, 688.4, 701.2, 711.8, 732.3, 742.5, 758.9, 777.7, 793.3, 801.5, 822.5, 833.3, 842.6, 853.6, 871.6, 884.8, 895.7, 916.7, 928.1, 940, 952.8, 968.4, 980.9, 994.05, 1200, 1208.9, 1221.95, 1233.4, 1244, 1249.55, 1260.3, 1271.5, 1295.5]
#100MS PAUSE
#spkTimes = [503.3, 519.8, 534.8, 545.65, 558.4, 574.85, 588.15, 603.25, 613.65, 625.6, 639.3, 649.3, 663.2, 680.5, 695.35, 708.9, 721.95, 733.4, 744, 749.55, 760.3, 771.5, 795.5, 809.3, 822.45, 835.9, 847.9, 864.2, 879.15, 895.5, 907.8, 925.8, 938.5, 952.7, 967.7, 982.35, 1000.4, 1009.2, 1023.3, 1041.1, 1051.35, 1072, 1084.55, 1094.5, 1107.6, 1124.7, 1147.2, 1159.5, 1168.5, 1179.2, 1188.4, 1201.2, 1211.8, 1232.3, 1242.5, 1258.9, 1277.7, 1293.3, 1301.5, 1322.5, 1333.3, 1342.6, 1353.6, 1371.6, 1384.8, 1395.7, 1416.7, 1428.1, 1440, 1452.8, 1468.4, 1480.9, 1494.05, 16100, 1603.25, 1613.65, 1625.6, 1639.3, 1649.3, 1663.2, 1680.5]

netParams.popParams['artif_CN'] = {'pop': 'artif_CN', 'cellModel': 'VecStim', 'numCells': 1, 'spkTimes': spkTimes}  #'noise': 1'noise': 0.5
#netParams.popParams['artif_CN'] = {'pop': 'artif_CN', 'cellModel': 'NetStim', 'numCells': 1, 'start': 100, 'number': 10, 'interval': 20, 'noise': 0 }  #'noise': 1'noise': 0.5



#netParams.popParams['CA_229hoc'] = {'cellType': 'DET', 'numCells': 1, 'cellModel': 'blank'}



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
netParams.synMechParams['depSyn'] = {'mod': 'RecovExp', 'e': 0, 'tau': 1, 'k': 0.5, 'tau_rec': 50,'U': 0.5, }  # depressing excitatory exponential synaptic mechanism, from Rudnicki and Hemmert 2017 'High entrainment constrains synaptic depression in a globular bushy cell'


################################################################################################
## Cell connectivity rules0
################################################################################################

netParams.connParams['CN->TC'] = { 	#  S -> M label
	'preConds': {'pop': 'artif_CN'}, 	# conditions of presyn cells
	'postConds': {'pop': 'TC'}, # conditions of postsyn cells
	'probability': 1, 			# probability of connection
	'weight': 0.01,            		# synaptic weight
	'delay': 0,						# transmission delay (ms)
	'synMech': 'depSyn',      #synaptic mechanism
     'sec': ['dend_1', 'dend_100', 'dend_50'],# for several enter dendrites, each section is plotted 
     #'sec': 'dend'
     'loc': 0.5,                   #location of synapses that make a connection
     'synsPerConn': 1}                  #number of synapses
 
    



