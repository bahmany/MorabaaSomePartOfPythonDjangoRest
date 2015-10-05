from rest_framework import permissions



class IsAccountOwner(permissions.BasePermission):


    def has_object_permission(self, request, view, user):
        if request.user:
            if user == request.user:
                if request.user.is_superuser and (
                        request.DATA.get('action', None) == 'delete' or request.DATA.get('action',
                                                                                         None) == 'passive/active'):
                    return False
            elif request.user.is_superuser:
                return True
            if not request.user.is_superuser and (
                        request.DATA.get('action', None) == 'delete' or request.DATA.get('action',
                                                                                         None) == 'passive/active'):
                return False
            return user == request.user
        return False