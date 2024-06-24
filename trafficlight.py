import matplotlib.pyplot as plt

class TrafficLightPhase:
    def __init__(self, direction, movement, duration):
        """
        Initialize a TrafficLightPhase object.

        Parameters:
        - direction (str): Direction of the traffic light phase (e.g., 'A (South)', 'B (East)', etc.).
        - movement (str): Movement associated with the phase (e.g., 'Straight', 'Left', 'Right').
        - duration (int): Duration of the phase in seconds.
        """
        self.direction = direction
        self.movement = movement
        self.duration = duration

def main():
    num_phases = 12
    total_time_steps = 60
    green_durations = [5] * num_phases  # Example durations for each phase in seconds

    directions = ['A (South)', 'B (East)', 'C (North)', 'D (West)']
    movements = ['Straight', 'Left', 'Right']
    phases = [TrafficLightPhase(directions[i // 3], movements[i % 3], green_durations[i]) for i in range(num_phases)]

    current_time_step = 0
    current_phase_index = 0
    current_phase_time_left = phases[current_phase_index].duration

    phase_changes = []

    # Simulate the traffic light phases over time steps
    while current_time_step < total_time_steps:
        phase_changes.append((current_time_step, current_phase_index))
        print(f"At time step {current_time_step}, phase is {current_phase_index + 1} ({phases[current_phase_index].direction} - {phases[current_phase_index].movement}) for {phases[current_phase_index].duration} seconds")

        current_time_step += 1
        current_phase_time_left -= 1

        if current_phase_time_left == 0:
            current_phase_index = (current_phase_index + 1) % num_phases
            current_phase_time_left = phases[current_phase_index].duration

    # Plot the phases over time
    plot_phase_changes(phase_changes, phases, total_time_steps)

    # Plot the time complexities (best case, worst case, average case)
    plot_time_complexities(total_time_steps)

def plot_phase_changes(phase_changes, phases, total_time_steps):
    """
    Plot the traffic light phases over time.

    Parameters:
    - phase_changes (list of tuples): List of (time_step, phase_index) tuples representing phase changes over time.
    - phases (list of TrafficLightPhase): List of TrafficLightPhase objects representing each phase.
    - total_time_steps (int): Total simulation time in time steps.
    """
    times = [change[0] for change in phase_changes]
    phase_indices = [change[1] for change in phase_changes]
    phase_labels = [f'{phases[i].direction} - {phases[i].movement}' for i in range(len(phases))]

    plt.figure(figsize=(12, 6))
    plt.plot(times, phase_indices, marker='o', linestyle='-', color='b')
    plt.title('Traffic Light Phases Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Phase')
    plt.xticks(range(0, total_time_steps + 1, 5))
    plt.yticks(range(len(phases)), labels=phase_labels)
    plt.grid(True)
    plt.tight_layout()

def plot_time_complexities(total_time_steps):
    """
    Plot the time complexities: best case (O(1)), worst case (O(total_time_steps)), and average case (O(total_time_steps)).

    Parameters:
    - total_time_steps (int): Total number of time steps considered for the complexity analysis.
    """
    x = list(range(1, total_time_steps + 1))
    y_best = [1] * total_time_steps  # Best case: O(1)
    y_worst = list(range(1, total_time_steps + 1))  # Worst case: O(total_time_steps)
    y_average = list(range(1, total_time_steps + 1))  # Average case: O(total_time_steps)

    # Create subplots with horizontal arrangement
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # Plot best case
    ax1.plot(x, y_best, label='Best Case: O(1)', linestyle='-', color='g')
    ax1.set_title('Best Case Time Complexity')
    ax1.set_xlabel('Total Time Steps')
    ax1.set_ylabel('Operations')
    ax1.legend()
    ax1.grid(True)

    # Plot worst case
    ax2.plot(x, y_worst, label='Worst Case: O(total_time_steps)', linestyle='-', color='r')
    ax2.set_title('Worst Case Time Complexity')
    ax2.set_xlabel('Total Time Steps')
    ax2.set_ylabel('Operations')
    ax2.legend()
    ax2.grid(True)

    # Plot average case
    ax3.plot(x, y_average, label='Average Case: O(total_time_steps)', linestyle='-', color='b')
    ax3.set_title('Average Case Time Complexity')
    ax3.set_xlabel('Total Time Steps')
    ax3.set_ylabel('Operations')
    ax3.legend()
    ax3.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
