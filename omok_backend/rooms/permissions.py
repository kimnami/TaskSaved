from rest_framework import permissions


class IsOmokAdmin(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True

        if request.method == 'POST':
            if request.user.username == 'omok_admin':
                return True


class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True

        if request.method == 'POST':
            if request.user == obj.room.player1 or request.user == obj.room.player2:
                return True
#     def has_object_permission(self, request, view, obj):
# # Room.objects.get(pk=self.kwargs.get('pk')
#         print(obj.room.player1.id," ")
#         print(obj.room.player2.id," ")
#         print(request.user.id)
#
#         if request.method in permissions.SAFE_METHODS:
#             return True

        # if request.method =='POST':
        #     print("F")
        #     if request.user.id == obj.room.player1.id:
        #         print("U")
        #         return True
        #         print("C")
        #     if request.user.id == obj.room.player2.id:
        #         print("K")
        #         return True

        # if request.method =='POST' and (request.user.id == obj.room.player1.id or request.user.id == obj.room.player2.id):
        #     return True


# class IslenderOrBorrowerReadOnly(permissions.BasePermission):
#     """
#     LENDER에게만 쓰기를 허용하고
#     BORROWER만 읽기를 허용하는 커스텀 권한
#
#     """
#
#     def has_object_permission(self, request, view, obj):
#         # 읽기 권한은 BORROWER에게만 허용하므로,
#         # GET, HEAD, OPTIONS 요청은 항상 허용함
#         if request.method in permissions.SAFE_METHODS:
#             if obj.borrower == request.user:
#                 return True
#
#         if request.user.username == 'debt_admin':
#             return True
#
#         # 쓰기 권한은 코드 조각의 소유자에게만 부여함
#         if request.method != 'PUT':
#             return obj.lender == request.user
#
#
# class IsRequestUser(permissions.BasePermission):
#     """
#     요청 유제에게만 보기를 허용하는 커스텀 권한
#     """
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             if obj == request.user:
#                 return True
#
#         if request.user.username == 'debt_admin':
#             return True
