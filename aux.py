import numpy as np

# function to separate dataset into mini batches
def create_mini_batches(X, y, batch_size, n_inputs, n_outputs): 
    X = X.reshape(-1, n_inputs)
    y = y.reshape(-1, n_outputs)
    mini_batches = [] 
    data = np.hstack((X, y)) 
    np.random.shuffle(data) 
    n_minibatches = data.shape[0] // batch_size 
    i = 0
    for i in range(n_minibatches + 1): 
        mini_batch = data[i * batch_size:(i + 1)*batch_size, :] 
        X_mini = mini_batch[:, :-1] 
        Y_mini = mini_batch[:, -1].reshape((-1)) 
        mini_batches.append((X_mini, Y_mini)) 
    if data.shape[0] % batch_size != 0: 
        mini_batch = data[i * batch_size:data.shape[0]] 
        X_mini = mini_batch[:, :-1] 
        Y_mini = mini_batch[:, -1].reshape((-1)) 
        mini_batches.append((X_mini, Y_mini)) 
    return mini_batches 