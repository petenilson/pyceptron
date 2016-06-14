'''
A python implementation of:

    'Perceptrons - the most basic form of a neural network'
     https://appliedgo.net/perceptron/
     
'''

import random

try:
    import matplotlib.pyplot as plt
except:
    pass

class Perceptron(object):
    """
    Uses random weights and biases that will me modified
    during the training program. A perceptron must be 
    able to: process input signals.
             adjust the input weights as instructed by 
             the trainer.
    """
    def __init__(self, n):
        
        self.inputs = n
        self.weights = [random.uniform(-1,1) for i in range(n)]
        self.bias = random.uniform(-1,1)
        
    def adjust(self, inputs, delta, learning_rate):
        """
        During the learning phase, the perceptron adjusts
        the weights and bias based on how much the answer
        differs from the correct answer
        """
        self.weights = [self.weights[i] + inputs[i]*delta*learning_rate for i in range(len(self.weights))]
        self.bias += delta*learning_rate

    def process(self, inputs):
        """
        The core functionality of the perceptron. Weighs the 
        input signals, sums them up, add the bias, the returns
        the value via the heaviside step function. 
        """
        w_inputs = [inputs[i]*float(self.weights[i]) for i in range(len(inputs))]
        sum_and_bias = sum(w_inputs) + self.bias
        
        return self.heaviside(sum_and_bias)
        
    def heaviside(self, _input):
        """
        This is the Heaviside Step Function.
        A Heaviside Step Function returns 1 if the input
        is greater or equal to zero, otherwise if the input
        is negative it returns 0.
        """
        if float(_input) >= 0:
            return 1
        else:
            return 0

def f(x):
    """
    The equation of a straight line. Checking whether a point
    is above or bellow the line now is very easy. For a point
    (x, y), if the value y is larger than the result of f(x),
    then (x, y) is above the line.
    """
    return a*x + b

def is_above(point):
    """
    Takes a tuple as an input
    Returns 1 if the point (x,y) is above the line y = ax+b.
    """
    x = point[0]
    y = point[1]
    
    if y > f(x):
        return 1
    else: return 0
    

def train(trials, training_rate, perceptron):
    for i in range(trials):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        
        point = (x,y)
        
        result = perceptron.process(point)
        expected = is_above(point)
        delta = expected - result
        p.adjust(point, delta, training_rate)
        

def verify(perceptron):
    """
    Test our models predictions over many trials
    and return a % of correct answers
    """
    # Keep track of our perceptrons correct guesses
    correct_answers = 0
    try: # If matplotlib is not installed
        fig = plt.figure(figsize=(10,6))
    except NameError:
        pass
    
    test_count = 1000 # increase or decrease for more/less tests
    
    for i in range(test_count):
        x = random.randint(-100,100)
        y = random.randint(-100,100)
        point = (x, y)
        
        result = perceptron.process(point)
        
        if is_above(point) == result:
            correct_answers +=1
            try: # If matplotlib is not installed
                correct = plt.scatter(x, y,c='#24bc00', alpha=.7, label='Correct')
            except NameError:
                pass
        else:
            incorrect = plt.scatter(x, y, c='#d40000', alpha=.7, label='Incorrect')
            
    try: # If matplotlib is not installed
        plt.legend((correct, incorrect),('correct guesses ', 'incorrect guesses  '),
                   loc='lower left',scatterpoints=1, ncol=1, fontsize=12)
        plt.show()
    except NameError:
        pass
    return (float(correct_answers)/test_count)*100



if __name__ == '__main__':
    
    # Set a, the gradient of the line between -5 and 5
    # Set b, the offset between -50 and 50
    a = random.randint(-5,5)
    b = random.randint(-50,50)
    
    # Set up our number of iterations to train our perceptron 
    # on and the the training rate.
    iterations = 1000
    learning_rate = 0.1
    
    # Create and train our perceptron
    p = Perceptron(2)
    train(iterations, learning_rate, p)
    
    success = verify(p)
    success_percent = (float(success)/iterations)*100
    
    print 'Trained our perceptron over {} iterations'.format(iterations)
    print 'using a learning rate of {}'.format(learning_rate)
    print '{}% of the answers were correct'.format(success)


