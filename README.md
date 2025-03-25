# Implementação do Algoritmo de Seleção Simultânea do Maior e do Menor Elementos (MaxMin Select)

### Como executar

Este código não possuí dependências, basta rodar o script da seguinte maneira:

```
python main.py
```

o arquivo é executado com um array de exemplo já inserido no código.

### Explicação linha a linha

```python
def maxmin(array):
    lenght = len(array)
```
A função pega um array de tamanho n e salva seu comprimento como uma variável length.

```python
if lenght == 0:
        return None
    elif lenght == 1:
        return (array[0], array[0])
    elif lenght == 2:
        return(max(array), min(array))
```
Se o comprimento for 0, retorna nenhum valor; se for 1, retorna o mesmo elemento como mínimo e máximo; se for 2, o código compara entre ambos elementos se um é maio que o outro e retorna.

```python
else:  
        split = lenght // 2
        lf_max, lf_min = maxmin(array[:split])
        rt_max, rt_min = maxmin(array[split:])
        return(max(lf_max, rt_max), min(lf_min, rt_min))
```

se for um array de comprimento maior, ele é dividido em dois e cada metade passa pelo algoritmo de maneira recursiva até que os máximos e mínimos de cada ponta sejam comparados.