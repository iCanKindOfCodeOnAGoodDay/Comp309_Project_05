"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Project #5
    Created on Wednesday March 13 2 16:05 2024  
    Last Updated .... March 15 21:46

    Description: 
        
    The program creates a chart showing how long it takes to sort random numbers 
    using 3 data structures, 1) Standard Lists, 2) Python Arrays, and 3) NumpyArrays
        
    
    Inputs: 
        
    CreatePlot( xData, ydataforList, ydataforPythonArrays, ydataforNumpyArrays )
    
    mySortFunc( someList )
    
    check_sort( someList )

    getTimes( someProblemSizes )
  
    ListResults( someProblemSizes, seed, minRandom, maxRandom )
        
    ArrayResults( someProblemSizes, seed, minRandom, maxRandom )
        
    NumpyResults( someProblemSizes, seed, minRandom, maxRandom )
    
    
    
    Returns: 
        
    check_sort()- boolean to verify sorting
      
    ListResults()- List for plotting
    
    ArrayResults()- List for plotting
    
    NumpyResults()- List for plotting
        
    

    Dependencies: random, time, mathhplotlib.pyplot, numpy as np, array

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.3.1
"""


#-----imports section


import time, random, numpy as np, matplotlib.pyplot as plt, array




#-----definitions section


def main():
    
    """
    
    Description
    ----------  
    Our main() is the entry point to our program .... 

    Parameters
    ----------
    None.
            
    Returns
    -------
    None.

    """
    
    print( "Scott Quashen", time.asctime() ) 
    
    # constants
    N = [ 128, 256, 512, 1024, 2048, 4096, 8192, 16384 ] 
    
    # function calls
    createPlot( N, ListResults( N, 22, 0, 9999 ), ArrayResults( N, 22, 0, 9999 ), NumpyResults( N, 22, 0, 9999 ) )
    
    return None

# end of main function


def createPlot( dataSetSize, ListTimes, PythonArrayTimes, NumpyArrayTimes ):
    
    """
    
    Description
    ----------  
    createPlot() uses mathPlot to plot results for 1) Standard Lists, 2) Python Arrays, and 3) NumpyArrays

    Parameters
    ----------
        
    dataSetSize- List of integers which are our problem sizes
        
    ListTimes- List of float numbers which are our Measurements in seconds
        
    PythonArrayTimes- List of float numbers which are our Measurements in seconds
        
    NumpyArrayTimes- List of float numbers which are our Measurements in seconds
            
    Returns
    -------
    None.

    """
    
    X = [ str( t ) for t in dataSetSize ] # string values for x ticks
    
    X_axis = np.arange( len( dataSetSize ) ) 
    
    plt.bar( X_axis - 0.3, ListTimes, 0.3, label='List', color='brown' )
    plt.bar( X_axis + 0, PythonArrayTimes, 0.3, label='Array', color='orange' )
    plt.bar( X_axis + 0.3, NumpyArrayTimes, 0.3, label='NumpyArray', color='red' )

    plt.xticks( X_axis, X )    
    plt.title( "Performance Variance: List v. Array v. Numpy" )
    plt.xlabel( 'Problem Size' )
    plt.ylabel( 'Time (seconds)' )
    plt.legend( [ "List", "Array", "Numpy" ], loc=2 )    
    
    plt.savefig( "Scott Quashen_Project_05.png", dpi=600 )   
    plt.show()

# end createPlot() func


def ListResults( someProblemSizes, seed, minRandom, maxRandom ):
    
    """
    
    Description
    ----------
    
    Measure time taken to sort random numbers in built in LIST
    
    Parameters
    ----------
    
    someProblemSizes- List of integers which are our problem sizes.
        
    seed- Integer representing our seed value for random number generation.
    
    minRandom- Integer representing our lower bound for our random numbers.
    
    maxRandom- Integer representing our upper bound for our random numbers.
 
    Returns
    -------
    
    List- Floats of time measurements
 
    """
    
    ListResults = [ ]
    
    for i in range( len( someProblemSizes ) ):
                
        random.seed( 22, int ) # define seed value
   
# ------------------Built in LISTS
 # create LIST of random numbers
        L = [ random.randint( minRandom, maxRandom ) for t in range( someProblemSizes[ i ] ) ]      
# ------------------Built in LISTS
   
        start = time.time() # start
        
        mySortFunc( L ) # sort
        
        end = time.time() # end
        
        elapsedTime = end - start # measure
        
        # let's just not log fake times, if it don't work, just break it 
        if check_sort( L ) != True:
            print( 'The sort func was not succesful' )
            break;
        
        print( elapsedTime )
        ListResults.append( elapsedTime ) # add result
        
    return ListResults # pass results to plot func

# end list timing func


def ArrayResults( someProblemSizes, seed, minRandom, maxRandom ):
    
    """
    
    Description
    ----------
    
    Measure time taken to sort random numbers in Python Array
    
    Parameters
    ----------
    
    someProblemSizes- List of integers which are our problem sizes.
        
    seed- Integer representing our seed value for random number generation.
    
    minRandom- Integer representing our lower bound for our random numbers.
    
    maxRandom- Integer representing our upper bound for our random numbers.
 
    Returns
    -------
    List- Floats of time measurements
 
    """
    
    ListResults = [ ] # Fill with time measurements
    
    for i in range( len( someProblemSizes ) ):
                      
        random.seed( 22, int ) # define seed value
        
# ------------------PYTHON ARRAYS
# PYTHON ARRAY of random numbers
        L = array.array( 'i', [ random.randint( minRandom, maxRandom ) for t in range( someProblemSizes[ i ] ) ] )
# ------------------PYTHON ARRAYS
        
        start = time.time() # start
              
        mySortFunc( L ) # sort
              
        end = time.time() # end
               
        elapsedTime = end - start # measure
        
        # let's just not log fake times, if it don't work, just break it 
        if check_sort( L ) != True:
            print( 'The sort func was not succesful' )
            break;
        
        ListResults.append( elapsedTime ) # add result for plot
        
        print( elapsedTime )
        
    return ListResults # pass to plot func

# end python array timing func


def NumpyResults( someProblemSizes, seed, minRandom, maxRandom ):
    
    """
    
    Description
    ----------
    
    Measure time taken to sort random numbers in Numpy Array
    
    Parameters
    ----------
    
    someProblemSizes- List of integers which are our problem sizes.
        
    seed- Integer representing our seed value for random number generation.
    
    minRandom- Integer representing our lower bound for our random numbers.
    
    maxRandom- Integer representing our upper bound for our random numbers.
 
    Returns
    -------
    List- Floats of time measurements
 
    """
    
    ListResults = [] # Fill with time measurements
    
    for i in range( len( someProblemSizes ) ):
                
        random.seed( 22, int ) # define seed value
        
# ------------------NUMPY ARRAYS
# NUMPY ARRAY to store random numbers
        L = np.array( [ random.randint( minRandom, maxRandom ) for t in range( someProblemSizes[ i ] ) ] )
# ------------------NUMPY ARRAYS
   
        start = time.time() # start
        
        mySortFunc( L ) # sort
        
        end = time.time() # end
          
        elapsedTime = end - start # measure
        
        # let's just not log fake times, if it don't work, just break it 
        if check_sort( L ) != True:
            print( 'The sort func was not succesful' )
            break;
         
        ListResults.append( elapsedTime ) # add each result for plotting
        
        print( elapsedTime )
        
    return ListResults # pass results to the plot func 

# end python array timing func


def mySortFunc( someList ):
    
    """
    
    Description
    ----------
    The insertionSort() function inserts candidate to the left
    walking up each index until completed.
    
    Example
    ----------
        outer loop--------------------
        candidate =  24
        [143, 248, 929, 981, 24, 627, 457, 188, 718, 123]
        [143, 248, 929, 981, 981, 627, 457, 188, 718, 123]
        [143, 248, 929, 929, 981, 627, 457, 188, 718, 123]
        [143, 248, 248, 929, 981, 627, 457, 188, 718, 123]
        [24, 143, 248, 929, 981, 627, 457, 188, 718, 123]
    
    Parameters
    ----------
    someList- This is a list of random numbers for any problem size.

    Returns
    -------
    None.

    """
    
    # walk through each index sorting to the left
    for i in range( 1, len( someList ) ):
                
        # candidate to be inserted
        candidate = someList[ i ]
                
        j = i - 1       
        
        # now start searching for insertion walking down the items to the left 
        while ( j >= 0 and someList[ j ] > candidate ):  
                  
            # this process continues until we reach position 0, or find the position an item belongs
            someList[ j + 1 ] = someList[ j ]
            
            # decrement 
            j = j - 1           
            
        # The while loops breaks because we found the position to insert candidate; insert candidate, continue outter loop
        someList[ j + 1 ] = candidate
    
# end insertion sort func


def check_sort( someList ):
    
    """
    
    Description
    ----------
    check_sort() walks up each index ensuring that the previous index is not a greater number
   
    Parameters
    ----------
    someList- The List of random numbers we will be sorting
    
    Returns
    -------
    bool- True if the list is in ascending order, False if not. Breaks the for loop either way,
    early if false

    """
        
    for i in range( 1, len( someList ) ): 
        
        # begin at index 1
        if someList[ i - 1 ] > someList[ i ]:
            
        # if any are found, then the list is not order
            return False
        
        if i == len( someList ) - 1:
            
        # We've reached the end of list, all previous numbers in order, so the entire list is in order
            return True
            
# end of check_sort() function


#----Entry point

if __name__ == "__main__":
    main()


