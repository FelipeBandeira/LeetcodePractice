def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool

    1) checa se valor da lista está no dict
    2) se nao estiver, adiciona
    3) se estiver, retorna verdadeiro
    4) se adicionar todos os elementos uma vez, retorna falso

    RUNTIME: beats 96%
    MEMORY: beats 28.91%
    """

    dict = {}
    for i in nums:
        if i in dict:
            return True
        else:
            dict[i]=1
    return False