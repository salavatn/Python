from tqdm import tqdm
import time

# Define the total number of iterations
total_iterations = 100

# Create a progress bar
progress_bar = tqdm(total=total_iterations, unit='iteration')

# Simulate a task
for i in range(total_iterations):
    # Perform the task
    time.sleep(0.1)  # Simulating some work being done
    
    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

# Task completed
print("Task completed!")
