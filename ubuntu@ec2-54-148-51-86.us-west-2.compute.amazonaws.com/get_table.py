def get_table(Hinfo, city):
    ''' 
    INPUT: Hinfo a pandas dataframe and city an entry
           in the 'cities' column.

    OUTPUT: A sub dataframe of Hinfo consisting of the
            best price to value ratio.
    '''
    hcity = Hinfo[Hinfo['cluster'] == 0]
    hcity = hcity[hcity['city'] == city]
    hcity = hcity[hcity['price'] < 200]
    cols = ['price', 'avgO', 'avgV', 'avgR', 'avgL', 'avgC']
    col_names = ['$', 'overall', 'val', 'rm', 'loc', 'clean']
    hcity = hcity[cols]
    hcity.columns = col_names
    hcity['$/val'] = hcity['$'] / hcity['val']
    col_names.append('$/val')
    rows = hcity[col_names].sort('$/val', ascending=True)
    rows = rows[:10]
    for col in col_names:
        rows[col] = rows[col].round(decimals=3)
    return rows
