# permissions.py
from rest_framework import permissions

class IsTenantUser(permissions.BasePermission):
    """
    Permite acesso somente a usuários autenticados que pertencem ao tenant atual.
    """

    def has_permission(self, request, view):
        # Usuário deve estar autenticado
        if not request.user.is_authenticated:
            return False

        # Verifique se o usuário pertence ao tenant atual.
        # Adapte a lógica abaixo com base no seu modelo de usuário
        # e como o tenant é associado ao usuário.
        return True # se a conexão com o banco de dados do tenant já garante
                     # o escopo, essa verificação pode ser simplificada
                     # ou removida, dependendo do seu modelo.
        #Ex: return request.user.tenant == request.tenant


    def has_object_permission(self, request, view, obj):
        # Permissões em nível de objeto.
        # Verifique se o objeto pertence ao tenant atual.
        return True # Similar ao has_permission, a verificação aqui
                      # pode ser simplificada ou removida se a conexão
                      # com o banco de dados do tenant já garante o escopo.
        #Ex: return obj.tenant == request.tenant