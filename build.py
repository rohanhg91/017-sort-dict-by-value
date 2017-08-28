import operator


def solution_asc(dic):
    '''
    Enter your code here
    '''
    op = []
    for i in range (0, len(dic)):
        for k, v in dic.iteritems():
            output = (k,v)
            op.append(output)
        return op


def solution_desc(dic):
    '''
    Enter your code here
    '''
    op = []
    for i in range (0, len(dic)):
        for k, v in dic.iteritems():
            output = (k,v)
            op.append(output)
        op1 = op[::-1]
        return op1

'''
dic = {2: 21, 1: 11, 0: 12, 9: 211, 4: 55}
a = solution_desc(dic)
print a
'''
