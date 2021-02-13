# # Input the number for entries N such that 2<= N <= 5
# N = int(input())

# # Enter the name and scores of the students 1 by 1 in a individual list, create 
# # a master list of N elements, Master_List
# master_list = []
# for i in range(N):
#     sub_list = []
#     sub_list.append(str(input()))
#     sub_list.append(float(input()))
#     master_list.append(sub_list)

# # Create a new list 'Temp' with only unique scores, 
# # and sort it using >>> sorted(list)
# unique_score = []
# for j in range(N):
#     if master_list[j][1] not in unique_score:    
#         unique_score.append(master_list[j][1])

# unique_score_sorted = sorted(unique_score)

# # find the second lowest grade using >>> list[1] 
# # and assign it to a variable 'second_lowest_score'
# second_lowest_score = unique_score_sorted[1] 

# # compare the 'second_lowest_score' with the scores in the Master list and 
# # score matching names in a 'Unsorted_final_list'
# unsorted_student_final_list = []

# for k in range(len(master_list)):
#     if master_list[k][1] == second_lowest_score:
#         unsorted_student_final_list.append(master_list[k][0])

# # Sort the list using >>> sorted(list_name)
# sorted_student_list = sorted(unsorted_student_final_list)
# print(sorted_student_list)

# =========================================================




def swap_case(s):
    s = s.swapcase()
    print(s)
str1 = 'The Big Brown Book of the Adventure"'
swap_case(str1)