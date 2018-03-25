from collections import defaultdict
from itertools import permutations

class Neuron(defaultdict):
    def __init__(self, name, threshold=0.5):
        self.name = name
        self.voltage = 0
        self.threshold = threshold
        self._active = False

    def time(self):
        if self.voltage > self.threshold:
            self._active = True
            self.voltage = 0
            
    def activate(self):
        self._active = True
        self.voltage = 0

    def is_active(self):
        return self._active

class Brain():
    def __init__(self, a_stdp=0.001):
        self.node = dict()
        self.weights = dict()
        self.a_stdp = a_stdp

    def receive(self, word):
        if not self.node.get(word):  # there is no neuron for that word
            self.node[word] = Neuron(word)
        else:
            self.node[word].activate()

    def time(self):
        active_neurons = [x for x in self.node.values() if x.is_active()]
        for weight in permutations(active_neurons, 2):
            self.weights[weight] += self.a_stdp

        for ((pre, post), weight) in self.weights.iteritems():
            if pre in active_neurons:
                post.voltage += weight

        for neuron in self.node.values():
            neuron.time()

class World():
    def __init__(self):
        self.brains = dict()
        self.knowledge_bases = dict()

    def add_brain(self, name, *args, **kwargs):
        self.brains[name] = Brain(*args, **kwargs)

    def remove_brain(self, name):
        del self.brains[name]

    def connect_knowledge_base(self, path, brain_name):
        self.knowledge_bases[brain_name] = path

    def run(self):
        for name, brain in self.brains.iteritems():
            if self.knowledge_bases.get(name):
                brain.time()
    
