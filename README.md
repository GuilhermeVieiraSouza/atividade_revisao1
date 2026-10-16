# O que acontece quando você tenta apagar um local que tem evento relacionado? 

Como o local está com a Tag on_delete=PROTECT o admin não permite que um local com eventos seja apagado, os eventos estão protegidos, ele espera que antes faça a disassociação do evento daquele local. o Admin retorna o aviso:

"Cannot delete local
Deleting the local “refeitorio” would require deleting the following protected related objects:""