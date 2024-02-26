from django.shortcuts import render

def home(request):

    topItems=[
        {'name':"Fish & Chips",'price':5,'img':"https://images.pexels.com/photos/19034918/pexels-photo-19034918/free-photo-of-fried-fish-and-chips-sprinkled-with-parsley.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},
        {'name':"Crispy Skin Chicken",'price':12,'img':"https://images.pexels.com/photos/6210933/pexels-photo-6210933.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},
        {'name':"Flank Steak	",'price':8,'img':"https://images.pexels.com/photos/7613561/pexels-photo-7613561.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"},





    ]

    return render(request,'home.html',{'topItems':topItems})