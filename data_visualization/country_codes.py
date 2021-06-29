from pygal.maps.world import COUNTRIES

unlisted_countries = {'ly':'Libya', 'bo':'Bolivia', 've':'Venezuela, RB', 'cd':'Congo, Dem. Rep.', 
'eg':'Egypt, Arab Rep.', 'tz':'Tanzania', 'cg':'Congo, Rep.'}

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, country in COUNTRIES.items():
        if country.lower() == country_name.lower():
            return code
        else:
            for code, country in unlisted_countries.items():
                if country_name.lower() == country.lower():
                    return code
    
    # If the country wasn't found, return None.
    return None