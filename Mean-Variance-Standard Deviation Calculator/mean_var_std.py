import numpy as np

def calculate(list):
    if(len(list) != 9):
        raise ValueError('List must contain nine numbers.')
        
    calculations = {
      'mean': [],
      'variance': [],
      'standard deviation': [],
      'max': [],
      'min': [],
      'sum': []
    }
        
    # create a 3x3 matrix
    npArr = np.array(list)
    mat = np.array([list[0:3], list[3:6], list[6:]])
    
    # mean calculations
    meanAxisCol = mat.mean(axis=0).tolist()
    meanAxisRow = mat.mean(axis=1).tolist()
    meanFlat = npArr.mean()
    calculations['mean'] = [meanAxisCol,meanAxisRow, meanFlat]
    
    # variance calculations
    varAxisCol = mat.var(axis=0).tolist()
    varAxisRow = mat.var(axis=1).tolist()
    varFlat = npArr.var()
    calculations['variance'] = [varAxisCol, varAxisRow, varFlat]
    
    # standard deviation calculations
    stdAxisCol = mat.std(axis=0).tolist()
    stdAxisRow = mat.std(axis=1).tolist()
    stdFlat = npArr.std()
    calculations['standard deviation'] = [stdAxisCol, stdAxisRow, stdFlat]
    
    # max calculations
    maxAxisCol = mat.max(axis=0).tolist()
    maxAxisRow = mat.max(axis=1).tolist()
    maxFlat = npArr.max()
    calculations['max'] = [maxAxisCol, maxAxisRow, maxFlat]
    
    # min calculations
    minAxisCol = mat.min(axis=0).tolist()
    minAxisRow = mat.min(axis=1).tolist()
    minFlat = npArr.min()
    calculations['min'] = [minAxisCol, minAxisRow, minFlat]
    
    # sum calculations
    sumAxisCol = mat.sum(axis=0).tolist()
    sumAxisRow = mat.sum(axis=1).tolist()
    sumFlat = npArr.sum()
    calculations['sum'] = [sumAxisCol, sumAxisRow, sumFlat]
    
    return calculations