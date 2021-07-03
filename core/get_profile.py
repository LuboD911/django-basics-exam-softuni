from exam.exam_profile.models import ProfileModel


def get_profile():
    return ProfileModel.objects.first()