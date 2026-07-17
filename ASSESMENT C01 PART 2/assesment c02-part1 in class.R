#=========================================================
# Markov Decision Process (MDP) Demo
# Beautiful Console Output + Professional Visualization
#=========================================================

library(ggplot2)

set.seed(123)   # For reproducible results

#-----------------------------
# Grid Initialization
#-----------------------------
grid_size <- 4

start <- c(1,1)
goal  <- c(4,4)

state <- start
step <- 1
total_reward <- 0

trajectory <- data.frame(
  step = 1,
  row = start[1],
  col = start[2]
)

#-----------------------------
# Display Initial Grid
#-----------------------------
cat("\n")
cat("==============================================\n")
cat("     MARKOV DECISION PROCESS SIMULATION\n")
cat("==============================================\n")
cat("Grid Size      :", grid_size, "x", grid_size, "\n")
cat("Start Position :", paste(start, collapse = ","), "\n")
cat("Goal Position  :", paste(goal, collapse = ","), "\n")
cat("==============================================\n\n")

#-----------------------------
# Simulation
#-----------------------------
while(!all(state == goal)){
  
  row <- state[1]
  col <- state[2]
  
  possible <- list()
  
  if(row > 1)
    possible$Up <- c(row-1, col)
  
  if(row < grid_size)
    possible$Down <- c(row+1, col)
  
  if(col > 1)
    possible$Left <- c(row, col-1)
  
  if(col < grid_size)
    possible$Right <- c(row, col+1)
  
  best_action <- NULL
  best_distance <- Inf
  state_next <- NULL
  
  for(action in names(possible)){
    
    next_state <- possible[[action]]
    
    distance <- abs(goal[1]-next_state[1]) +
      abs(goal[2]-next_state[2])
    
    if(distance < best_distance){
      
      best_distance <- distance
      best_action <- action
      state_next <- next_state
      
    }
    
  }
  
  # Exploration (20%)
  if(runif(1) < 0.20){
    
    random_action <- sample(names(possible),1)
    
    best_action <- random_action
    state_next <- possible[[random_action]]
    
  }
  
  reward <- -1
  
  if(all(state_next == goal))
    reward <- 100
  
  total_reward <- total_reward + reward
  
  #-----------------------------
  # Beautiful Console Output
  #-----------------------------
  cat("==============================================\n")
  cat(sprintf("STEP %d\n", step))
  cat("==============================================\n")
  cat(sprintf("Current State : (%d,%d)\n", state[1], state[2]))
  cat(sprintf("Action Taken  : %s\n", best_action))
  cat(sprintf("Next State    : (%d,%d)\n", state_next[1], state_next[2]))
  cat(sprintf("Reward        : %d\n", reward))
  cat("==============================================\n\n")
  
  state <- state_next
  step <- step + 1
  
  trajectory <- rbind(
    trajectory,
    data.frame(
      step = step,
      row = state[1],
      col = state[2]
    )
  )
  
}

#-----------------------------
# Final Result
#-----------------------------
cat("\n")
cat("#########################################################\n")
cat("#                SIMULATION COMPLETED                   #\n")
cat("#########################################################\n")
cat(sprintf("Total Steps  : %d\n", step-1))
cat(sprintf("Total Reward : %d\n", total_reward))
cat("Goal Successfully Reached!\n")
cat("#########################################################\n")

#=========================================================
# Beautiful Visualization
#=========================================================

grid <- expand.grid(
  col = 1:grid_size,
  row = 1:grid_size
)

grid$Cell <- "Empty"

grid$Cell[
  grid$row == start[1] &
    grid$col == start[2]
] <- "Start"

grid$Cell[
  grid$row == goal[1] &
    grid$col == goal[2]
] <- "Goal"

ggplot() +
  
  geom_tile(
    data = grid,
    aes(col, row, fill = Cell),
    colour = "black",
    linewidth = 1
  ) +
  
  geom_path(
    data = trajectory,
    aes(col, row),
    colour = "dodgerblue4",
    linewidth = 2,
    lineend = "round"
  ) +
  
  geom_point(
    data = trajectory,
    aes(col, row, colour = step),
    size = 6
  ) +
  
  geom_text(
    data = trajectory,
    aes(col, row, label = step),
    colour = "white",
    fontface = "bold",
    size = 4
  ) +
  
  scale_fill_manual(values = c(
    "Empty" = "grey95",
    "Start" = "forestgreen",
    "Goal" = "red3"
  )) +
  
  scale_colour_gradient(
    low = "skyblue",
    high = "navy"
  ) +
  
  scale_x_continuous(
    breaks = 1:grid_size
  ) +
  
  scale_y_reverse(
    breaks = 1:grid_size
  ) +
  
  coord_fixed() +
  
  labs(
    title = "MARKOV DECISION PROCESS (MDP)",
    subtitle = "Optimal Path from Start to Goal",
    x = "Columns",
    y = "Rows",
    colour = "Step",
    fill = ""
  ) +
  
  theme_minimal(base_size = 15) +
  
  theme(
    
    plot.title = element_text(
      face = "bold",
      size = 22,
      colour = "darkblue",
      hjust = 0.5
    ),
    
    plot.subtitle = element_text(
      size = 14,
      hjust = 0.5
    ),
    
    axis.title = element_text(
      face = "bold"
    ),
    
    axis.text = element_text(
      face = "bold",
      size = 12
    ),
    
    panel.grid = element_blank(),
    
    legend.position = "right"
  )