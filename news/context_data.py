from posts.models import CategoryModel


def get_category(request):
    return {
        'category': CategoryModel.objects.all()
    }
