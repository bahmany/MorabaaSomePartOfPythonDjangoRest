import json
import uuid
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from rest_framework import viewsets, permissions, views
from rest_framework.decorators import detail_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from amsp import settings
from amspApp.CompaniesManagment.models import Company
from amspApp.Infrustructures.Classes.SendMail import sendMail
from amspApp.amspUser.models import MyUser
from amspApp.amspUser.permissions.UserPermissions import IsAccountOwner
from amspApp.amspUser.serializers.UserGroupSerializer import UserGroupSerializer
from amspApp.amspUser.serializers.UserSerializer import UserSerializer
from rest_framework import status


class UserListPagination(PageNumberPagination):
    page_size = 14
    page_size_query_param = 'page_size'
    max_page_size = 50


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserListPagination
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner())

    def create(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
                            'status': 'Bad request',
                            'message': serializer.errors,
                        }, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        query = self.request.GET.get('query')
        item_per_page = self.request.GET.get('itemPerPage')

        if item_per_page and not item_per_page == 'undefined':
            self.pagination_class.page_size = item_per_page

        if query and not query == 'undefined':
            search_text = self.request.GET['query']
            queryset = MyUser.objects.filter(Q(username__contains=search_text) |
                                             Q(email__contains=search_text) |
                                             Q(first_name__contains=search_text) |
                                             Q(last_name__contains=search_text) & Q(is_deleted=False)
            )
        else:
            queryset = MyUser.objects.filter(is_deleted=False)
        return queryset

    def partial_update(self, request, *args, **kwargs):
        request.user.current_company = Company.objects.get(id=request.data["current_company"])
        request.user.save()
        return Response({'id': request.user.current_company.id, 'name': request.user.current_company.name},
                        status.HTTP_200_OK)


    def template_view(self, request, *args, **kwargs):
        gt_datas_title = [
            'id',
            'username'
            'email',
            'active',
            'staff',
            'superuser',
            'lastlogin ',
        ]

        gt_datas_dbtitle = [
            'id',
            'username',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            "last_login | jalaliDateFromNow:'jYYYY-jMM-jDD hh:mm:ss' ",
        ]

        gt_buttons = [
            {'type': 'primary fa fa-edit', 'func': 'userEdit(obj.username)', 'is_toggle_func': 's', 'is_toggle': 0},
            {'type': 'info fa fa-key', 'func': 'passEdit(obj.username)', 'is_toggle_func': 's', 'is_toggle': 0},
            {'type': 'warning fa fa-lock', 'type2': 'success fa fa-unlock', 'is_toggle_func': 'is_active',
             'func': 'userPassive(obj.username)', 'title': 'passive',
             'is_toggle': 1},
            {'type': 'danger fa fa-trash', 'func': 'userDelete(obj.username)', 'is_toggle_func': 's', 'is_toggle': 0}

        ]

        gm_user_buttons = [
            {'type': 'success fa fa-save', 'func': 'saveUserEdit()', 'title': ''},
            {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
        ]

        gm_pass_buttons = [
            {'type': 'success fa fa-save', 'func': 'savePassEdit()', 'title': ''},
            {'type': 'danger fa fa-times', 'func': 'cancel()', 'title': ''},
        ]

        gm_aresure_buttons = [
            {'type': 'success fa fa-check', 'func': 'yes()', 'title': ''},
            {'type': 'danger fa fa-times', 'func': 'no()', 'title': ''},
        ]

        serializer = self.get_serializer()
        renderer = HTMLFormRenderer()
        gm_user_form = renderer.render(serializer.data, renderer_context={
            'template': 'forms/amsp-user/EditUsernameEmail.html',
            'request': self.request
        })

        gm_pass_form = renderer.render(serializer.data, renderer_context={
            'template': 'forms/amsp-user/EditPass.html',
            'request': self.request
        })

        # gt_ means GenericTable
        # gm_ means GenericModal

        data = {'gm_items': [{
                                 'gm_modal_title': 'edituser',
                                 'gm_modal_id': 'GenericModalUserEdit.html',
                                 'gm_form': gm_user_form,
                                 'gm_buttons': gm_user_buttons},
                             {
                                 'gm_modal_title': 'editpass',
                                 'gm_modal_id': 'GenericModalPassEdit.html',
                                 'gm_form': gm_pass_form,
                                 'gm_buttons': gm_pass_buttons},
                             {
                                 'gm_modal_title': 'areyuosure',
                                 'gm_modal_id': 'GenericModalAreYouSure.html',
                                 'gm_form': 'areusure',
                                 'gm_buttons': gm_aresure_buttons},
                             {
                                 'gm_modal_title': 'forbiden',
                                 'gm_modal_id': 'GenericModalPermissionDenied.html',
                                 'gm_form': 'permissiondenied',
                                 'gm_buttons': [{'type': 'success fa fa-check', 'func': 'ok()', 'title': ''}]}],
                'gt_table_title': 'userlist',
                'gt_object_name': 'user',
                'gt_func_col': 'col-md-2',
                'gt_search_func': 'searchUsers()',
                'gt_datas_title': gt_datas_title,
                'gt_datas_dbtitle': gt_datas_dbtitle,
                'gt_buttons': gt_buttons,
                'user_table_template': 'ani-theme/generic-templates/Table.html',
                'user_edit_modal': 'ani-theme/generic-templates/Modal.html',
        }

        return render_to_response('ani-theme/views/pages/dashboard/../../../templates/amsp-user/UsersTable.html', data,
                                  context_instance=RequestContext(self.request))


class LoginView(views.APIView):
    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)
        remember = data.get('remember', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(7 * 24 * 60 * 60)
                serialized = UserSerializer(user)

                return Response(serialized.data)
            else:
                return Response({
                                    'status': 'Unauthorized',
                                    'message': 'This account has been disabled.'
                                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                                'status': 'Unauthorized',
                                'message': 'Username/password combination invalid.'
                            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


class ForgetPassView(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'email'
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)

    def create(self, request, *args, **kwargs):
        if not "email" in request.data:
            return Response({"message": "Email not found", "status": "Unauthorized"},
                            status=status.HTTP_401_UNAUTHORIZED)

        self.queryset = MyUser.objects.filter(email=request.data["email"])
        if self.queryset.count() != 1:
            return Response({"message": "Email not found", "status": "Unauthorized"}, status=status.HTTP_404_NOT_FOUND)

        guidFirst = uuid.uuid4().hex
        guidSeccond = uuid.uuid4().hex
        guidThird = uuid.uuid4().hex
        finalGuid = guidFirst + guidSeccond + guidThird
        requestedUser = self.queryset[0]
        requestedUser.password_reset = finalGuid
        requestedUser.password_reset_post_date = datetime.now()
        requestedUser.save()
        addressOfThisHost = "http://%s/myapi/forgetpass/?q=%s" % (
            settings.CURRENT_HOST,
            finalGuid)
        subject = "Password Reset Link from Morabaa"
        message = """
        Dear user,
        You have been requested password reset link from morabaa,
        This link is available for 48 hours.
        click here to to reset your password : %s
        if this link sent without your request, please left it alone, it will be deleted in next 48 hours


        Morabaa - A new generation of Virtual Society


         best regards
         Morabaa...
        """ % addressOfThisHost
        addresses = [requestedUser.email]
        sendMail(subject, message, addresses)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        # key = request.query_params["q"]
        # self.queryset = MyUser.objects.filter(password_reset = key)
        return redirect("/#/ResetPassword/" + request.query_params["q"] + "/")


class ResetPassView(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'password_reset'
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)

    def create(self, request, *args, **kwargs):
        key = request.data["hashed"]

        if not request.data["newPass"] == request.data["ConfnewPass"]:
            return Response({
                                'status': 'Unauthorized',
                                'message': 'Password is not matched'
                            }, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data["newPass"]) < 4:
            return Response({
                                'status': 'Unauthorized',
                                'message': 'Password is too short it must be more than 4 chars'
                            }, status=status.HTTP_400_BAD_REQUEST)

        if len(key) != 96:
            return Response({
                                'status': 'Unauthorized',
                                'message': 'Invalid Key'
                            }, status=status.HTTP_400_BAD_REQUEST)

        userInstance = MyUser.objects.filter(password_reset=key)

        if userInstance.count() != 1:
            return Response({
                                'status': 'Unauthorized',
                                'message': 'User not found !!'
                            }, status=status.HTTP_400_BAD_REQUEST)

        userInstance = userInstance[0]
        userInstance.set_password(request.data["newPass"])
        userInstance.password_reset = ""
        userInstance.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


    def list(self, request, *args, **kwargs):
        return render_to_response('ani-theme/views/pages/../../../templates/authentication/resetpass.html', {},
                                  context_instance=RequestContext(request))



