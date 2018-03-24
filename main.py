from collections import defaultdict

class Neuron(defaultdict):
    def __init__(self, name):
        self.name = name
        self.voltage = 0
        
class Brain():
    def __init__(self, init_knowledge_base):
        self.node = dict()
        sentences = tools.SentenceGrabber('data/wikipedia')
        for word in tools.newsha(init_knowledge_base):
            self.receive(word)

    def receive(self, word):
        if not node.get(word):  # there is no neuron for that word
            self.node[word] = Neuron(word)
        else:
            self.node[word].activate()

    def time(self):
        active_neurons = [x for x in self.node.values() if x.is_active()]
