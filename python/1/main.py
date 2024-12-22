
with open("input.txt", "r") as input_file:
    input_values = input_file.read()
    input_values = input_values.split("\n")

left_list = []
right_list = []

for value in input_values:
    left, right = value.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))

# left_list.sort()
# right_list.sort()
#
# total_distance = 0
# for i in range(1000):
#     total_distance += abs(left_list[i] - right_list[i])
# print(f"Total distance: {total_distance}")

similarities = {}  # left_list_item: item_similarity_score
for i in range(1000):
    number = left_list[i]
    number_count_in_right_list = 0
    for j in range(1000):
        if right_list[j] == number:
            number_count_in_right_list += 1
    similarities.update({number: number * number_count_in_right_list})

total_similarity = 0
for i in range(1000):
    number = left_list[i]
    total_similarity += similarities[number]
print(f"Total similarity score: {total_similarity}")