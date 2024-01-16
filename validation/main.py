import pydantic

from pydantic import BaseModel


class Style(BaseModel):
    id: int
    name: str = 'niladri'
    account: str




if __name__ == "__main__":
    style_obj = Style(id='3',account = 'picc') # Note that string value of id was coerced to an int.
    print(style_obj.model_dump()) # returns a dictionary{'id': 2, 'name': 'niladri'}
    print(style_obj.model_dump_json())
    print(style_obj.model_fields_set)  #{'id'} , does not take into account the default attribues
    print(style_obj.model_computed_fields) # need to come back. not sure what it is
    print(style_obj.model_construct())
    # modelcopy = style_obj.model_copy()



    # json_data = style_obj.model_dump()
    # fields_set = style_obj.model_fields_set
    # newStyle_obj = Style.model_construct(_fields_set=fields_set, **json_data)
    # print(repr(newStyle_obj))
    # print(newStyle_obj.model_fields_set)









