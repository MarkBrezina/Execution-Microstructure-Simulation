https://colab.research.google.com/drive/1C1FSH4kOTEq42hP6LK-Q5lyVofiJJFD1?authuser=1#scrollTo=PApZM9kiXioE


# Execution Microstructure Simulation

This repository implements a simulation environment for studying
financial market microstructure and order execution.

The goal is to model how orders interact inside a limit order book
and explore how different execution strategies affect market impact
and execution quality.

The project simulates:

• Limit order books  
• Order flow dynamics  
• Market orders and limit orders  
• Order cancellation  
• Execution algorithms  
• Price formation

The simulation can be used to study:

• market impact
• order book imbalance
• liquidity dynamics
• execution strategies
• optimal trade scheduling


Example simulation:

price
  ^
  |
102|       ████
101|    █████████
100|███████████████
 99|████████████
 98|   ███████
      ---------------->
      bid        ask
