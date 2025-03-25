def maxmin(array):
    lenght = len(array)
    
    if lenght == 0:
        return None
    elif lenght == 1:
        return (array[0], array[0])
    elif lenght == 2:
        return(max(array), min(array))
    else:  
        split = lenght // 2
        lf_max, lf_min = maxmin(array[:split])
        rt_max, rt_min = maxmin(array[split:])
        return(max(lf_max, rt_max), min(lf_min, rt_min))


def main():
     examplearr = [3, 1, 4, 1, 5, 9, 2, 6]
     
     maxarr, minarr = maxmin(examplearr)

     print(f"Mínimo: {minarr}, Máximo: {maxarr}")


if __name__ == "__main__":
    main()