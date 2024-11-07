class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, n):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # To keep track of free time slots
    result = [-1] * n

    # To keep track of the result (sequence of jobs)
    slot = [False] * n

    # Iterate through all given jobs
    for i in range(n):
        # Find a free slot for this job (start from the last possible slot)
        for j in range(min(n, jobs[i].deadline) - 1, -1, -1):
            # If a free slot is found
            if not slot[j]:
                result[j] = i  # Add this job to the result
                slot[j] = True  # Mark this slot as occupied
                break

    # Print the result
    print("Following is the maximum profit sequence of jobs:")
    for i in range(n):
        if slot[i]:
            print(f"Job {jobs[result[i]].id}", end=" ")
    print()

if __name__ == "__main__":
    # Take user input for the number of jobs
    n = int(input("Enter the number of jobs: "))

    # Create an empty list to store jobs
    jobs = []

    # Input each job's ID, deadline, and profit
    print("Enter job ID, deadline, and profit for each job:")
    for i in range(n):
        job_id = int(input(f"Job {i + 1} ID: "))
        deadline = int(input(f"Job {i + 1} Deadline: "))
        profit = int(input(f"Job {i + 1} Profit: "))
        jobs.append(Job(job_id, deadline, profit))

    # Perform job sequencing
    job_sequencing(jobs, n)
