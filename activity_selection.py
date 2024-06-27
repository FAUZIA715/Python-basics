def activity_selection(start_time, end_time):
    """
    Select the maximum number of activities that can be performed
    by a single person, given a set of activities with start and
    end times. The goal is to maximize the number of activities
    performed while avoiding conflicts between them.

    Args:
    start_time (list): A list of integers representing the start
        times of the activities.
    end_time (list): A list of integers representing the end times
        of the activities.

    Returns:
    A list of integers representing the indices of the selected
    activities in the order they are selected.
    """
    n = len(start_time)  # number of activities
    selected_activities = []  # initialize the list of selected activities
    i = 0  # index for the first activity in the sorted list
    selected_activities.append(i)  # select the first activity
    for j in range(n):
        if start_time[j] >= end_time[i]:  # check for conflicts
            selected_activities.append(j)  # select the activity
            i = j  # update the index for the last selected activity
    return selected_activities


# Example usage:
start_time = [5,1,3,0,5,8]
end_time = [9,2,4,6,7,9]

selected_activities = activity_selection(start_time, end_time)

print("Selected activities:", selected_activities)
