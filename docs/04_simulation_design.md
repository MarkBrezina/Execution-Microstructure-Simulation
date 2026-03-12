The simulation environment consists of several components.

Order Book
    stores active limit orders

Matching Engine
    matches market orders against the book

Agents
    generate trading behavior

Execution Algorithm
    schedules large orders

Market State
    describes liquidity conditions

Agent -> Order -> Matching Engine -> Order Book -> Trades
