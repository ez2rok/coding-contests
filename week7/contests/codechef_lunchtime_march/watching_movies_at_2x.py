# cook your dish here
total_movie_length, double_speed_movie_length = tuple([int(x) for x in input().split()])
time_spent_watching_movie = (total_movie_length - double_speed_movie_length) + double_speed_movie_length // 2
print(time_spent_watching_movie)
