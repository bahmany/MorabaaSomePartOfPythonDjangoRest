from rest_framework import permissions



class CanCruid(permissions.BasePermission):

    def has_object_permission(self, request, view, company):
        if request.method == 'DELETE':
            if company.automatically_created == True:
                return False
        if company.owner_user_id != request.user.id:
            return False

        return True


    # def has_permission(self, request, view):
    #     return True
