from liblinearutil import *
import numpy as np



# Construct problem in python format
# Dense data

y, x = [1,-1,2,1], [[1,0,1], [-1,0,-1],[0,0,0],[1,2,3]]
print len(x)
print len(y)



prob  = problem(y, x)
param = parameter('-s 7 -c 4 -B 1')
m = train(prob, param)

# Other utility functions
save_model('heart_scale.model', m)
m = load_model('heart_scale.model')
x=[[1,1,1],[2,3,5],[-1,0,-1],[1,1,1],[0,0,0]]
y = [0] * len(x) #unknown labels, put the real labels if you want to 

p_label, p_acc, p_val = predict(y, x, m, '-b 1')
print p_label
print p_acc
print p_val
#ACC, MSE, SCC = evaluations(y, p_label)

