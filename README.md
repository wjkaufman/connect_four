# Connect Four AI

To get my sig from Tad, I'm making a reinforcement learning AI to play connect four. Let's go!

### How Stuff is Written

The board keeps track of the current state of the game. Players are numbered 1,2 on the board (0 is empty).

### My Understanding of the Theory

When making an AI to play Connect Four, I think it needs to evaluate the moves it has, and pick the one that maximizes the chances of it winning. Simple enough. Maybe not simple.

Let $x$ be the current state (board, whose move it is), and $f(x)$ be the chance player 1 wins. So it would check all available moves it has, then pick the move that maximizes its chance of winning (same as minimizing the chance it opponent wins). It could also, to improve accuracy, go to some depth $d$ down the tree, evaluate probabilities there, then pick the branch that maximizes probabilities. This is where $\alpha/\beta$ testing comes in.

### Resources

- [A githob repo](https://github.com/SamRagusa/Checkers-Reinforcement-Learning)
- [some](https://en.wikipedia.org/wiki/Q-learning) [wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) page

### To Do

- Probably save the entire model, rather than just the weights (easier to reload when I want to play it)
- Something to try: change the reward from binary (1 if win, -1 if loss) to a numerical scale of how quickly you win or slowly you use.