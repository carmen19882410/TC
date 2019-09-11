
#%%



#import neuron
#import neuron.hoc
#import neuron.hclass3
#import neuron.psection
#import cfg


from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg.py', netParamsDefault='netParams.py')					

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)


#import numpy as np
#import matplotlib.pyplot as plt

#spkid = np.array(sim.simData['spkid'].to_python())
#spkt = np.array(sim.simData['spkt'].to_python())

#_, ax = plt.subplots()
#ax.plot(spkt, spkid, '|')

# only stimulus
#stimt = spkt[spkid==1] #select the spkt which have the spkid 1.
#_, ax = plt.subplots()
#ax.plot(stimt, np.ones(stimt.size), '|') # 'I' is the marker line

# the same result with a different method
#stimt = []
#for i, spikes in enumerate(spkt):
#    if spkid[i]==1:
#        stimt.append(spikes)f

#_, ax = plt.subplots()
#ax.plot(stimt, np.ones(stimt.size), '|')
        
        
