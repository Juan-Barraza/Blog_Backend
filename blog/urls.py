from django.urls import path
from .views import category, login, user, article, comment, multimedia
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('category/', category.CategoryView.as_view(), name='category'),
    path('user/', user.UserView.as_view(), name='user-created'),
    path('article/', article.ArticleView.as_view(), name='article_created'),
    path('comment/', comment.CommentView.as_view(), name='comment_created'),
    path('multimedia/', multimedia.MultimediaView.as_view(), name='multimedia_created'),
    path('login/', login.LoginView.as_view(), name='login_created'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
 ]