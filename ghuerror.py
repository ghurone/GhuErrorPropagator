import math

from sympy import *
from sympy.parsing.sympy_parser import standard_transformations


class GhuErrorPropagator:
    def __init__(self, expr: str, var: dict) -> None:
        """
            func: funcao em str
            var: {'var': (val_var, inc_var)}
        """
    
        self.func = parse_expr(expr,
                               transformations=standard_transformations)
                               
        self.val = {}
        self.inc = {}

        self.sigma = 0  # inicializador da função

        for _, k in enumerate(var):
            sk = f'sigma_{k}'
            self.val[k] = var[k][0]
            self.inc[sk] = var[k][1]

            if self.inc[sk] > 0:
                self.sigma += (self.func.diff(k) * Symbol(sk)) ** 2 
        
        self.sigma = simplify(sqrt(self.sigma))
        self.resultado = self.sigma.evalf(subs= {**self.val, **self.inc})
        self.valor = self.func.evalf(subs=self.val)	

    def print_func(self):
        pprint(self.func)

    def print_sigma(self):
        pprint(self.sigma)

    def get_latex_func(self):
        return latex(self.func)
    
    def get_latex_sigma(self):
        return latex(self.sigma)

    def resultado_final(self):
        inc = self.resultado
        val = self.valor
	
        sig = - int(math.floor(math.log10(abs(inc))))
        ninc = round(inc, sig)
        nval = round(val, sig)        
        
        if int(ninc) == ninc:
            ninc = int(ninc)
        
        if int(nval) == nval:
            nval = int(nval)        

        return str(nval) + ' ± ' + str(ninc)







