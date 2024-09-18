video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

#  Task 1:

#Implement the binary search algorithm for searching videos by title.

#Implement a sorting algorithm to ensure your binary search is searching through a sorted list. NO .sort() or sorted()

def merge(movies, left, right):

    l = 0
    r = 0
    a = 0

    while l < len(left) and r < len(right):
        
        if left[l] < right[r]:
            movies[a] = left[l]
            l += 1
            a += 1
        else:
            movies[a] = right[r]
            r += 1
            a += 1


    while l < len(left):
        movies[a] = left[l]
        l += 1
        a += 1

    while r < len(right):
        movies[a] = right[r]
        r += 1
        a += 1

def sort(movies):
    
    if len(movies) > 1:
        mid = len(movies) // 2
        left = movies[0:mid]
        right = movies[mid:]

        sort(left)
        sort(right)

        merge(movies, left, right)
    

def search(movies, target):
    high = len(movies) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2

        if movies[mid] == target:
            return mid
        elif movies[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


movie = "Exploring The Cosmos"

sort(video_titles)

print(search(video_titles, movie))