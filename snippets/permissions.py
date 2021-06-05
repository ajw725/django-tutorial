from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow anyone to read snippets, but only a snippet's owner can edit it
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, and OPTIONS are read operations that are allowed for anyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # only the snippet's owner can do anything other than read it
        return obj.owner == request.user