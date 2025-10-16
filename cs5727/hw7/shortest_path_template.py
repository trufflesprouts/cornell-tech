from gurobipy import *

# initialize the data for the problem
noNodes = 8
arcs = [[0 for j in range(noNodes)] for i in range(noNodes)]
arcs[0][1] = 1.0
arcs[0][2] = 2.0
arcs[1][2] = 1.0
arcs[1][3] = 5.0
arcs[1][4] = 2.0
arcs[2][3] = 2.0
arcs[2][4] = 1.0
arcs[2][5] = 4.0
arcs[3][4] = 3.0
arcs[3][5] = 6.0
arcs[3][6] = 8.0
arcs[4][5] = 3.0
arcs[4][6] = 7.0
arcs[5][6] = 5.0
arcs[5][7] = 2.0
arcs[6][7] = 6.0

fromNode = 0
toNode = 7


# create a new model
model = Model("assignment7")

# create decision variables and store them in the array vars
vars = [[0 for i in range(noNodes)] for j in range(noNodes)]
for i in range(noNodes):
    for j in range(noNodes):
        weight = arcs[i][j]
        if weight > 0:
            vars[i][j] = model.addVar(vtype=GRB.CONTINUOUS, name="x_" + str(i) + str(j))

# integrate decision variables into the model
model.update()

# create a linear expression for the objective
objective = LinExpr()
for i in range(noNodes):
    for j in range(noNodes):
        weight = arcs[i][j]
        if weight > 0:
            objective += weight * vars[i][j]
model.setObjective(objective, GRB.MINIMIZE)


# create constraints so that each tech is assigned to one job
for i in range(noNodes):
    constExpr = LinExpr()
    for j in range(noNodes):
        if arcs[i][j] > 0:
            curVar = vars[i][j]
            constExpr += curVar
        if arcs[j][i] > 0:
            curVar = vars[j][i]
            constExpr -= curVar
        rhs = 0
        if i == fromNode:
            rhs = 1
        if i == toNode:
            rhs = -1
    model.addLConstr(lhs=constExpr, sense=GRB.EQUAL, rhs=rhs)

model.update()

# write the model in a file to make sure it is constructed correctly
model.write(filename = "assignment7.lp")

# optimize the model
model.optimize()

# print optimal objective and optimal solution
print("\nOptimal Objective: " + str(model.ObjVal))
print("\nOptimal Solution:")
allVars = model.getVars()
for curVar in allVars:
    print(curVar.varName + " " + str(curVar.x))