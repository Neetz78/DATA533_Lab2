def recipe():
    
    '''The recipe package
     Importing all the required modules for execution
     Imports pandas,recipes.Veg.veg,recipes.NonVeg.nveg,recipes.Veg,recipes.NonVeg modules
     
     Parameters:
     
     data(Dataframe) : Consists of the recipe book.
     
     perf(Str) : Contians the food preference of the user.
     
     lev,nlev(Str) : It takes the difficulty level entered by the user
     
     a(class object) : An class object to call the respective easy, medium or difficult methods.
     
     
     '''
    
    import pandas as pd
    #import recipes.init as recipes
    import recipes.Veg.veg as veg
    import recipes.NonVeg.nveg as nveg
    from recipes.Veg import easy as e,intermediate as i,difficult as d 
    from recipes.NonVeg import easy as ne,intermediate as ni,difficult as nd
    
    

    data = pd.read_csv("Recipes.csv",encoding = "ISO-8859-1", engine='python')

    print("Please select your food preference")
    perf = input("Vegetarian or Non-Vegetarian:")
    if (perf == "Vegetarian" or perf == "Veg" or perf == "veg" or perf == "vegetarian"):
        lev = veg.level()
        if (lev == "Easy" or lev == "easy" or lev == "e" or lev == "EASY"):
            a=e.steps(data)
            a.seasy()
        elif (lev == "Medium" or lev == "medium" or lev == "m" or lev == "MEDIUM"):
            a=i.steps(data)
            a.smedium()
        elif (lev == "Difficult" or lev == "difficult" or lev == "d" or lev == "DIFFICULT"):
            a=d.steps(data)
            a.sdiff()
        else:
            pass
    
    elif (perf == "Non-Vegetarian" or perf == "Non-Veg" or perf == "nonveg" or perf == "nonvegetarian" or perf == "NonVegetarian"):
        nlev = nveg.level()
        if (nlev == "Easy" or nlev == "easy" or nlev == "e" or nlev == "EASY"):
            a=ne.steps(data)
            a.seasy()
        elif (nlev == "Medium" or nlev == "medium" or nlev == "m" or nlev == "MEDIUM"):
            a=ni.steps(data)
            a.smedium()
        elif (nlev == "Difficult" or nlev == "difficult" or nlev == "d" or nlev == "DIFFICULT"):
            a=nd.steps(data)
            a.sdiff()
        else:
            pass
    else:
        pass





