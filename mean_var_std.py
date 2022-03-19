import numpy as np

def calculate(list):

  calculations={
  'mean': [],
  'variance': [],
  'standard deviation': [],
  'max': [],
  'min': [],
  'sum': []
}
  
  #failure
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  
  #convert to 3x3 array
  a = np.resize(list,(3,3))

  #mean
  calculations['mean'].append(np.average(a,axis=0).tolist())
  calculations['mean'].append(np.average(a,axis=1).tolist())
  calculations['mean'].append(np.average(list).tolist())

  #variance
  calculations['variance'].append(np.var(a,axis=0).tolist())
  calculations['variance'].append(np.var(a,axis=1).tolist())
  calculations['variance'].append(np.var(list).tolist())

  #standard dev
  calculations['standard deviation'].append(np.std(a,axis=0).tolist())
  calculations['standard deviation'].append(np.std(a,axis=1).tolist())
  calculations['standard deviation'].append(np.std(list).tolist())

  #max
  calculations['max'].append(np.amax(a,axis=0).tolist())
  calculations['max'].append(np.amax(a,axis=1).tolist())
  calculations['max'].append(np.amax(list).tolist())

  #min
  calculations['min'].append(np.amin(a,axis=0).tolist())
  calculations['min'].append(np.amin(a,axis=1).tolist())
  calculations['min'].append(np.amin(list).tolist())

  #sum
  calculations['sum'].append(np.sum(a,axis=0).tolist())
  calculations['sum'].append(np.sum(a,axis=1).tolist())
  calculations['sum'].append(np.sum(list).tolist())

  #output

  return calculations