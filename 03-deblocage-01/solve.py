'''

Template for France-IOI programming tasks with debugger in gitpod

The Python version on gitpod is 3.11, whereas the python version on france-ioi
is sadly stuck at 3.4.2 ... This means no type hints, no dataclasses, ... The
code should therefore remain pretty basic to run flawlessly on france-ioi

'''

######################## Tests ###############################
try:
    from soiutils import load_test
    load_test('test1')
except:
    pass
######################## Tests ###############################
    
def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''
    problem = {}
    
    nb_livres, nb_jours = [int(x) for x in input().split(' ')]
    
    for _ in range(nb_jours):
        nb_clients = int(input())
        
        for i_client in range(nb_clients):
            
        
    
    print(input())
    
    return problem

def solve(problem):
    result = []
    
    return result
        
    
    
def output(result):
    for r in result:
        print(r)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)