"""
Le premier prgramme en Python
@author Alexandra Dobrescu
@date 09.03.2017
"""

def dites_bonjour(personne):
    print "Bonjour " + personne + " !"

if __name__ == "__main__":
    import sys
    dites_bonjour(sys.argv[1])
