from netpyne import specs

# Simulation options
cfg = specs.SimConfig()		# object of class SimConfig to store simulation configuration

cfg.duration = 5000			# Duration of the simulation, in ms
cfg.dt = 0.025 				# Internal integration timestep to use
cfg.verbose = True  			# Show detailed messages
cfg.recordStim = True

#cfg.seeds['stim'] = 1234
# Variable parameters (used in netParams)
#cfg.synMechTau2 = 5
#cfg.connWeight = 1
cfg.hParams.celsius = 34 # change temperature at which sim is made 
cfg.hParams.v_init = -73                #-71.6 # change v init 
cfg.distributeSynsUniformly = True
cfg.connRandomSecFromList = True



cfg.recordCells = ['TC']

#record voltage
cfg.recordTraces = {'V_soma':{'sec':'soma_0', 'loc': 0.5, 'var':'v'}}  # Dict with traces to record
#cfg.recordTraces['V_dend'] = {'sec':'dend_30', 'loc': 0.5, 'var': 'v'} #'synMech': 'Exp2Syn',

#record the synapses
cfg.recordTraces['I_dend'] = {'synMech': 'depSyn', 'var': 'i'} #'synMech': 'Exp2Syn',plot for severeal synapses
#cfg.recordTraces['I_syn'] = {'sec':'dend_31', 'loc': 0.5, 'synMech': 'exc', 'var': 'i'} #'synMech': 'Exp2Syn',
#cfg.recordTraces['I_syn'] = {'sec': 'dend_130', 'loc': 0.5, 'synMech': 'exc', 'var': 'i'} #'synMech': 'Exp2Syn',
#cfg.recordTraces['I_syn'] = {'sec':'dend_31', 'loc': 0.5, 'synMech': 'depSyn', 'var': 'i'} #'synMech': 'Exp2Syn',

#record the individual currents  at soma
#cfg.recordTraces['ina'] = {'sec':'soma_0', 'loc': 0.5, 'mech': 'hh2', 'var': 'ina'}
#cfg.recordTraces['ik'] = {'sec':'soma_0', 'loc': 0.5, 'mech': 'hh2', 'var': 'ik'}
#cfg.recordTraces['gna'] = {'sec':'soma_0', 'loc': 0.5, 'mech': 'hh2', 'var': 'gna'}
#cfg.recordTraces['gk'] = {'sec':'soma_0', 'loc': 0.5, 'mech': 'hh2', 'var': 'gk'}
#cfg.recordTraces['ica'] = {'sec':'soma_0', 'loc': 0.5, 'mech': 'itGHK', 'var': 'ica'}
#cfg.recordTraces['cai'] = {'sec':'soma_0', 'loc': 0.5, 'var': 'cai'} #plots the internal calcium diffusion of the cell, not of the conductances defined in the mod. file

cfg.recordSpikesGids = [0,1]

cfg.recordStep = 0.1 			# Step size in ms to save data (eg. V traces, LFP, etc)
cfg.filename = 'Carmen_mod_swc'  # Set file output name
cfg.saveJson = True 	
cfg.printPopAvgRates = True
#cfg.analysis['plotRaster'] = { 'include': ['artif_CN'], 'saveFig': True} 			# Plot a raster
#cfg.analysis['plotTraces'] = {'include': [0], 'saveFig': True} 
cfg.analysis['plotTraces'] = {'include': [('TC',0)], 'saveFig': True}

# Plot recorded traces for this list of cells, for separate figures 'oneFigPer': 'trace'
#cfg.analysis['plotShape'] = {'includePost': [0], 'includePre': [('artif_CN',0), ('artif_CN', 1)], 'showSyns': True, 'synSiz': 10, 'dist': 1, 'includeAxon': True, 'saveFig': True, 'showFig': True}	
cfg.analysis['plotShape'] = {'includePost': [0], 'includePre': ['all'], 'showSyns': True, 'synSiz': 5, 'dist': 1, 'includeAxon': True, 'saveFig': True, 'showFig': True}	

#plot the morphologz of the network

#plot Rasterplot
cfg.analysis['plotRaster'] = True
cfg.analysis['plotRaster'] = {'orderBy': 'y', 'orderInverse': False, 'saveFig': True} 
#cfg.analysis['plotRaster'] = {'include': [('TC',0), ('artif_CN', 0)],  'saveFig': 'raster.png', 'showFig': True}

cfg.analysis['plot2Dnet'] = True           # plot 2D visualization of cell positions and connections
cfg.analysis['plotConn'] = True           # plot connectivity matrix
