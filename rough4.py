import random
import asciichartpy

def generate_random_data(num_points):
    # Generate random data for the chart
    data = [random.randint(0, 100) for _ in range(num_points)]
    return data

if __name__ == "__main__":
    num_points = 20  # Number of data points for the chart

    # Generate random data for the chart
    data = generate_random_data(num_points)

    # Plot the chart
    chart = asciichartpy.plot(data)

    # Display the chart in the terminal
    print(chart)
