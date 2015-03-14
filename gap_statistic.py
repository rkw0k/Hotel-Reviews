'''
# Usage example: 

maxK = 5
numK = range(2, maxK + 1)
for K in numK:
    # run multiple K means for data X
    kmeans_model = KMeans(K, init='random', n_init=20, 
                    precompute_distances=False,
                    random_state=1).fit(X)
    
    Y = kmeans_model.labels_

cluster = []
for k in xrange(maxK):
    cluster.append([X[Y==k]])

gap_statistic = gap_statistic(cluster)

'''

def bound_box(cluster):
    '''
    INPUT: List of clusters: cluster[0], cluster[1], ...

    OUTPUT: For each cluster[i], produce arrays xmin[i], xmax[i] that form bounding box containing datapoints
    '''
    xmin, xmax = [], []
    for i in xrange(len(cluster)):
        xmin.append([np.min(cluster[i][:, j]) for j in xrange(len(cluster[i][0]))])
        xmax.append([np.max(cluster[i][:, j]) for j in xrange(len(cluster[i][0]))])
    return xmin, xmax

def get_logW(cluster):
    ''' 
    INPUT: List of clusters: cluster[0], cluster[1], ...

    OUTPUT: Sum of the within-cluster pairwise L2 norms.
    '''
    W = np.sum([np.sum(pdist(cluster[k]) * 0.5) / len(cluster[k]) for k in xrange(K)])
    return np.log(W)

def get_logWB(xmin, xmax):
    '''
    INPUT: List of dimensions forming a bounding box
    
    OUTPUT: The within-box variance and the scaled standard deviation for each cluster.

    Notes:
    Randomly generated data from one cluster. Array of length N of xmin and xmax where xmin[i] < xmax[i] for every i=1,2,...,N
    Returns a box of dimensions (xmin[0], xmax[0]) x ... x (xmin[N-1], xmax[N-1])
    uniformly populated in each dimension with 100 points.
    data_per_cluster = random uniformly points of size=size between xmin[cluster_num][feature_num] and xmax[cluster_num][feature_num]
    '''
    logWB = []
    B = 10 # number of Monte Carlo simulations
    for b in xrange(B):
        # generates Monte Carlo simulations within bounding box
        data_per_cluster = [np.random.uniform(xmin[i], xmax[i], size=100) for i in xrange(len(xmin))]
        logWB.append(np.log(np.sum(pdist(data_per_cluster) * 0.5 / len(data_per_cluster))))
    lbar = np.sum(logWB) / 10.
    stddev = np.sqrt(np.dot(logWB - lbar, logWB - lbar) / B)
    sk = stddev * np.sqrt(1 + 1. / B)
    return lbar, sk

def gap_statistic(cluster):
    xmin, xmax = bound_box(cluster)
    lbar, sk = [],  []
    for k in xrange(K):
        results = get_logWB(cluster[k], xmin[k], xmax[k])
        lbar.append(results[0])
        sk.append(results[1])

    logW = get_logW(cluster)
    gap = [lbar[k] - logW[k] for k in xrange(K)]
    shift_gap = np.array(gap[1:])
    new_gap = np.array(gap[:-1])
    sk = np.array(sk[1:])
    return gap_diff + sk
