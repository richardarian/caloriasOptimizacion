#! /usr/bin/python3
import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory
#asdasdasd as
model = pyo.ConcreteModel()
i = ['malanga', 'platano']
j = [30, 42]
cantidad = {'malanga': 25, 'platano': 50}

model.i = pyo.Set(initialize=i, doc='Productos')
model.j = pyo.Set(initialize=j, doc='Calorias')
# Variables
x = model.x = pyo.Var(model.i, bounds=(0.0, None), doc='Cantidad')
h = model.h = pyo.Var(model.i, bounds=(0.0, None), doc='Hectareas')
# Parametros
cantidadP = model.cantidadP = pyo.Param(i, initialize=cantidad, default=0)


def FO(model):
    return sum(model.x[n]*model.cantidadP[n] for n in cantidad)


model.obj = pyo.Objective(rule=FO)


model.pprint()
