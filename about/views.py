from django.shortcuts import render

def about(request):
    chefs=[
        {'name':"Peter Hart",'position':"CHEF",'img':"https://static.cordonbleu.edu/Files/MediaFile/70794.jpg"},
        {'name':"Maria",'position':"CHEF",'img':"https://oldtowncrier.com/wp-content/uploads/2017/01/chef-special-2-17-margaret.jpg"},
        {'name':"Alejandro",'position':"CHEF",'img':"https://www.prego-samui.com/storage/2023/02/APR_3355-2-scaled.jpg"},
    ]
    return render(request,'about.html',{'chefs':chefs})