class weight:

    @classmethod
    def compute_recommend_weight(cls, height, age):
        recommend_weight=(height-100+age%10)*0.9
        return recommended_weight


print('Enter height')
h= float(input())

print('enter age')
a= int(input())

weight= weight_recommend_weight(weight)
print(weight)
