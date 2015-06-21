# Done by FerranAlet, 17/6/15
# !/usr/bin/env python3

"""
In this code I try to obtain all the statistics (regarding rating) of every participant in a list of contests
WARNING: a little bit inefficient
"""

import os
import sys

from codeforces import CodeforcesAPI


def main(argv):
    #llistat = [341,343,346,348,351,354,356,360,364,367,372,375,377,380,383,388,403,406,407,414,418,420,425,429,434,438,442]; #Div1contests
    #llistat = [379, 436, 325, 316, 241] #Div1&2contests
    #llistat = [549]; #LookseryCup
    llistat = [447,448,450,451,454,456,459,460,462,463,465,466,467]; #Div2contests.
    f = open('Div2sft.txt', 'w')
    api = CodeforcesAPI()
    for id in llistat:
        llista = list(api.contest_standings(id)['rows'])
        participa = str(len(llista))
        for p in llista:
            tio = p.party.members[0].handle
            print(str(id)+' '+str(p.rank))
            concursos = api.user_rating(tio)
            cont = 0
            for c in concursos:
                cont = cont+1
                if c.contest_id==id:
                    f.write(str(c.rank)+' '+str(c.old_rating)+' '+str(c.new_rating)+' '+participa+' '+str(cont)+' '+str(id)+'\n')



if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(sys.argv)
    else:
        print("Invalid number of arguments")
        print("Usage: python {} [contest id]".format(os.path.basename(sys.argv[0])))
