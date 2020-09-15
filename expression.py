class Variable (object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __mul__(self, x):
        if type(x) in [int, Variable, float]:
            return Term([self,x])
        elif type(x) == Term:
            return Term([self] + x.nom.copy(), x.dem.copy())

    def __truediv__(self, x):
        if type(x) in [int, Variable, float]:
            return Term([self], [x])
        elif type(x) == Term:
            return Term([self] + x.den.copy(), x.nom.copy())

class Term (object):
    def __init__(self, nom=[], den=[]):
        self.nom = nom
        self.den = den

    def __str__(self):
        str_nom = "("
        str_den = "("
        for i in self.nom:
          str_nom += str(i)
        str_nom += ")"
        for i in self.den:
          str_den += str(i)
        str_den += ")"
        return str_nom + "/" + str_den

    def __repr__(self):
        return self.__str__()

    def mul(self, x):
        t = Term()
        t.nom = [i for i in self.nom]
        t.den = [i for i in self.den]
        if type(x) in [int, Variable, float]:
          t.nom.append(x)
        elif type(x) is Term:
          t.nom += x.nom
          t.den += x.den
        else:
          raise TypeError()
        return t

    def __mul__(self, x):
        return self.mul(x)

    def div(self, x):
        t = Term()
        t.nom = [i for i in self.nom]
        t.den = [i for i in self.den]
        if type(x) in [int, Variable, float]:
          t.den.append(x)
        elif type(x) is Term:
          t.den += x.nom
          t.nom += x.den
        else:
          raise TypeError()
        return t

    def __truediv__(self, x):
        return self.div(x)

    #def copy(self):


class Expression (object):
    def __init__(self, nom=[], den=[]):
        self.nom = nom
        self.den = den

    def __str__(self):
        str_nom = "("
        str_den = ""
        for i, j in enumerate(self.nom):
          str_nom += str(j)
          if i != len(self.nom) - 1:
            str_nom += " + "
        for i, j in enumerate(self.den):
          str_den += str(j)
          if i != len(self.den) - 1:
            str_den += " + "
        str_nom += ")"
        str_den += ")"
        return str_nom + "/" + str_den

    def __repr__(self):
        return str(self)

    #def __add__(self):
        #for i in self.den:
