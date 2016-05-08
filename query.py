"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# Get the brand with the **id** of 8.
Model.query.filter(id==8).all()
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(brand_name="Chevrolet", name="Corvette").all()
# Get all models that are older than 1960.
Model.query.filter(Model.year<1960).all()
# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded>1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("%oCor")).all()
# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter((Brand.founded == 1903)& (Brand.discontinued == None)).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter((Brand.founded < 1950)| (Brand.discontinued != None)).all()
# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name !='Chevrolet').all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    
    model_info = Model.query (model.brand_name,
                            model.name,
                            model.headquarters)

    for model in model_info:
        print model_info.name, model_info.brand_name, model_info. headquarters
                                                
        

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    models = Model.query.all()

    for model in models:
        print model.name, model.brand_name


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# you would get all names of cars that are Ford brand, they would be objects

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table helps to connect two tables that would have many-to-many relationships.
# This usually is formatted with a PK, and foriegn keys from other tables to link up different tables


# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brands = Brand.query.filter((Brand.name.like('%'+mystr+'%'))|(Brand.name == mystr)).all()
    
    return brands


def get_models_between(start_year, end_year):
    models = Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()

    return models
    
