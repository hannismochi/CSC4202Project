#TRAFFIC LIGHT SYSTEM

1) Problem statement : 
Innovatia, a bustling city known for its innovation and culture, faces a critical issue of severe traffic congestion, particularly during peak hours. This congestion leads to frustratingly long travel times, hindering economic productivity and contributing to environmental degradation. The city council seeks to address this challenge by designing an intelligent traffic management system to optimize traffic flow and reduce congestion, aiming to minimize total travel time for all vehicles by dynamically adjusting traffic light timings at intersections.

2) Algorithm Paradigm: Dynamic Programming

State Definition:
Defines ideal performance metric at time t while traffic signal is in phase i. 
Phase i may indicate different traffic signal orientations. 

State Transition:
Analyzes transition from one phase to another considering traffic signal timing and performance metrics. 
Defines transition functions considering current phase and assigned green time. 

Decision Variables:
The decision variable represents the duration of green traffic light stays in each traffic direction during each phase. 
The duration of the green signal assigned to phase i is denoted by gi. 

Objective Function:
The goal is to minimise the cumulative waiting time, line lengths, and number of stops within the specified time period T.
   
3) Pseudocode : 

         // Define constants and data structures
         num_phases = 12  // Total number of phases (4 directions x 3 movements)
         total_time_steps = 60  // Total simulation time in steps
         green_durations = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]  // Example durations for each phase
         
         directions = ['A (South)', 'B (East)', 'C (North)', 'D (West)']
         movements = ['Straight', 'Left', 'Right']

         // Initialize phase information
         phases = []
         for i = 0 to num_phases - 1:
             direction = directions[i // 3]
             movement = movements[i % 3]
             duration = green_durations[i]
             phases[i] = (direction, movement, duration)

         // Simulation loop
         current_time_step = 0
         current_phase_index = 0
         current_phase_time_left = phases[current_phase_index].duration
         
         phase_changes = []
         
         while current_time_step < total_time_steps:
             // Record current phase
             phase_changes.append((current_time_step, current_phase_index))

          // Print or log current phase details
          print("At time step", current_time_step, "phase is", current_phase_index, "(", phases[current_phase_index].direction, "-", phases[current_phase_index].movement, ")")
      
          // Update time step and remaining time in current phase
          current_time_step = current_time_step + 1
          current_phase_time_left = current_phase_time_left - 1
      
          // Check if current phase duration is over
          if current_phase_time_left == 0:
              // Move to the next phase
              current_phase_index = (current_phase_index + 1) % num_phases
              current_phase_time_left = phases[current_phase_index].duration

         // Function to plot phase changes
         function plot_phase_changes(phase_changes, num_phases, total_time_steps):
             // Extract time and phase indices for plotting
             times = [change[0] for change in phase_changes]
             phases = [change[1] for change in phase_changes]
   
       // Plot using a line graph
       plot(times, phases, marker='o')
       title('Traffic Light Phases Over Time')
       xlabel('Time')
       ylabel('Phase')
       xticks(range(0, total_time_steps + 1, 5))
       yticks(range(num_phases), labels=['A - Straight', 'A - Left', 'A - Right', 'B - Straight', 'B - Left', 'B - Right', 'C - Straight', 'C - Left', 'C - Right', 'D - Straight', 'D - Left', 'D - Right'])
       grid(True)
       show()

         // Main function
         function main():
             // Run the simulation
             simulate_traffic_light(phases, num_phases, total_time_steps)

             // Plot the results
             plot_phase_changes(phase_changes, num_phases, total_time_steps)
         
         // Execute main function
         main()

4) Output :

The graph shows the traffic light phases over time. The y-axis represents different phases, including directions (South, East, North, West) and specific turns (Straight, Left, Right). The x-axis represents time in seconds.

6) Algorithm Analysis : 
  
Worst Case - The worst case happens in the nested loop within the simulation loop. Here, the loop iterates through `total_time_steps` which is currently set to 60.Inside the loop, constant time operations like incrementing counters and comparisons occur.Therefore, the time complexity for the worst case is O(total_time_steps) which is linear in the number of simulation steps.

Best Case - There is no real "best case" in terms of time complexity because the loop always iterates through all time steps.

Average Case - The average case is also the same as the worst case, O(total_time_steps). The loop always iterates a fixed number of times regardless of the specific data.

7) Analysis of Time Complexity :
   
Best case : O(1)

Worse case : O(total_time_steps)

Average case : O(total_time_steps)

   
