from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS:
        #     return True

        return obj.author == request.user


class IsAssignee(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.assignee.all()
