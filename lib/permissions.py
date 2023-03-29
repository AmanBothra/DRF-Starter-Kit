from rest_framework import permissions

from lib import constants


class AdminReadPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.ADMIN:
            if hasattr(view,
                       'action') and view.action in permissions.SAFE_METHODS or request.method in permissions.SAFE_METHODS:
                return True
        return False


class AdminWritePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.ADMIN:
            return True
        return False


class OrganizationAdminReadPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.ORGANIZATION_ADMIN:
            if hasattr(view,
                       'action') and view.action in permissions.SAFE_METHODS or request.method in permissions.SAFE_METHODS:
                return True
        return False


class OrganizationAdminWritePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.ORGANIZATION_ADMIN:
            return True
        return False


class OrganizationUserReadPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.ORGANIZATION_USER:
            if hasattr(view,
                       'action') and view.action in permissions.SAFE_METHODS or request.method in permissions.SAFE_METHODS:
                return True
        return False


class OrganizationUserWritePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.ORGANIZATION_USER:
            return True
        return False


class TransporterReadPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.TRANSPORTER:
            if hasattr(view,
                       'action') and view.action in permissions.SAFE_METHODS or request.method in permissions.SAFE_METHODS:
                return True
        return False


class TransporterWritePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.TRANSPORTER:
            return True
        return False


class CustomerReadPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.CUSTOMER:
            if hasattr(view,
                       'action') and view.action in permissions.SAFE_METHODS or request.method in permissions.SAFE_METHODS:
                return True
        return False


class CustomerWritePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.tame_user.user_type == constants.CompanyUserConstants.CUSTOMER:
            return True
        return False
