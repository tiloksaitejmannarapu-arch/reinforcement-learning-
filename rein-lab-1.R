#---------------------------------------
# Markov Decision Process Demonstration
#---------------------------------------

# Grid size
grid_size <- 4

# Start and Goal positions
start <- c(1,1)
goal  <- c(4,4)

# Initial state
state <- start

# Create grid
grid <- matrix(".", grid_size, grid_size)

grid[start[1], start[2]] <- "S"
grid[goal[1], goal[2]] <- "G"

cat("Initial Grid\n")
print(grid)

step <- 1

cat("\nStarting Simulation...\n\n")

while (!all(state == goal)) {
  
  row <- state[1]
  col <- state[2]
  
  possible <- list()
  
  # Possible actions
  if (row > 1)
    possible$Up <- c(row-1, col)
  
  if (row < grid_size)
    possible$Down <- c(row+1, col)
  
  if (col > 1)
    possible$Left <- c(row, col-1)
  
  if (col < grid_size)
    possible$Right <- c(row, col+1)
  
  best_action <- NULL
  best_distance <- Inf
  
  # Choose action with minimum Manhattan distance
  for (a in names(possible)) {
    
    next_state <- possible[[a]]
    
    distance <- abs(goal[1] - next_state[1]) +
      abs(goal[2] - next_state[2])
    
    if (distance < best_distance) {
      best_distance <- distance
      best_action <- a
      state_next <- next_state
    }
  }
  
  # Reward function
  reward <- ifelse(all(state_next == goal), 100, -1)
  
  # Mark visited path
  if (!all(state_next == goal))
    grid[state_next[1], state_next[2]] <- "*"
  
  # Display step details
  cat("Step:", step, "\n")
  cat("Current State :", state, "\n")
  cat("Action Taken  :", best_action, "\n")
  cat("Next State    :", state_next, "\n")
  cat("Reward        :", reward, "\n\n")
  
  print(grid)
  cat("\n")
  
  state <- state_next
  step <- step + 1
}

cat("----------------------------------\n")
cat("Goal Reached Successfully!\n")
cat("Total Steps Taken:", step - 1, "\n")
cat("----------------------------------\n")

