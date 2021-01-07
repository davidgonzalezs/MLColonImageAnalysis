import pandas as pd 
import os



def main():
    #Load data in dataframe
    df = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.csv'))
    
    ones = df[df.relevant==1].count()
    print(ones)





if __name__ == "__main__":
    main()