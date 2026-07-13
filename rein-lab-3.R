# Install once if needed
# install.packages("DiagrammeR")

library(DiagrammeR)

grViz("
digraph MDP {

graph [
  layout = dot,
  rankdir = TB,
  bgcolor = white,
  nodesep = 0.5,
  ranksep = 0.7,
  splines = line
]

node [
  shape = box,
  style = 'rounded,filled',
  fontname = Helvetica,
  fontsize = 12,
  color = black,
  penwidth = 1.5
]

edge [
  color = black,
  penwidth = 1.2,
  arrowsize = 0.8
]

Start      [label='Start', fillcolor='#4CAF50', fontcolor='white']
Problem    [label='Problem Definition', fillcolor='#AED6F1']
States     [label='State Space (S)', fillcolor='#A9DFBF']
Actions    [label='Action Space (A)', fillcolor='#A9DFBF']
Transition [label='Transition Probability', fillcolor='#A9DFBF']
Reward     [label='Reward Function', fillcolor='#A9DFBF']
Discount   [label='Discount Factor (γ)', fillcolor='#A9DFBF']

Observe    [label='Observe Current State', fillcolor='#FCF3CF']
Choose     [label='Choose Action', fillcolor='#FCF3CF']
Execute    [label='Execute Action', fillcolor='#FCF3CF']
Receive    [label='Receive Reward', fillcolor='#FCF3CF']
Update     [label='Update Value / Policy', fillcolor='#FAD7A0']

Decision [
  shape = diamond,
  label = 'Converged?',
  fillcolor = '#F8C471'
]

Policy [label='Optimal Policy', fillcolor='#F1948A']
Value  [label='Optimal Value Function', fillcolor='#F1948A']
End    [label='End', fillcolor='#E74C3C', fontcolor='white']

Start -> Problem
Problem -> States
States -> Actions
Actions -> Transition
Transition -> Reward
Reward -> Discount
Discount -> Observe
Observe -> Choose
Choose -> Execute
Execute -> Receive
Receive -> Update
Update -> Decision

Decision -> Observe [label='No']
Decision -> Policy [label='Yes']

Policy -> Value
Value -> End

}
")
