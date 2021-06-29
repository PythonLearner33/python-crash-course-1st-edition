def check_gdp_tier(cc, gdp_2019, GDP_T1, GDP_T2, GDP_T3):
    '''Refactor of program to check GDP tier by 
       if-statements and append to appropiate lists.'''
    if cc:
        if gdp_2019 <= 10000000000: # 10,000,000,000
            GDP_T1[cc] = gdp_2019
        elif gdp_2019 <= 100000000000: # 100,000,000,000
            GDP_T2[cc] = gdp_2019
        else:
            GDP_T3[cc] = gdp_2019