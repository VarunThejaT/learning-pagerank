# toy page rank algorithm
# A -> B
# B -> A, C, D
# C -> D
# D -> A, B

adj_list = {
    "a": ["b"],
    "b": ["a", "c", "d"],
    "c": ["d"],
    "d": ["a", "b"]
}
# at every step with some probability, web surfer will stop surfing
stopping_probability = 0.05
# initial set of seed pages they will visit
initial_seed_pages = ["b", "d"]
# number of iterations to run the algo. It will eventually reach a steady state
num_iterations = 20


page_probabilities = {x: [0, 0] for x in adj_list.keys()}
for seed in initial_seed_pages:
    # assigning 1/len(seeds) helps keep sum of prob = 1 
    # (this is not recommended for universe with large pages, as prob will become
    # exteremely small)
    # Setting two values: [prob for current step, prob for next step]
    page_probabilities[seed] = [1/len(initial_seed_pages), 0] 
def evolve():
    for page, probs in page_probabilities.items():
        curr_prob = probs[0]
        probs[1] += curr_prob * stopping_probability
        adj_pages = adj_list[page]
        for adj_page in adj_pages:
            page_probabilities[adj_page][1] += curr_prob * (1 - stopping_probability) / len(adj_pages)
                
for iteration in range(num_iterations):
    evolve()
    for page, probs in page_probabilities.items():
        page_probabilities[page] = [probs[1], 0]
    # print the probabilities of current pages
    print([x[0] for x in page_probabilities.values()])
# Observations 
# 1. denser the graph (i.e. larger the adjacency list), slower the algo
# 2. larger the stopping_probability, longer it takes to reach the steady state prob
