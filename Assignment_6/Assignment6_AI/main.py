import csv
import random

from matplotlib import pyplot


# Reads the points from the file (without the first line).
def read_points(file_name):
    points = dict()
    with open(file_name, "r") as file:
        read_file = csv.reader(file, delimiter=',')
        passed_first_line = False
        for line in read_file:
            if passed_first_line:
                points[(float(line[1]), float(line[2]))] = line[0]
            else:
                passed_first_line = True
    return points


# Returns the distance between two points.
def distance_between_points(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


# Gets the closest centroids for a specific point.
def get_closest_centroid(centroids, point):
    solution = centroids[0]

    for centroid in centroids[1:]:
        if distance_between_points(centroid, point) < distance_between_points(solution, point):
            solution = centroid

    return solution


# Generates a new set of centroids.
def generate_new_centroids(points, k):
    minX = min([point[0] for point in points])
    maxX = max([point[0] for point in points])
    minY = min([point[1] for point in points])
    maxY = max([point[1] for point in points])

    # Creates a new 'empty' list of centroids.
    centroids = [[0, 0] for i in range(k)]

    centroids_count = [0 for i in range(k)]

    for point in points:
        centroids_count[points[point]] += 1
        centroid = centroids[points[point]]
        centroid[0] += point[0]
        centroid[1] += point[1]
    to_return = []

    for i, centroid in enumerate(centroids):
        if centroids_count[i] != 0:
            to_return.append((centroid[0] / centroids_count[i], centroid[1] / centroids_count[i]))
        else:
            to_return.append((random.random() * (maxX - minX) + minX, random.random() * (maxY - minY) + minY))
    return to_return


# The solver of the K-Means Algorithm.
def solver(read_points, k):
    solution = dict()
    minX = min([point[0] for point in read_points])
    maxX = max([point[0] for point in read_points])
    minY = min([point[1] for point in read_points])
    maxY = max([point[1] for point in read_points])
    centroids = []

    for i in range(k):
        centroids.append((random.random() * (maxX - minX) + minX, random.random() * (maxY - minY) + minY))

    iterations = 100

    for i in range(iterations):
        for point in read_points:
            centroid = get_closest_centroid(centroids, point)
            solution[point] = centroids.index(centroid)
        if i != iterations - 1:
            centroids = generate_new_centroids(solution, k)
    return solution, centroids

# Generates the Stats that checks which points are in every cluster.
def get_stats(read_points, computed_points, k):
    guys = [dict() for i in range(k)]
    for point in read_points:
        if read_points[point] not in guys[computed_points[point]]:
            guys[computed_points[point]][read_points[point]] = 0
        guys[computed_points[point]][read_points[point]] += 1
    return guys


if __name__ == '__main__':
    file_name = 'dataset.csv'

    read_points = read_points(file_name)

    k = 4

    points, centroids = solver(read_points, k)

    stats = get_stats(read_points, points, k)
    accuracy = sum([max(stat.values()) for stat in stats]) / len(read_points)
    print(stats)
    print(f"accuracy: {accuracy}")
    colors = ["magenta", "cyan", "green", "yellow"]
    for point in points:
        pyplot.scatter(point[0], point[1], color=colors[points[point]])
    for point in centroids:
        pyplot.scatter(point[0], point[1], color="black")
    pyplot.show()
