# dict = {

#     "name":"sonam",
#     "age":34
# }

# dict["name"] = "prabhat"
# print(dict)


# Nested dictonaries

# students = {
#     "name": "sonam",
#     "marks":{
#         "physics": 34,
#         "maths": 45
#     }
# }
# print(students["marks"]["physics"])



# collection = {1,2,2,2,"hello","worl"}
# print(collection) // set isunordered value


# set1 = {1,2,3,4}
# set2 = {2,3,4}

# print(set1.union(set2))


# set_1 = {"puthon","c++","java","javaScript","sql","sql"}
# print(len(set_1))


marks = {}

x = int(input("enter the physics: "))
marks.update({"physics": x})

y = int(input("enter the math: "))
marks.update({"math": y})

z = int(input("enter the bio: "))
marks.update({"bio": z})

print(marks)