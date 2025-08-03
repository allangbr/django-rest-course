from rest_framework import permissions

class EhSuperUsuario(permissions.BasePermission):
  """
  Permissão personalizada para permitir acesso apenas a superusuários.
  """

  def has_permission(self, request, view):
    if request.method == 'DELETE':
      if request.user.is_superuser:
        return True
      return False
    return True  # Permite outros métodos para todos os usuários