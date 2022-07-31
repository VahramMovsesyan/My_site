from django.shortcuts import render
from datetime import date


posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Movsesyan",
        "data": date(2022, 7, 31),
        "title": "Mountain Hiking",
        "excert": "There's nothing like the views you get when hiking in the mountain! And I wasn't even prepared for what happend whilst I was enjoying the views",
        "content": """
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illum deleniti, 
            eaque sed et neque in, provident tempore dicta, ipsa sint quaerat!
            Asperiores tenetur quae est iusto enim eum amet atque.
            
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illum deleniti, 
            eaque sed et neque in, provident tempore dicta, ipsa sint quaerat!
            Asperiores tenetur quae est iusto enim eum amet atque.
            
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Illum deleniti, 
            eaque sed et neque in, provident tempore dicta, ipsa sint quaerat!
            Asperiores tenetur quae est iusto enim eum amet atque.
        
        """
    }
]

# Create your views here.


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
