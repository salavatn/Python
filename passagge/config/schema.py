from pydantic import BaseModel, Field
from typing import Optional, Union, List, Dict

class Product(BaseModel):
    title:      Optional[str] = Field(title='Product title')
    sku:        Optional[str] = Field(title='Product SKU')
    color:      Optional[str] = Field(title='Product color')
    brand:      Optional[str] = Field(title='Product brand')
    gender:     Optional[str] = Field(title='woman or man')
    material:   Optional[str] = Field(title='Product material')
    type:       Optional[str] = Field(title='Product type')
    category:   Optional[str] = Field(title='Product category')
    season:     Optional[str] = Field(title='Product season')
    collection: Optional[str] = Field(title='Product collection')
    inner:      Optional[str] = Field(title='Product collection inner')
    country:    Optional[str] = Field(title='Product country')
    price:      Optional[Union[str, int]] = Field(title='Product price')
    discount:   Optional[int] = Field(title='Product discount')
    sale:       Optional[bool] = Field(title='Product sale')
    size:       Optional[str] = Field(title='Product size')
    count:      Optional[int] = Field(title='Product count')


class FilterCondition(BaseModel):
    field:      Optional[str] = Field(title='Product title', min_length=3, max_length=50)
    operator:   Optional[str] = Field(title='Operator',      min_length=2, max_length=15) #, regex='^(IN|EQ|GT|LT|BETWEEN)$')
    value:      Optional[str] = Field(title='Value',         min_length=3, max_length=50)

class Filter(BaseModel):
    filters: Optional[List[FilterCondition]] = Field(default=None)
    limit: Optional[int] = Field(title='Get limit count', ge=0, le=100, default=10)
